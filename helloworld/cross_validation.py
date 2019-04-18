import pandas as pd
import os
import sys
import subprocess

def validate(working_dir: str):
    train_csv = 'train1.csv'
    menu = 'menu_train.csv'
    tags = 'menu_tagged.csv'
    NUM_TESTS = 5
    os.chdir(working_dir)
    all_data = pd.read_csv(train_csv, header=0, sep=',')
    total_rows = all_data.shape[0]
    batch_size = int(total_rows / NUM_TESTS)
    F1 = []
    f = open('result.txt', 'w')
    print(all_data.shape)
    for i in range(NUM_TESTS):
        start = i * batch_size
        test_data = all_data.iloc[start:start + batch_size, 0:4]
        test_data.drop_duplicates(inplace=True)
        test_data.to_csv('test.csv', index=False, header=True)
        train_data = pd.concat([all_data.iloc[:start, :], all_data.iloc[start + batch_size:, :]], ignore_index=True)
        train_data.to_csv('train.csv', index=False, header=True)
        subprocess.check_call(f'python train.py', shell=True, stdout=sys.stdout)
        subprocess.check_call(f'python predict.py', shell=True, stdout=sys.stdout)

        test_answers = all_data.iloc[start:start + batch_size, :]
        # test_answers.to_csv('answers.csv', index=False)
        prediction = pd.read_csv('prediction.csv', header=0, sep=',')
        total_matches = 0
        total_pred = 0

        answers = dict()
        for row in prediction.values:
            chknum, pred = row
            if not isinstance(pred, str):
                pred = []
            else:
                pred = [int(id) for id in pred.split()]
            answers[chknum] = pred
            total_pred += len(pred)

        answ = {}
        for row in test_answers.values:
            chknum, person_id, month, day, good, good_id = row
            if chknum in answ:
                answ[chknum].append(good_id)
            else:
                answ[chknum] = [good_id]

        pd.DataFrame([[key, " ".join([str(j) for j in sorted(val)])] for key, val in answ.items()], columns=['chknum', 'answ']).to_csv('answers.csv', index=False)

        for row in test_answers.values:
            chknum, person_id, month, day, good, good_id = row
            if good_id in answers[chknum]:
                answers[chknum].remove(good_id)
                total_matches += 1

        p = total_matches / total_pred
        r = total_matches / test_answers.shape[0]
        F1.append(2 * p * r / (p + r))
    print(F1[-1], file=f)
    print(sum(F1) / NUM_TESTS, file=f)
    f.close()

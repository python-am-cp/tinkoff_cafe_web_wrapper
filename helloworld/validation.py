from django.apps import AppConfig
import pandas as pd
import os
import sys
from pathlib import Path
import numpy as np
import importlib
import subprocess


def valid(working_dir: str):
    train_csv = 'train1.csv'
    menu = 'menu_train.csv'
    tags = 'menu_tagged.csv'
    NUM_TESTS = 5
    os.chdir(working_dir)
    all_data = pd.read_csv(train_csv, header=0, sep=',')
    kolvo_rows = all_data.shape[0]
    batch_size = int(kolvo_rows / NUM_TESTS)
    F1 = []
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
        prediction = pd.read_csv('prediction.csv', header=0, sep=',')
        kolvo_matches = 0
        kolvo_pred = 0

        answers = dict()
        for row in prediction.values:
            chknum, pred = row
            if not isinstance(pred, str):
                pred = []
            else:
                pred = [int(id) for id in pred.split()]
            answers[chknum] = pred
            kolvo_pred += len(pred)

        for row in test_answers.values:
            chknum, person_id, month, day, good, good_id = row
            if good_id in answers[chknum]:
                answers[chknum].remove(good_id)
                kolvo_matches += 1

        p = kolvo_matches / kolvo_pred
        r = kolvo_matches / test_answers.shape[0]
        F1.append(2 * p * r / (p + r))
    f = open('result.txt', 'w')
    print(sum(F1) / NUM_TESTS, file=f)
    f.close()


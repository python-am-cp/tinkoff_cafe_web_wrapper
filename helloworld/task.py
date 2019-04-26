import shutil
from django.core.mail import EmailMessage

from helloworld import cross_validation


def calculate_send_clear(curr_res):
    print("ya tut")
    # cross_validation.validate(curr_res.path)

    # with open(curr_res.path + 'result.txt', 'w+') as dest:
    #         dest.write('134423 \n 435423')

    # f = open(curr_res.path + "result.txt", "r")
    # while True:
    #     line1 = f.readline()
    #     line2 = f.readline()
    #     line3 = f.readline()
    #     if not line3:
    #         break
    # f.close()
    # subj = 'Результат' + ' ' + curr_res.resName
    # mail_content = 'Здравствуйте,' + ' ' + curr_res.name + ', ' + 'результат ' \
    #                'расчетов по метрике составил: ' + '\n\n' + str(line1) + \
    #                str(line2) + '\n\n' + 'Описание вашего исследования:' + ' ' \
    #                + curr_res.resDesc
    subj = 'Результат' + ' ' + curr_res.resName
    mail_content = 'Здравствуйте,' + ' ' + curr_res.name + ', ' + 'результат ' \
                   'расчетов по метрике составил: ' + '\n\n'

    msg = EmailMessage(subject=subj, body=mail_content, to=[curr_res.email])
    msg.send()
    shutil.rmtree(curr_res.path, ignore_errors=True)

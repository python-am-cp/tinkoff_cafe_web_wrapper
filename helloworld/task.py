import shutil
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tinkoff_web.settings')
from django.core.mail import send_mail
# from tinkoff_web import settings

from django.conf import settings

from sendgrid.helpers.mail import *
from helloworld import cross_validation



def calculate_send_clear(curr_res):
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

    print("hello")
    print(curr_res.email)
    snd = send_mail(subj,
                    mail_content,
                    settings.EMAIL_HOST_USER,
                    [curr_res.email],
                    fail_silently=False)
    shutil.rmtree(curr_res.path, ignore_errors=True)
    print(snd)

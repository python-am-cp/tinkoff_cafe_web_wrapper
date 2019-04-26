import shutil
import os
from django.core.mail import EmailMessage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tinkoff_web.settings')
from django.core.mail import send_mail
from tinkoff_web import settings
import sendgrid

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
    # sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    # from_email1 = Email("app131467002@heroku.com")
    # subject1 = "Hello World from the SendGrid Python Library!"
    # to_email1 = Email(curr_res.email)
    # content1 = Content("text/plain", "Hello, Email!")
    # mail1 = Mail(from_email1, subject1, to_email1, content1)
    # response = sg.client.mail1.send.post(request_body=mail1.get())
    # print(response.status_code)
    # print(response.body)
    # print(response.headers)
    # msg = EmailMessage(subject=subj, body=mail_content, to=[curr_res.email])
    # msg.send()
    print(curr_res.email)
    snd = send_mail(subj,
              mail_content,
              'app131467002@heroku.com',
              [curr_res.email],
              fail_silently=False,
              auth_password="2qjldf2z8830")
    shutil.rmtree(curr_res.path, ignore_errors=True)
    print(snd)

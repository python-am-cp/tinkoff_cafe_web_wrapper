from django.shortcuts import render
import os
import threading
from django.core.mail import EmailMessage
from. import validation

from django.http import HttpResponse

def directComputationReq(request):
    # validation.valid('helloworld/input_user/')
    f = open("X:/Docs/Pycharm Projects/tinkoff_cafe_web_wrapper/helloworld/"
             "input_user/result.txt", "r")
    while True:
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
        if not line3: break
    f.close()
    em = EmailMessage(subject='Result', body='Ваш результат', to=['atomicmaize@gmail.com'])
    em.attach_file(r"X:/Docs/Pycharm Projects/tinkoff_cafe_web_wrapper/helloworld/"
             "input_user/result.txt")
    em.send()
    return HttpResponse('\n'.join([line1, line2,]))

# validation.valid('helloworld/input_user/')
# def printit():
#     threading.Timer(10.0, printit).start()
#     if not os.listdir('helloworld/input_user/'):
#         print('COOL!')
#     else:
#         print('FUCK!')
#
# printit()

# em = EmailMessage(subject='Test', body='Test', to=['tinkoffweb228@gmail.com'])
# # em.attach_file(r'C:\Users\Артемий\Documents\СПбГУ\hello.txt')
# em.send()


def index_page(request):
    # Get the index template file absolute path.
    # index_file_path = PROJECT_PATH + '/pages/home.html'
    # Return the index file to client.
    return render(request, 'index.html')
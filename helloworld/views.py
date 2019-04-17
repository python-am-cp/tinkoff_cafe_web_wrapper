from django.shortcuts import render
import os
import threading
from django.core.mail import EmailMessage
from. import validation
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time
import shutil


INPUT_DIR = "X:/Docs/Pycharm Projects/tinkoff_cafe_web_wrapper/helloworld/" \
            "input_user/"
doLogic = False


def directComputationReq(request):
    # validation.valid('helloworld/input_user/')
    f = open(INPUT_DIR + "result.txt", "r")
    while True:
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
        if not line3: break
    f.close()
    em = EmailMessage(subject='Result', body='Ваш результат', to=['atomicmaize@gmail.com'])
    em.attach_file(r"X:/Docs/Pycharm Projects/tinkoff_cafe_web_wrapper/helloworld/"
             "input_user/user1/result.txt")
    em.send()
    return HttpResponse('\n'.join([line1, line2]))


def doMainLogic():
    global doLogic
    while True:
        if doLogic:
            validation.valid(INPUT_DIR + 'user1/')
            f = open(INPUT_DIR + 'user1/' + "result.txt", "r")
            while True:
                line1 = f.readline()
                line2 = f.readline()
                line3 = f.readline()
                if not line3: break
            f.close()
            em = EmailMessage(subject='Result', body='Ваш результат', to=['atomicmaize@gmail.com'])
            em.attach_file(r"X:/Docs/Pycharm Projects/tinkoff_cafe_web_wrapper/helloworld/"
                     "input_user/user1/result.txt")
            em.send()
            shutil.rmtree(INPUT_DIR + 'user1/', ignore_errors=True)
            doLogic = False
        time.sleep(5)



def handleUploaded(reqFiles):
    for key, value in reqFiles.items():
        name = reqFiles[key].name
        if not os.path.exists(INPUT_DIR + 'user1/'):
            os.makedirs(INPUT_DIR + 'user1/')
        with open(INPUT_DIR + 'user1/' + name, 'wb+') as destination:
            for chunk in reqFiles[key].chunks():
                destination.write(chunk)



@csrf_exempt
def uploadFiles(request):
    global doLogic
    if request.method == 'POST':
        handleUploaded(request.FILES)
        doLogic = True
        return HttpResponse("Ваши файлы сохранены")
    return HttpResponse("Метод должен быть POST")


# validation.valid('helloworld/input_user/')
# def printit():
#     threading.Timer(10.0, printit).start()
#     if not os.listdir('helloworld/input_user/'):
#         print('COOL!')
#     else:
#         print('FUCK!')
#
# printit()


def index_page(request):
    # Get the index template file absolute path.
    # index_file_path = PROJECT_PATH + '/pages/home.html'
    # Return the index file to client.
    return render(request, 'index.html')
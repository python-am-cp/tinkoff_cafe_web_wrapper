from django.shortcuts import render
import os
import threading
from django.core.mail import EmailMessage
from. import validation
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


INPUT_DIR = "X:/Docs/Pycharm Projects/tinkoff_cafe_web_wrapper/helloworld/" \
            "input_user/"


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
    return HttpResponse('\n'.join([line1, line2]))


def handleUploaded(reqFiles):
    for key, value in reqFiles.items():
        name = reqFiles[key].name
        with open(INPUT_DIR + name, 'wb+') as destination:
            for chunk in reqFiles[key].chunks():
                destination.write(chunk)


@csrf_exempt
def uploadFiles(request):
    if request.method == 'POST':
        handleUploaded(request.FILES)
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
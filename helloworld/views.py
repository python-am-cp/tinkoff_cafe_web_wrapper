from django.shortcuts import render
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time
import shutil
import random
from helloworld.classes import User
from django.core.mail import EmailMessage
from. import validation


INPUT_DIR = "X:/Docs/Pycharm Projects/tinkoff_cafe_web_wrapper/helloworld/" \
            "input_user/"
doLogic = False
curr_user = User()


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
    global curr_user
    while True:
        if doLogic:
            # validation.valid(curr_user.path)
            with open(curr_user.path + 'result.txt', 'w+') as dest:
                    dest.write('134423 \n 4354')
            f = open(curr_user.path + "result.txt", "r")
            while True:
                line1 = f.readline()
                line2 = f.readline()
                line3 = f.readline()
                if not line3: break
            f.close()
            subj = 'Результат' + ' ' + curr_user.resName
            mailContent = 'Здравствуйте,' + ' ' + curr_user.name + ', ' + 'результат ' \
                          'расчетов по метрике составил: ' + '\n\n' + str(line1) + \
                          str(line2) + '\n\n' + 'Описание вашего исследования:' + ' '\
                          + curr_user.resDesc

            msg = EmailMessage(subject=subj, body=mailContent, to=[curr_user.email])
            # em.attach_file(curr_user.path + 'result.txt')
            msg.send()
            shutil.rmtree(curr_user.path, ignore_errors=True)
            doLogic = False
            curr_user = User()
        time.sleep(5)



def handleUserData(data):
    userName = data.get('user-name')
    email = data.get('user-email')
    resName = data.get('research-name')
    resDesc = data.get('research-desc')
    userFolder = email + str(random.randint(10000, 99999)) + '/'
    userPath = INPUT_DIR + userFolder

    ThisUser = User(userName, email, resName, resDesc, userPath)
    return ThisUser


def handleUserFiles(reqFiles, user):
    if not os.path.exists(user.path):
        os.makedirs(user.path)
    for key, value in reqFiles.items():
        fileName = reqFiles[key].name
        with open(user.path + fileName, 'wb+') as destination:
            for chunk in reqFiles[key].chunks():
                destination.write(chunk)


@csrf_exempt
def receiveForm(request):
    global doLogic
    global curr_user
    if request.method == 'POST':
        userData = request.POST.copy()
        curr_user = handleUserData(userData)
        handleUserFiles(request.FILES, curr_user)
        doLogic = True
        return HttpResponse("Ваши файлы сохранены")
    return HttpResponse("Метод должен быть POST")


def index_page(request):
    return render(request, 'index.html')
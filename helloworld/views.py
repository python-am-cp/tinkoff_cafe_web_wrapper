from django.shortcuts import render
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time
import shutil
import random
from helloworld.classes import Research
from django.core.mail import EmailMessage
import queue
import threading
from tinkoff_web import settings


taskQueue = queue.Queue(maxsize=6)


# def handle_queue():
#     global taskQueue
#     while True:
#         if not taskQueue.empty():
#             current = taskQueue.get()
#             calculate_send_clear(current)
#         time.sleep(5)


@csrf_exempt
def receive_form(request):
    global taskQueue
    print("adbgsbfs")
    if request.method == 'POST':
        print("12345443")
        if taskQueue.full():
            return HttpResponse("К сожалению очередь заполнена, отправьте позже")
        user_data = request.POST.copy()
        curr_research = handle_user_data(user_data)
        handle_user_files(request.FILES, curr_research)
        taskQueue.put(curr_research)
        return HttpResponse("Ваши файлы сохранены")
    return HttpResponse("Метод должен быть POST")


def handle_user_data(data):
    user_name = data.get('user-name')
    email = data.get('user-email')
    res_name = data.get('research-name')
    res_desc = data.get('research-desc')
    user_folder = email + str(random.randint(10000, 99999)) + '/'
    user_path = settings.INPUT_DIR + user_folder

    this_research = Research(user_name, email, res_name, res_desc, user_path)
    print("Разобрались с данными")
    return this_research


def handle_user_files(req_files, current_res):
    if not os.path.exists(current_res.path):
        os.makedirs(current_res.path)
    for key, value in req_files.items():
        file_name = req_files[key].name
        with open(current_res.path + file_name, 'wb+') as destination:
            for chunk in req_files[key].chunks():
                destination.write(chunk)
    print("Разобрались с файлами")



# def calculate_send_clear(curr_res):
#     cross_validation.validate(curr_res.path)
#     # with open(curr_res.path + 'result.txt', 'w+') as dest:
#     #         dest.write('134423 \n 435423')
#     f = open(curr_res.path + "result.txt", "r")
#     while True:
#         line1 = f.readline()
#         line2 = f.readline()
#         line3 = f.readline()
#         if not line3:
#             break
#     f.close()
#     subj = 'Результат' + ' ' + curr_res.resName
#     mail_content = 'Здравствуйте,' + ' ' + curr_res.name + ', ' + 'результат ' \
#                    'расчетов по метрике составил: ' + '\n\n' + str(line1) + \
#                    str(line2) + '\n\n' + 'Описание вашего исследования:' + ' ' \
#                    + curr_res.resDesc
#
#     msg = EmailMessage(subject=subj, body=mail_content, to=[curr_res.email])
#     msg.send()
#     shutil.rmtree(curr_res.path, ignore_errors=True)


def index_page(request):
    return render(request, 'index.html')


# logicThread = threading.Thread(target=handle_queue, args=[])
# logicThread.setDaemon(False)
# logicThread.start()

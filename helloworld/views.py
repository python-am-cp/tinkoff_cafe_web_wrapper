from django.shortcuts import render
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random
from helloworld.classes import Research
from tinkoff_web import settings
from rq import Queue
from worker import conn
from helloworld.task import calculate_send_clear


task_q = Queue(connection=conn)


@csrf_exempt
def receive_form(request):
    if request.method == 'POST':
        user_data = request.POST.copy()
        curr_research = handle_user_data(user_data)
        handle_user_files(request.FILES, curr_research)
        result = task_q.enqueue(calculate_send_clear, curr_research)
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


def index_page(request):
    return render(request, 'index.html')

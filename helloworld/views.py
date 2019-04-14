from django.shortcuts import render
import os
import threading
from django.core.mail import EmailMessage
from. import validation

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
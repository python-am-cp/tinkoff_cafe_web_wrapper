import sys
import time
import shutil
from django.core.mail import EmailMessage

from views import taskQueue
from daemon import Daemon
import cross_validation


class TaskDaemon(Daemon):
    def run(self):
        while True:
            if not taskQueue.empty():
                current = taskQueue.get()
                calculate_send_clear(current)
            time.sleep(5)


def calculate_send_clear(curr_res):
    cross_validation.validate(curr_res.path)
    # with open(curr_res.path + 'result.txt', 'w+') as dest:
    #         dest.write('134423 \n 435423')
    f = open(curr_res.path + "result.txt", "r")
    while True:
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
        if not line3:
            break
    f.close()
    subj = 'Результат' + ' ' + curr_res.resName
    mail_content = 'Здравствуйте,' + ' ' + curr_res.name + ', ' + 'результат ' \
                   'расчетов по метрике составил: ' + '\n\n' + str(line1) + \
                   str(line2) + '\n\n' + 'Описание вашего исследования:' + ' ' \
                   + curr_res.resDesc

    msg = EmailMessage(subject=subj, body=mail_content, to=[curr_res.email])
    msg.send()
    shutil.rmtree(curr_res.path, ignore_errors=True)


if __name__ == "__main__":
    daemon = TaskDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)

from utils import *
from corr_del_hw import *
from os.path import exists


def main():
    while True:
        step = input(("Введите действие: "))
        if step == 'q':
            break
        elif step == 'w':
            path = 'phone.csv'
            flag = exists(path)
            if not flag:
                creating()
                record_info()
            else:
                record_info()

        elif step == 'r':
            view()
        elif step == 'c':
            correction()
        elif step == 'd':
            removing()


main()









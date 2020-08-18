# def show_process(nums):
#     a = "_"*20
#     print(a)
#     for i in range(nums):
#         for j in range(len(a)):
#             if i / nums > 0.05*j:
#                 print(a[j].replace("_", "$"))
#
# show_process(30)

import sys, time, threading


def process_function():
    n = 20
    for i in range(n):
        time.sleep(1)
        sys.stdout.write(r'loading... process '+str[i]+'/'+str(n)+' '+'{:.2f}'.format(i/n*100)+'%')
        sys.stdout.flush()
    sys.stdout.write(r'loading... finished             \n')


def animated_loading():
    chars = ['|', '/', '-', '\\']
    for char in chars:
        sys.stdout.write(r'loading...'+char)
        time.sleep(1)
        sys.stdout.flush()


process = threading.Thread(name='process', target=process_function)
process.start()

while process.is_alive():
    animated_loading()
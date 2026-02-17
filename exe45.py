from time import sleep
for i in range(10,-1,-1):
    print('\033[1;31mfaltam {} segundos pro ano novo!\033[m'.format(i))
    sleep(1)
    if i == 0:
        print('\033[1;31mANO NOVO!!\033[m')
        break
import os
import time

s = 600
while True:
    time.sleep(1)
    os.system('clear')  # ← windows では 'cls'
    if s > 0:
        print(f'再開まで {s} 秒')
    elif s % 2 == 0:
        print(' 講義を再開します ')
    else:
        print('>講義を再開します<')
    s -= 1
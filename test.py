import os
import psutil

print("Hello Student PY")
print('Укажи какую операцию выполнить')
print("1 - Тек. директории\n 2 - ") 
answer = int(input())

if answer == 1:
    print(os.listdir())
elif answer == 2:
    print(psutil.cpu_times())
elif answer == 3:
    pass
elif condition:
    pass                
else:
    print("Введено некорректное число")

import os, shutil


if not os.path.exists('Задание 2'):
    os.mkdir("Задание 2")
    file = open('2task.py', 'w+')
    file.close()
    shutil.move('2task.py', 'Задание 2/2task.py')
if not os.path.exists('Задание 5'):
    os.mkdir("Задание 5")
    file = open('5task.py', 'w+')
    file.close()
    shutil.move('5task.py', 'Задание 5/5task.py')
if not os.path.exists('Задание 6'):
    os.mkdir("Задание 6")
    file = open('6task.py', 'w+')
    file.close()
    shutil.move('6task.py', 'Задание 6/6task.py')
if not os.path.exists('Задание 8'):
    os.mkdir("Задание 8")
    file = open('8task.py', 'w+')
    file.close()
    shutil.move('8task.py', 'Задание 8/8task.py')
if not os.path.exists('Задание 12'):
    os.mkdir("Задание 12")
    file = open('12task.py', 'w+')
    file.close()
    shutil.move('12task.py', 'Задание 12/12task.py')
if not os.path.exists('Задание 14'):
    os.mkdir("Задание 14")
    file = open('14task.py', 'w+')
    file.close()
    shutil.move('14task.py', 'Задание 14/14task.py')
if not os.path.exists('Задание 15'):
    os.mkdir("Задание 15")
    file = open('15task.py', 'w+')
    file.close()
    shutil.move('15task.py', 'Задание 15/15task.py')
if not os.path.exists('Задание 16'):
    os.mkdir("Задание 16")
    file = open('16task.py', 'w+')
    file.close()
    shutil.move('16task.py', 'Задание 16/16task.py')

file = open('17task.py', 'w+')
file.close()
file = open('24task.py', 'w+')
file.close()
shutil.move('17task.py', 'Задание 17/17task.py')
shutil.move('24task.py', 'Задание 24/24task.py')
if not os.path.exists('Задание 19-21'):
    os.mkdir("Задание 19-21")
    file = open('19-21task.py', 'w+')
    file.close()
    shutil.move('19-21task.py', 'Задание 19-21/19-21task.py')
if not os.path.exists('Задание 23'):
    os.mkdir("Задание 23")
    file = open('23task.py', 'w+')
    file.close()
    shutil.move('23task.py', 'Задание 23/23task.py')
if not os.path.exists('Задание 25'):
    os.mkdir("Задание 25")
    file = open('25task.py', 'w+')
    file.close()
    shutil.move('25task.py', 'Задание 25/25task.py')

print('DONE')
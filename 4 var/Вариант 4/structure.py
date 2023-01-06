import os, shutil


for i in range(2, 27):
    if i == 19 or i == 20 or i == 21:
        if not os.path.exists('Задание 19-21'):
            os.mkdir("Задание 19-21")
            file = open('19-21task.py', 'w+')
            file.close()
            shutil.move('19-21task.py', 'Задание 19-21/19-21task.py')
    elif not os.path.exists(f'Задание {i}'):
        os.mkdir(f'Задание {i}')
        file = open(f'{i}task.py', 'w+')
        file.close()
        shutil.move(f'{i}task.py', f'Задание {i}/{i}task.py')

print('DONE')
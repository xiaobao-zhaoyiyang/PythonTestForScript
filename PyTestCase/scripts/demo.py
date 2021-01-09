from tempfile import NamedTemporaryFile
import os
f = None


def demo():
    file_path = './temp'
    if not os.path.isdir(file_path):
        os.makedirs(file_path)
    list_dir = os.listdir(file_path)
    if len(list_dir) != 0:
        for dir_temp in list_dir:
            os.remove(file_path + '/' + dir_temp)
    global f
    f = NamedTemporaryFile(mode='w+', dir=f'{file_path}/', delete=False)
    f.write('my name is file\n')
    f.write('my age is 22\n')
    f.seek(0)
    # print(f.read())


def read_data():
    print(f.read())


if __name__ == '__main__':
    demo()
    read_data()
import os.path
import shutil
from google_images_download import google_images_download

directory_list = [
    'custom_dataset/train/',
    'custom_dataset/test/'
]

for i in directory_list:
    if not os.path.isdir(i):
        os.makedirs(i)


def dataset_split(keyword, train_count):
    for i in directory_list:
        if not os.path.isdir(i + '/' + keyword):
            os.makedirs(i + '/' + keyword)

    cnt = 0
    for j in os.listdir(keyword):
        if cnt < train_count:
            print(f'[Train Dataset] {j}')
            shutil.move(keyword + '/' + j, directory_list[0] + keyword + '/' + j)
        else:
            print(f'[Test Dataset] {j}')
            shutil.move(keyword + '/' + j, directory_list[1] + keyword + '/' + j)
    shutil.rmtree(keyword)


def google_image_crawling(keyword):
    arguments = {'keywords': keyword,
                 'format' : 'png',
                 'limit': 40,
                 'print_urls': True,
                 'output_directory': './'}

    paths = google_images_download.googleimagesdownload().download(arguments)
    print(paths)
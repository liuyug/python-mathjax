#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
import site
import os.path
import urllib.request
import zipfile


def progress_bar(count, total, bar_len=60, suffix=''):
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()


def download(src, dest, callback=None, block=8192):
    def _download(response, dest_file, dest_size):
        if callback:
            callback(0, dest_size)
        count = 0
        while True:
            data = response.read(block)
            if not data:
                break
            count += len(data)
            dest_file.write(data)
            if callback:
                callback(count, dest_size)

    with open(dest, 'wb') as dest_file:
        with urllib.request.urlopen(src) as response:
            s_size = response.getheader('Content-Length')
            if not s_size:
                return
            dest_size = int(response.getheader('Content-Length'))
            _download(response, dest_file, dest_size)
    return dest_file


def unzip(src, dest=None, callback=None):
    zip_file = zipfile.ZipFile(src)
    total = sum(f.file_size for f in zip_file.infolist())
    count = 0

    for f in zip_file.infolist():
        count += f.file_size
        if callback:
            callback(count, total)
        zip_file.extract(f, dest)


def installMathJax():
    mathjax_url = 'https://github.com/mathjax/MathJax/archive/master.zip'
    package_paths = site.getsitepackages()
    package_paths.append(site.getusersitepackages())
    for path in package_paths:
        if os.path.exists(os.path.join(path, 'pymathjax', '__init__.py')):
            break
    install_path = os.path.join(path, 'pymathjax')
    mathjax_zip = os.path.join(install_path, 'MathJax-master.zip')
    print("Install MathJax")
    print('download to "%s"' % mathjax_zip)
    count = 1
    while True:
        dest = download(mathjax_url, mathjax_zip, progress_bar)
        if dest:
            break
        if count > 2:
            print('Failed to install. Please install later...')
            return
        count += 1
    print('\ncomplete!')
    print('uncompress')
    unzip(mathjax_zip, dest=install_path, callback=progress_bar)
    print('\ncomplete!')


def getMathJax():
    return os.path.join(
        os.path.dirname(__file__),
        'MathJax-master'
    )

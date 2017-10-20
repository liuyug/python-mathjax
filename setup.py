#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from setuptools import setup
from setuptools.command.install import install

from pymathjax import installMathJax


class install_mathjax(install):
    def run(self):
        install.run(self)
        installMathJax()


setup(
    name='pymathjax',
    version='0.1.0',
    author='Yugang LIU',
    author_email='liuyug@gmail.com',
    url='https://github.com/liuyug/pymathjax.git',
    license='GPLv3',
    description='install MathJax on local',
    packages=['pymathjax'],
    cmdclass={
        'install': install_mathjax,
    }
)

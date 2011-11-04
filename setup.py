import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "djangorestframework_jsonp",
    version = "0.1",
    author = "Proteus Technologies",
    author_email = "devs@proteus-tech.com",
    description = ("JSONP Response Renderer, extension for Django REST Framework Library"),
    long_description = read('README.markdown'),
    keywords = "djangorestframework jsonp",
    classifiers = [
        "Development Status :: 1 - Alpha",
        "Intended Audience :: DevOps",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Boost Software License - Version 1.0 - August 17th, 2003",
    ],
    packages = ['djangorestframework_jsonp'],
    install_requires = ['django','djangorestframework', ],

)
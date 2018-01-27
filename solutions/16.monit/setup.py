
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'monit',
    'author': 'Zed A. Shaw',
    'url': 'http://github.com/zedshaw/lpthw-study-projects',
    'download_url': 'http://github.com/zedshaw/lpthw-study-projects',
    'author_email': 'zedshaw@zedshaw.com',
     'version': '1.0',
     'scripts': [],
     'install_requires': [],
     'packages': ['monit'],
     'name': 'lpthwsp-monit'
}

setup(**config)

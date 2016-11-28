import os
import sys
import platform
from setuptools import setup, find_packages
from os.path import join, dirname

# copied from electrum project
data_files = []
if platform.system() == 'Linux':
    usr_share = os.path.join(sys.prefix, 'share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['stripbar.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['stripbar.xpm']),
    ]


setup(
    name = 'stripbar',
    scripts = ['stripbar'],
    version = '0.0.1',
    license = 'MIT License',
    description = 'Simple LED widget that displays a color per dot',
    author = 'Huan Truong',
    author_email = 'htruong@tnhh.net',
    url = 'https://github.com/htruong/stripbar',
    download_url  ='https://github.com/limpbrains/stripbar/tarball/0.0.1',
    keywords = ['AnyBar', 'stripbar', 'taskbar', 'indicator'],
    packages = find_packages(),
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
    ],
    package_data = {'stripbar_icons' : ['*.png']},
    data_files = data_files,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires = [
        # 'gi'
    ],
)

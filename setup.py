from setuptools import setup

import os.path

requirements_dev_filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'requirements-dev.txt')

with open(requirements_dev_filename) as fd:
    tests_require = [i.strip() for i in fd.readlines()]

long_description_filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'README.md')

with open(long_description_filename) as fd:
    long_description = fd.read()

setup(
    name='yacgol',
    version='0.5.0',
    description="A pure Python implementation of Conway's Game of Life using Tkinter.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mschwager/yacgol',
    py_modules=['yacgol'],
    license='GPLv3',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    tests_require=tests_require,
    python_requires='>=3.0',
    entry_points={
        'console_scripts': [
            'yacgol = yacgol:main',
        ],
    },
)

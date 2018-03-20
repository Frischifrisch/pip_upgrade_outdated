# -*- coding: utf-8 -*-

from setuptools import setup
import re

## from https://gehrcke.de/2014/02/distributing-a-python-command-line-application/
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('pip_upgrade_outdated/upgrade_pip_packages.py').read(),
    re.M
    ).group(1)

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(name='pip_upgrade_outdated',
      version=version,
      description='Command-line tool to updated outdated python packages',
      url='http://github.com/defjaf/pip_upgrade_outdated',
      author='Andrew H. Jaffe',
      author_email='a.h.jaffe@gmail.com',
      license='MIT', ### sewe https://choosealicense.com/licenses/mit/#
      packages=['pip_upgrade_outdated'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',

        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Archiving :: Packaging',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
      ],
      keywords='pip',
            ## zip_safe=False,   ### probably true?
      entry_points = {
        'console_scripts': ['pip_upgrade_outdated=pip_upgrade_outdated.upgrade_pip_packages:main'],
    }
)

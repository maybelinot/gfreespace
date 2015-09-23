#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eduard Trott
# @Date:   2015-09-07 14:59:52
# @Email:  etrott@redhat.com
# @Last modified by:   etrott
# @Last Modified time: 2015-09-23 11:08:30

from setuptools import setup

VERSION_FILE = "gfreespace/_version.py"
VERSION_EXEC = ''.join(open(VERSION_FILE).readlines())
__version__ = ''
exec(VERSION_EXEC)  # update __version__
if not __version__:
    raise RuntimeError("Unable to find version string in %s." % VERSION_FILE)

# acceptable version schema: major.minor[.patch][-sub[ab]]
__pkg__ = 'gfreespace'
__pkgdir__ = {'gfreespace': 'gfreespace'}
__pkgs__ = ['gfreespace', ]
__provides__ = ['gfreespace']
__desc__ = 'Get information about rooms state in Google Calendar.'
__scripts__ = ['bin/gfreespace']
__irequires__ = [
    # CORE DEPENDENCIES
    'functioncache==0.92',
    'argparse==1.3.0',
    'pyyaml==3.11',
    'gdata==2.0.18',
    'google-api-python-client==1.4.1',
    'oauth2client==1.4.12',
    'python-dateutil==2.4.2'
]
__xrequires__ = {
    'tests': [
        'pytest==2.7.2',
        'instructions',
        'pytest-pep8==1.0.6',  # run with `py.test --pep8 ...`
    ],
    # 'docs': ['sphinx==1.3.1', ],
    # 'github': ['PyGithub==1.25.2', ],
    # 'invoke': ['invoke==0.10.1', ],
}

pip_src = 'https://pypi.python.org/packages/src'
__deplinks__ = []

# README is in the parent directory
readme_pth = 'README.rst'
with open(readme_pth) as _file:
    readme = _file.read()

github = 'https://github.com/etrott/gfreespace'
download_url = '%s/archive/master.zip' % github

default_setup = dict(
    url=github,
    license='GPLv3',
    author='Eduard Trott',
    author_email='etrott@redhat.com',
    maintainer='Chris Ward',
    maintainer_email='cward@redhat.com',
    download_url=download_url,
    long_description=readme,
    data_files=[],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business',
        'Topic :: Utilities',
    ],
    keywords=['information'],
    dependency_links=__deplinks__,
    description=__desc__,
    install_requires=__irequires__,
    extras_require=__xrequires__,
    name=__pkg__,
    package_dir=__pkgdir__,
    packages=__pkgs__,
    provides=__provides__,
    scripts=__scripts__,
    version=__version__,
    zip_safe=False,  # we reference __file__; see [1]
)

setup(**default_setup)

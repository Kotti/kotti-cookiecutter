# !/usr/bin/env python

from distutils.core import setup


tests_require = [
    'cookiecutter>=1.4.0',
    'pytest',
    'pytest-cookies',
    'tox',
    'pipenv',
]

docs_require = [
    'Sphinx',
    'sphinx_rtd_theme',
]

setup(
    name='kotti-cookiecutter',
    packages=[],
    version='0.0.1',
    description='Cookiecutter template for Kotti addons',
    author='Kotti developers',
    license='BSD-derived (http://www.repoze.org/LICENSE.txt)',
    author_email='kotti@googlegroups.com',
    url='https://github.com/Kotti/kotti-cookiecutter',
    keywords=['cookiecutter', 'template', 'package', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    extras_require={
        'docs': docs_require,
        'tests': tests_require,
        },
)

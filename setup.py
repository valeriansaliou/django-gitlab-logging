# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='django-gitlab-logging',
    version='0.2.2',
    author=u'Valérian Saliou',
    author_email='valerian@valeriansaliou.name',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/valeriansaliou/django-gitlab-logging',
    license='MIT - http://opensource.org/licenses/mit-license.php',
    description='A logging handler that opens GitLab issues on server error.',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

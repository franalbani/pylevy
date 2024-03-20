#!/usr/bin/env python

from distutils.core import setup

setup(name='PyLevy',
      version='1.1',
      author='Paul Harrison, Jose Miotto',
      url='https://github.com/josemiotto/pylevy',
      license='GPL',
      description='A package for calculating and fitting Levy stable distributions.',
      long_description='Read levy/__init__.py',
      packages=['levy'],
      package_data={'levy': ['cdf.npz', 'pdf.npz', 'lower_limit.npz', 'upper_limit.npz']},
      options={'sdist': {'force_manifest': True}},
     )

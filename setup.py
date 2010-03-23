from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='emencia.django.stylish',
      version=version,
      description="Apply style attributes to HTML markups",      
      long_description=open('README.rst').read() + '\n' +
                       open(os.path.join('docs', 'HISTORY.txt')).read(),
      keywords='html, markup, style',
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: BSD License',
          ],

      author='Julien Fache',
      author_email='fantomas42@gmail.com',
      url='http://emencia.fr',

      license='BSD License',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['emencia', 'emencia.django'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

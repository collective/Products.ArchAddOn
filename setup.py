from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='Products.ArchAddOn',
      version=version,
      description="Straightforward toolbox of field types, widgets, and validators for Archetypes.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Joel Burton',
      author_email='joel@joelburton.com',
      url='https://svn.plone.org/svn/collective/Products.ArchAddOn',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

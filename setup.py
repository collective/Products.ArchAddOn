from setuptools import setup, find_packages
import os

#versionfile = open(os.path.join('Products', 'ArchAddOn', 'version.txt'))
version = '1.7'
version = versionfile.read().strip()
versionfile.close()

readmefile = open('README.rst')
readme = readmefile.read().strip()
readmefile.close()

historyfile = open(os.path.join('docs', 'HISTORY.txt'))
history = historyfile.read().strip()
historyfile.close()

long_description = readme + "\n\n" + history
description = "Straightforward toolbox of field types, widgets, and"
description += " validators for Archetypes."

setup(name='Products.ArchAddOn',
      version=version,
      description=description,
      long_description=long_description,
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='archetypes plone widget',
      author='Joel Burton',
      author_email='joel@joelburton.com',
      maintainer='Alex Clark',
      maintainer_email='aclark@aclark.net',
      url='https://github.com/collective/Products.ArchAddOn/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone>=4.0dev',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

from setuptools import setup, find_packages

version = '1.0b2'

setup(name='plone.app.contenttypes',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
      ],
      keywords='plone content types dexterity',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='https://github.com/plone/plone.app.contenttypes',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',
          'plone.app.collection>=2.0a1',
          'plone.app.dexterity',
          'plone.app.relationfield',
          'plone.namedfile [blobs]',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'lxml',
              'plone.app.testing',
              'robotsuite',
              'robotframework-selenium2library',
          ],
          'migrate_atct': [
              'Products.contentmigration',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

from setuptools import setup, find_packages
import sys, os

version = '0.3.0'

setup(name='arke',
      version=version,
      description="basic server agent for collecting stats",
      #long_description="""TODO""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Dominic LoBue',
      author_email='dominic@geodelic.com',
      url='',
      license='proprietary',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      scripts=['bin/arke'],
      data_files=[('/etc/init', ['init_scripts/arke.conf']),
                 ],
      install_requires=[
          "timer2>0.1.0",
          "giblets>=0.2.1",
          "simpledaemon>=1.0.1",
          "pymongo>=1.10",
          "gevent>=0.13.6",
          "psutil>=0.2.1",
          "paramiko",
          "boto>=2.0rc1",
          "psycopg2>=2.4.2",
      ],
      entry_points="""
      # -*- Entry points: -*-
      [arke_plugins]
      latency = arke.plugins.latency
      system = arke.plugins.system
      ssh_hello = arke.plugins.ssh_hello
      mongodb = arke.plugins.mongodb
      postgres_repl = arke.plugins.postgres_repl
      """,
      )

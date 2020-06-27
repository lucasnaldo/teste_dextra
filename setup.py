from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '0.1'
    
setup(name='dextra',
      version=version,
      install_requires=requirements,
      description='Python Distribution Utilities',
      author='Lucas Naldo Falotico',
      author_email='lucas_naldo@hotmail.com',
      maintainer='Lucas Naldo Falotico',
      maintainer_email='lucas_naldo@hotmail.com',
      url='www.python.org',
      packages=['dextra']
     )
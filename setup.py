from setuptools import setup, find_packages
 
setup(name='pig-latin',
      version='0.1.4',
      url='http://github.com/cjanis/python-pig-latin',
      license='Unlicense',
      author='Craig Janis',
      author_email='cjanis@gmail.com',
      description='Translate text into Pig Latin using Python',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
from setuptools import setup
from shutil import copyfile
import os

# copyfile(os.path.join(os.path.dirname(__file__), 'test.txt'), '/home/odoo/.config/odoo/test.txt')

setup(name='e3_test',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['e3_test'],
      zip_safe=False)


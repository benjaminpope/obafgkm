#!/usr/bin/env python
import sys
import os
from setuptools import setup

if "publish" in sys.argv[-1]:
    os.system("python setup.py sdist")
    os.system("twine upload dist/*")
    os.system("rm -rf dist/*")
    sys.exit()

# Load the __version__ variable without importing the package
exec(open('coco/version.py').read())

# Command-line tools
entry_points = {'console_scripts': [
    'obafgkm = obafgkm.obafgkm:obafgkm'
]}

setup(name='obafgkm',
      version=__version__,
      description="Convert spectral type to stellar parameters",
      long_description="",
      author='Benjamin Pope',
      author_email='b.pope@sydney.edu.au',
      license='GPLv3',
      url='https://github.com/benjaminpope/obafgkm',
      packages=['obafgkm'],
      install_requires=['numpy>=1.8',
                        ],
      entry_points=entry_points,
      include_package_data=True,
      classifiers=[
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Intended Audience :: Science/Research",
          "Topic :: Scientific/Engineering :: Astronomy",
          ],
      )

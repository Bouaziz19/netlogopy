from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.14'
DESCRIPTION = 'netlogopy : Usage netlogo by python'
LONG_DESCRIPTION = 'netlogopy : Usage netlogo by python () '

# Setting up
setup(
    name="netlogopy",
    version=VERSION,
    author="BOUAZIZ (BOUAZIZ NOURDDINE)",
    author_email="<nourddine.bouaziz.dz@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        ('netlogo', ['netlogopy/netlogopy.nlogo']),
    ],
    install_requires=['nl4py'],
    keywords=['python', 'netlogo', 'simulation', 'multi agent'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

# python setup.py bdist_wheel
# pip install dist/netlogopy-0.0.1-py3-none-any
# twine upload dist/*
# __token__


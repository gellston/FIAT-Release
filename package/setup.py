from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='fiat-tool',
version='0.7.0.10',
description='Fast Image Annotation Tool, Free image labeling tool for deep learning',
author='FIAT Development Team',
author_email='fiattool2022@gmail.com',
long_description=long_description,
long_description_content_type="text/markdown",
url='https://github.com/gellston/FIAT-Release',
license='MIT',
python_requires='>=3.6',
packages=find_packages(include=['fiat_tool', 'fiat_tool.*']),
install_requires=['numpy',
                  'opencv-python',
                  'torch-utils',
                  'torch'],
classifiers=[
  'Topic :: Software Development :: Libraries',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.6',
],
)
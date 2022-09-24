from setuptools import find_packages, setup

setup(
    name='kapyr',
    packages=['kapyr'],
    version='1.0.0',
    description='Library to make satellital images',
    author='No pixel, no fun',
    license='MIT',
    install_requires = ['numpy', 'opencv-python', 'rasterio'],
    include_package_data=True
)
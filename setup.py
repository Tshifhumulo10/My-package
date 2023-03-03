from setuptools import setup, find_packages

setup(
    name="Mypackage",
    version= '0.1',
    package= find_packages(exclude=['test']),
    license="MIT",
    description="Tshifhumulo Python  package",
    long_description=open('readme.md').read(),
    install_requires=['Numpy'],
    url="https://github.com/Tshifhumulo10/Mypackage",
    author= "Tshifhumulo",
    author_email="mapasatshifhumulo@gmail.com"
)
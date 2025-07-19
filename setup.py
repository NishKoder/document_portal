from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="DOCUMENT_PORTAL",
    version="0.1",
    author="nishkoder",
    packages=find_packages(),
    install_requires = requirements,
)
from setuptools import find_packages, setup

with open("README.md",'r') as f:
    long_description = f.read()

setup(
    name = 'yogi_formula',
    packages = find_packages(include=['yogi_formula']),
    version = '0.1.2',
    description = 'My first Python library',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = 'Yogesh Nile',
    install_requires = [],
    license = 'MIT',
    url = 'https://github.com/yogeshnile/fin-formula',
    author_email = 'yogeshnile.work4u@gmail.com',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
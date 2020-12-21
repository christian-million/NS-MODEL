# This is a setup file for the package handler to install

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ns_model",
    version="0.0.1",
    author="Christian Million",
    author_email="christianmillion93@gmail.com",
    description="A natural selection simulator based on: https://www.youtube.com/watch?v=0ZGbIKd0XrM&vl=en",
    include_package_data=True,
    package_data={'ns_model': ['defaults.json']},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/christian-million/NS-MODEL",
    packages=setuptools.find_packages()
)

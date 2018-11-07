from setuptools import setup

setup(
    name="cba_signnow",
    version="0.1.0",
    description="Forked Python SDK for the SignNow system",
    long_description=open("README.rst").read(),
    url="",
    author="SignNow, Joshua Learn",
    author_email="joshuaryanlearn@gmail.com",
    license="MIT",
    packages=["cba_signnow"],
    install_requires=["unirest"],
    zip_safe=False,
)

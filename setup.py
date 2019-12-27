from setuptools import setup

setup(name='signnow_python_sdk',
    version="0.2.0",
    description='Python SDK for the SignNow system',
    long_description = open("README.rst").read(),
    url = '',
    author = 'SignNow',
    author_email='api@signnow.com',
    license = 'MIT',
    packages=['signnow_python_sdk'],
    install_requires=[
        'requests',
    ],
    zip_safe=False)

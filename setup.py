from setuptools import setup

setup(name='signnow_python_sdk',
    version="2.0",
    description='Python SDK for the SignNow system',
    long_description = open("README.rst").read(),
    url = 'https://github.com/signnow/SNPythonSDK',
    download_url = 'https://github.com/signnow/SNPythonSDK/archive/refs/tags/2.0.tar.gz',
    author = 'SignNow',
    author_email='api@signnow.com',
    license = 'Apache 2.0',
    packages=['signnow_python_sdk'],
    install_requires=[
        'requests',
    ],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)

from setuptools import setup, find_packages

setup(
    name="ebics_api_client",
    version="1.0.9",
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description="EBICS API Client",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Andrew Svirin",
    author_email="andrey.svirin@ukr.net",
    url="https://github.com/andrew-svirin/ebics-api-client-python",
    install_requires = requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="web3storagepy",
    version="0.0.1",
    description="An IPFS web3.storage unofficial library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tahaafarooq/web3.storage",
    download_url="",
    author="Tahaa Farooq",
    author_email="tahacodez@gmail.com",
    license="MIT",
    packages=["web3storagepy"],
    keywords=[
        "web3 storage",
        "web3" "web3 storage api" "IPFS" "web3 api" "IPFS api",
        "python-tanzania",
    ],
    install_requires=["libmagic", "python-magic-bin==0.4.14", "requests"],
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
)

# web3storagepy
This is IPFS web3.storage unofficial library written in python. I have made it simple and easier to integrate with web3.storage API using this masterpiece of codes.

[![Releases](https://badgen.net/github/releases/tahaafarooq/web3storagepy)](https://github.com/tahaafarooq/web3storagepy/releases)
[![Downloads](https://static.pepy.tech/badge/web3storagepy)](https://pepy.tech/project/web3storagepy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation
You can either install it from git, or using pip.

```shell
~$ git clone https://github.com/tahaafarooq/web3storagepy
~$ cd web3storagepy
~$ pip3 install -r requirements.txt 
~$ python3 setup.py install
```

```shell
~$ pip3 install web3storagepy
```

## Usage

To upload a file to the IPFS web3 storage API we will do the following;

```python
>>> import web3storagepy
>> > w3s = web3storagepy
>> > upload = w3s.upload(file="XXXXXX", token="XXXXXXX")
>> > upload
{'STATUS_CODE': 200, 'RESPONSE': '{"cid":"XXXXXXXXXXXXXXXX","carCid":"XXXXXXXXXXXX"}'}
```

Using the CID you are provided with you can decide to check the status of the uploaded file with;

```python
>> > import web3storagepy
>> > w3s = web3storagepy
>> > status = w3s.status(cid="XXXXXXXX", token="XXXXXXXXXXXX")
>> > status
{'RESPONSE': '{xxx:xxx}'}
```

You can retrieve all your uploaded files with;

```python
>> > import web3storagepy
>> > w3s = web3storagepy
>> > all_files = w3s.user_uploads(token="XXXXXXXXX")
>> > all_files
'XXXXXXXXXXXXXXXXX'
```

You can access your uploaded file by providing only the CID as follows;

```python
>> > import web3storagepy
>> > w3s = web3storagepy
>> > get_file = w3s.get_upload(cid="XXXXXXXXX")
>> > get_file
'https://XXXXXXXXX.ipfs.w3s.link'
```

## Give it star
If you happen to find this repository useful or helpful , give it a star!

## Issues

Are you facing any issue with usage of the package, just raise an issue and I will look into fixing it as soon as possible

## Contributions

If there is anything yould would like to add warmly welcome, Just fork it

## Disclaimers

This is not an official package, therefore I'm not responsible for any misinformation or misuse of the package of any kind !!!


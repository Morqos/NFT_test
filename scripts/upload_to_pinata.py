import requests
import os
from pathlib import Path
import json


PINATA_BASE_URL = 'https://api.pinata.cloud/'
endpoint = 'pinning/pinFileToIPFS'

headers = {'pinata_api_key': os.getenv('PINATA_API_KEY'),
            'pinata_secret_api_key': os.getenv('PINATA_API_SECRET')}


jsonToPrint = {}

for i in range(1, 101):
  filepath = '100imgs/' + 'img-' + str(i) + '.png'
  filename = 'img-' + str(i) + '.png'
  with Path(filepath).open("rb") as fp:
    image_binary = fp.read()
    response = requests.post(PINATA_BASE_URL + endpoint,
                              files={"file": (filename, image_binary)},
                              headers=headers)
    print(response.json())
    ipfs_hash = response.json()["IpfsHash"]
    image_uri = "https://ipfs.io/ipfs/{}?filename={}".format(ipfs_hash, filename)
    print(image_uri)
    jsonToPrint[filename] = image_uri


with open("metadata/nameToImageUri.json", 'w') as outfile:
  json.dump(jsonToPrint, outfile, indent=2)
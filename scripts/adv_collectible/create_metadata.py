from brownie import advCollectible, network
from metadata import sample_metadata, nameToImageUri
from pathlib import Path
import os
import requests
import json


PINATA_BASE_URL = 'https://api.pinata.cloud/'
endpoint = 'pinning/pinFileToIPFS'

headers = {'pinata_api_key': os.getenv('PINATA_API_KEY'),
            'pinata_secret_api_key': os.getenv('PINATA_API_SECRET')}


def main():
  adv_collectible = advCollectible[len(advCollectible) - 1]
  write_metadata(adv_collectible);


def write_metadata(nft_contract):
  collectible_metadata = sample_metadata.metadata_template
  image_uris = nameToImageUri.image_uris
  dict_URIs = {}
  for i in range(1, 101):
    name_single_metadata = 'mtdtTest-' + str(i) + ".json"
    metadata_file_name = (
      "./metadata/{}/".format(network.show_active()) + name_single_metadata
    )

    collectible_metadata["image"] = image_uris['img-' + str(i) + '.png']
    collectible_metadata["name"] = 'CHAD Ice Cream ' + str(i)
    collectible_metadata["description"] = "An Incredible Gelato"

    with open(metadata_file_name, "w") as file:
      json.dump(collectible_metadata, file, indent=2)

    tmpURI = ""
    if os.getenv("UPLOAD_IPFS") == "true":
      tmpURI = upload_to_ipfs(metadata_file_name)
    
    dict_URIs[name_single_metadata] = tmpURI


  with open('./metadata/allMetadataURIs/mtdtURIs.json', "w") as file:
    json.dump(dict_URIs, file, indent=2)




def upload_to_ipfs(filepath):
  with Path(filepath).open("rb") as fp:
    metadata_binary = fp.read()
    # ipfs_url = "http://localhost:5001"
    # response = requests.post(ipfs_url + "/api/v0/add", files={"file": image_binary})

    filename = filepath.split("/")[-1:][0]
    response = requests.post(PINATA_BASE_URL + endpoint,
                              files={"file": (filename, metadata_binary)},
                              headers=headers)

    ipfs_hash = response.json()["IpfsHash"]
    uri = "https://ipfs.io/ipfs/{}?filename={}".format(ipfs_hash, filename)    
    print(uri)
    return uri

  print(response)

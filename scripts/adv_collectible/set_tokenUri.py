from brownie import advCollectible, network, config, accounts
from metadata.allMetadataURIs import mtdtURIs


OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"

dev = accounts.add(config["wallets"]["from_key"]);

def main():
  adv_collectible = advCollectible[len(advCollectible) - 1]
  dict_URIs = mtdtURIs.mtdtURIs
  for i in range(1, 101):
    name_single_metadata = 'mtdtTest-' + str(i) + ".json"
    set_tokenURI(i, adv_collectible, dict_URIs[name_single_metadata])

def set_tokenURI(tokenId, nft_contract, tokenURI):
  nft_contract.createCollectible(tokenURI, {"from": dev})
  print(
    "Check new NFT at {}".format(OPENSEA_FORMAT.format(nft_contract.address, tokenId))
    )

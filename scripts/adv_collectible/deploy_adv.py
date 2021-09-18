from brownie import advCollectible, accounts, network, config

def main():
  dev = accounts.add(config['wallets']['from_key']);
  print(network.show_active());
  adv_collectible = advCollectible.deploy(
    {"from": dev}
  );
  return adv_collectible
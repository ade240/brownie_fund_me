from brownie import network, config, accounts, MockAggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet=fork-dev"]
LOCAL_BLOCKHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if(
        network.show_active() in LOCAL_BLOCKHAIN_ENVIRONMENTS
        or network.show_Active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    

    def deploy_mocks():
        print(f"The active network is {network.show_Active()}")
        print("Deploying Mocks...")
        if len(Mockv3Aggregator) <= 0:
               Mockv3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mocks Deployed!")
    

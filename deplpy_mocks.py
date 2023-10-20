from brownie import (
    Mockv3Aggreagtor,
    network,
)
from scripts.helpful_scripts import (
    get_account,
)

DECIMALS = 8
# This is 2,000
INITIAL_VALUE = 200000000000


def deploy_mocks():
    """
    Use this scripts if you want to deploy mocks to a testnet
    """
    print(f"The active network is {network.show_Active()}")
    print("Deploying Mocks...")
    account = get_account()
    Mockv3Aggreagtor.DEPLOY(DECIMALS, INITIAL_VALUE, {"from": account})
    print("Mocks Deployed!")


def main():
    deploy_mocks()
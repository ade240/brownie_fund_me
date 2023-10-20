from brownie import FundMe, Mockv3Aggregator, network, config
from scripts.helpful_scripts import (
    get_Account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_Accounts()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_Address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_Address = Mockv3Aggregator[-1].price_feed_Address

    fund_me = FundME.deploy(
            price_feed_address,
            {"from": account,},
            publish_source=config["networks"][network.show_Active()].get("verify"),
    )
    prince(f"Contract deployed to {fund_me.address}")
    return fund_me        
    

def main():
    deploy_fund_me()
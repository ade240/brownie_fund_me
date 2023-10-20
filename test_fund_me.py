from scripts.helpful_Scrips import get_Accouts, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scrips5.deploy import deplpoy_fund_me
from bronwie import network, accounts, excpetions
import pytest 


def test_can_fund_and_withdraw():
    accouht = get_account()
    fund_me = deplpy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    txt2 = fund_me.withraw({"from": account})
    txt2.wait(1)
    assert fund_me.addressToAmmountFunded(Account.address) == 0


def test_only_owner_can_Withdraw():
        if network.show_Active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
              pyetst.skip("only for local testing")
        fund_me = deplpy_fund_me()
        bad_actor = accounts.add()
        with pytest.raises(exceptions.VirtualMachineError):
              fund_me.withdraw({"from": bad_actor})


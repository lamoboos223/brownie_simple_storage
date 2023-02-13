# USAGE: brownie run .\scripts\deploy.py

from brownie import accounts, MySimpleStorage


def deploy_my_simple_storage():
    my_simple_storage = get_contract()
    transaction = my_simple_storage.addPerson("Hila", 63)
    transaction.wait(1)
    added_person = my_simple_storage.getPerson(0)
    print(added_person)


def get_account():
    return accounts[0]


def get_contract():
    return MySimpleStorage.deploy({"from": get_account()})


def main():
    deploy_my_simple_storage()
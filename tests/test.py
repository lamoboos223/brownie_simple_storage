# USAGE: brownie test .\tests\test.py --disable-warnings

from brownie import accounts, MySimpleStorage


def test_deploy():
    my_simple_storage = MySimpleStorage.deploy({"from": get_account()})
    transaction = my_simple_storage.addPerson("Hila", 63)
    transaction.wait(1)
    starting_value = my_simple_storage.getPerson(0)
    print(starting_value)
    expected = ('Hila', 63)
    assert starting_value == expected


def get_account():
    return accounts[0]

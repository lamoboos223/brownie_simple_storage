create new smart contract project via brownie:

```sh
brownie init
```

add new ganache account using the following:
```sh
brownie account new 0
```

to delete account
```sh
brownie account delete 0
```

create a deploy.py file under /scripts and invoke it using the following:

```sh
brownie run scripts/deploy.py
```

test the smart contract using the following:

```sh
brownie test tests/test.py --disable-warnings
```
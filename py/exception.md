```py
class EpdsException(Exception):
    def __init__(self, msg):
        super(EpdsException, self).__init__()
        self.msg = msg

    def __str__(self):
        return f"EpdsException {self.msg}"


if __name__ == "__main__":
    try:
        raise EpdsException("test")
    except EpdsException as ex:
        print(ex)
    except Exception as ex:
        print(ex)
```


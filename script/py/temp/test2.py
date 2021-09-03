class TestBase(object):
    def __init__(self) -> None:
        super().__init__()

    def prepare(self):
        print("this is base prepare")
    def step1(self):
        pass
    def step2(self):
        pass
    def step3(self):
        print("this is base step3")
    def main_work(self):
        print("this is main work")
        self.step1()
        self.step2()
        self.step3()

class Testwork(TestBase):
    def __init__(self) -> None:
        super().__init__()
    def step1(self):
        super().step1()
        print("this is Testwork step1")
    def main_work(self):
        super().main_work()

handle = Testwork()
handle.main_work()
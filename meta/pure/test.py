
class Test:

    def __init__(self, id_: str,
                 testable: "Testable"):
        self.id_ = id_
        self.testable = testable


class Testable:

    def __init__(self, tests: list["Test"] = None):
        self.tests = [] if tests is None else tests

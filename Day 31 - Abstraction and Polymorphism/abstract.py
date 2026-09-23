from abc import ABC, abstractmethod

class ABsclass(ABC):
    def print(self,x):
        print("Passed value:", x)

    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
class test_class(ABsclass):
    def task(self):
        print("We are inside test_class task")
test_obj=test_class()
test_obj.task()
test_obj.print(100)
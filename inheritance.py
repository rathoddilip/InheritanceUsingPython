# Base class
class Child:

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is student
    def isStudent(self):
        """"
        @:return false is returned
        """
        return False


# Derived class
class Student(Child):
    """"
    @:returns true is returned
    """

    def isStudent(self):
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # An Object of Child
    std = Child("Dilip")
    print(std.isStudent().__doc__)
    print(std.getName(), std.isStudent())

    # An Object of Student
    std = Student("Shivam")
    print(std.getName(), std.isStudent())

# Python program to demonstrate
# multiple inheritance


# Base class1
class Mother:
    motherName = ""

    def mother(self):
        """"
        :returns mother name
        """
        return self.motherName


# Base class2
class Father:
    fatherName = ""

    def father(self):
        return self.fatherName


# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father name :", self.fatherName)
        print("Mother name:", self.motherName)


if __name__ == '__main__':
    s1 = Son()
    s1.fatherName = "RAMDAS"
    s1.motherName = "ANITA"
    s1.parents()

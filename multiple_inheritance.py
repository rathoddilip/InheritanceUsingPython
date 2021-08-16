# Python program to demonstrate
# multiple inheritance


class Mother:
    motherName = ""

    def mother(self):
        """"
        :return mother name
        """
        return self.motherName


class Father:
    fatherName = ""

    def father(self):
        """
        :return father name
        """
        return self.fatherName


class Son(Mother, Father):
    def parents(self):
        print("Father name :", self.fatherName)
        print("Mother name:", self.motherName)


if __name__ == '__main__':
    s1 = Son()
    s1.fatherName = "RAMDAS"
    s1.motherName = "ANITA"
    print(s1.motherName.__doc__)
    print("function return mother name: "+s1.mother())
    print("function return father name: "+s1.father())
    s1.parents()

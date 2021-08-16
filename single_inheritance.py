class Father:
    fatherName = ""

    def father(self):
        return self.fatherName


class Son(Father):

    def parents(self):
        print("Father name :", self.fatherName)


if __name__ == '__main__':
    s1 = Son()
    s1.fatherName = "RAM"
    s1.parents()

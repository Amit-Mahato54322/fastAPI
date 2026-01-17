# we can also declare a class as a data type for a particular variable. 

class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person): #one_person is an instance of the class Person not the class called Person
    return one_person.name
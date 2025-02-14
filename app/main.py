class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    object_list = []
    for human in people:
        obj = Person(human["name"], human["age"])
        object_list.append(obj)
    for human in people:
        current_person = Person.people[human["name"]]
        if "wife" in human and human["wife"] is not None:
            current_person.wife = Person.people[human["wife"]]
        if "husband" in human and human["husband"] is not None:
            current_person.husband = Person.people[human["husband"]]

    return object_list

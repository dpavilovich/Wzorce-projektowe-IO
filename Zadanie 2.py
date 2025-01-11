from abc import ABC, abstractmethod



class Component(ABC):
    @abstractmethod
    def send(self, message):
        pass



class User(Component):
    def __init__(self, name):
        self.name = name

    def send(self, message):
        print(f"User {self.name} received message: {message}")



class Group(Component):
    def __init__(self, name):
        self.name = name
        self.components = []

    def add(self, component):
        self.components.append(component)

    def remove(self, component):
        self.components.remove(component)

    def send(self, message):
        print(f"Group {self.name} propagates message: {message}")
        for component in self.components:
            component.send(message)



def main():
 
    root_group = Group("RootGroup")
    user1 = User("User1")
    user2 = User("User2")
    user3 = User("User3")
    root_group.add(user1)
    root_group.add(user2)
    root_group.add(user3)

   
    print("Testing flat hierarchy:")
    root_group.send("Hello, flat hierarchy!")

    
    sub_group1 = Group("SubGroup1")
    sub_group2 = Group("SubGroup2")
    sub_group3 = Group("SubGroup3")

    sub_group1.add(User("User4"))
    sub_group1.add(User("User5"))

    sub_group2.add(User("User6"))
    sub_group2.add(User("User7"))
    sub_group2.add(User("User8"))

    sub_group3.add(User("User9"))

    
    sub_group3.add(sub_group1)

   
    root_group.add(sub_group1)
    root_group.add(sub_group2)
    root_group.add(sub_group3)

   
    print("\nTesting hierarchical structure:")
    root_group.send("Hello, hierarchical structure!")


if __name__ == "__main__":
    main()

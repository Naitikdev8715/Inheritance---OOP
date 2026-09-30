class ParentClass():
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm
    def show_traits(self):
        print("Eye color:", self.eye_color)
        print("Height (cm):", self.height_cm)
class ChildClass(ParentClass):
    def __init__(self, name, age, eye_color, height_cm):
        super().__init__(eye_color, height_cm)
        self.name = name
        self.age = age
    def show_traits(self):
        super().show_traits()
        print("Name:", self.name)
        print("Age:", self.age)
    def favorite_hobby(self, hobby):
        print(self.name + "'s favorite hobby is " + hobby)
child1 = ChildClass("Naitik", 12, "black", 127)
child1.show_traits()
child1.favorite_hobby("Coding")
print("Is childclass is a subclass of parentclass?", issubclass(ChildClass, ParentClass))

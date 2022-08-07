##### POO ######


#Definition
class human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def salute(self,nametwo):
        return f'Hi {nametwo.name}!, my name is {self.name}'

#The instances
person1 = human("Ariel",37)
person2 = human("Joseph", 22)

print(person1.salute(person2))
# "Hi Joseph, my name is Ariel"



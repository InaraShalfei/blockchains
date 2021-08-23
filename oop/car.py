from vehicle import Vehicle


class Car(Vehicle):
    def brag(self):
        print('Look how cool my car is!')


car1 = Car()
car1.drive()
car1.brag()
car1.add_warning('New warning!')
#print(car1.__dict__)
print(car1)
print(car1.get_warnings())

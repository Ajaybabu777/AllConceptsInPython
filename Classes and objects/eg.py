class Employee:
    def __init__(self, id,name,dept, salary):
        self.id = id
        self.name = name
        self.dept = dept
        self.salary = salary
    
sandhya = Employee(123,"sandhya","Engineering", 500000000)

print("sandhya's dept is ",sandhya.dept)

mahesh = Employee(321,"mahesh","Management",423544364)

print("mahesh's dept is ",mahesh.dept)



# class Car:
#     def __init__(self,brand,model,cost):
#         self.brand = brand
#         self.model = model
#         self.cost = cost

#     def startEngine(self):
#         print("engine started")

#     def stopEngine(self):
#         print("engine stopped")


# car1 = Car("Maruti","Baleno", 900000)
# car2 = Car("Mahindra","Thar",1900000)

# car1.startEngine()
# print(car1.cost)
# car2.stopEngine()
# print(car2.model)
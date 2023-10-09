class Father: # this is a parent class
    def earningMoney(self):
        return("I earn like 50k / month")
    def takeCareOfMyFather(self):
        return("I look after my father Mr Kripa Sindhu")
    def eat(self):
        return("I eat when my body needs food")
    def hairColor(self):
        return("My hair color is black")
    def sleep(self):
        return("I sleep 5 hours a day")
    
class Son(Father):
    def earningMoney(self):
        return("I earn like 30k / month")
    def takeCareOfMyFather(self):
        return("I look after my father Mr Narayana")

s = Son()
print(s.earningMoney())
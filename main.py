import datetime

# Vehicle init and info
class Vehicle():

    def __init__(self, hgsNo, name, surname, date, balance):
      self.hgsNo = hgsNo
      self.name = name
      self.surname = surname
      self.date= date
      self.balance = balance
    
    def info(self):
        print("-----------------------------")
        print("hgsNO:", self.hgsNo)
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("Date:", self.date)
        print("Balance:", self.balance)

# Classes for vehicle type
class Auto(Vehicle):

    def __init__(self, hgsNo, name, surname, date, balance):
        super().__init__(hgsNo, name, surname, date, balance)

    def info(self):
        super().info()

class Minibus(Vehicle):

    def __init__(self, hgsNo, name, surname, date, balance):
        super().__init__(hgsNo, name, surname, date, balance)

    def info(self):
        super().info()

class Bus(Vehicle):

    def __init__(self, hgsNo, name, surname, date, balance):
        super().__init__(hgsNo, name, surname, date, balance)

    def info(self):
        super().info()

# Class for checking balances to pay the fees
class Counter():

    def __init__(self):
        self.autoFee = 10
        self.minibusFee = 13
        self.busFee = 17
        global daily_revenue

    def Payment(self, vehicle):
        if isinstance(vehicle, Auto):
            global daily_revenue
            if vehicle.balance >= self.autoFee:
                vehicle.balance -= self.autoFee
                daily_revenue += self.autoFee
            else:                
                print("-----------------------------")
                print(vehicle.hgsNo, "doesn't have enough balance to pay the fee")
                return 0
                
        elif isinstance(vehicle, Minibus):
            if vehicle.balance >= self.minibusFee:
                vehicle.balance -= self.minibusFee
                daily_revenue += self.minibusFee
            else:
                print("-----------------------------")
                print(vehicle.hgsNo, "doesn't have enough balance to pay the fee")
                return 0
        elif isinstance(vehicle, Bus):
            if vehicle.balance >= self.busFee:
                vehicle.balance -= self.busFee
                daily_revenue += self.minibusFee
            else:
                print("-----------------------------")
                print(vehicle.hgsNo, "doesn't have enough balance to pay the fee")
                return 0
        else:
            return 0

# Class for reporting daily revenue
class Report():

    def __init__(self):
        print("-----------------------------")
        print("Today Revenue:", daily_revenue)

if __name__ == "__main__":        
    
    daily_vehicle = []
    daily_revenue = 0
    counter = Counter()

    vehicle0 = Auto("HGS_4200", "Jeff", "Bezos", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 3)
    if counter.Payment(vehicle0) != 0:
        daily_vehicle.append(vehicle0.info())

    vehicle1 = Minibus("HGS_4201", "Emin", "Taş", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 42)
    if counter.Payment(vehicle1) != 0:
        daily_vehicle.append(vehicle1.info())

    vehicle2 = Bus("HGS_4202", "Elon", "Musk", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 69)
    if counter.Payment(vehicle2) != 0:
        daily_vehicle.append(vehicle2.info())

    Report()
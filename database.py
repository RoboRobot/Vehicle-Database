class vehicle(object):
  def __init__(self, make = None, model = None, year = None, hp = None):
    self.make = make
    self.model = model
    self.year = year
    self.hp = hp

database = []
database.append(vehicle("BMW", "760Li", "2011", "535"))
database.append(vehicle("Mercedes-Benz", "Sprinter", "2016", "161"))
database.append(vehicle("Lexus", "LX570", "2009", "383"))
database.append(vehicle("Toyota", "Prius", "2010", "134"))
database.append(vehicle("Honda", "Odyssey", "2007", "248"))
database.append(vehicle("Honda", "Civic","2009","139"))

for y in range(1,len(database)+1):
  print("%s %s" %(database[y-1].make, y))
x = input("Which vehicle do you want?")
z = raw_input("Information Selection")
if 'all' in z:
  print("The %s %s %s has %s horsepower." %(database[x-1].year, database[x-1].make, database[x-1].model, database[x-1].hp))
if 'make' in z:
  print("Make: %s" %database[x-1].make)
if 'model' in z:
  print("Model: %s" %database[x-1].model)
if 'year' in z:
  print("Year: %s" %database[x-1].year)
if 'hp' in z:
  print("Horsepower: %s" %database[x-1].hp)

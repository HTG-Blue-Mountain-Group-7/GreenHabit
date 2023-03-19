import csv
with open("dataset/CO2_passenger_cars_v12.csv", 'r') as file:
    reader = csv.DictReader(file)
    dataset = dict()
    for row in file:
        print(row)
        # dataset[(row[15], row[16], row[19])] = row[24]


class CarInfo:
    def __init__(self, make, model, engine_type):
        self.make = make
        self.model = model
        self.engine_type = engine_type


# make = input("Please enter your car's make")

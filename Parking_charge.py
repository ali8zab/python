import utils
from utils import Cost
print("==========================================PARKING CHARGE COST==============================================")

Starting_hour = input("Please Enter The Entry Point Hour:  ")
Ending_hour = input("Please Enter The Ending Point Hour: ")
standard_fee = 5000
extra_fee = 1500
hours_amount = float(Ending_hour) - float(Starting_hour)


def Parking_fee():
    if hours_amount < 2:
        return print(f'the price you should pay is {standard_fee}')
    elif hours_amount > 2:
        cost = Cost(5000, hours_amount)
        return print(cost)


       
Parking_fee()
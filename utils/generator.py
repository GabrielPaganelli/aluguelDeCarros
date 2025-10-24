import random
from datetime import datetime

from utils.interface import WEIGHT_OPTIONS

def randomCarId():
    carId = random.randint(0, 999)
    
    return carId

def generateCarPrice(category, brand, fuel_type, transmission, year):
    basePrice = 90.0
    currentYear = datetime.now().year

    year_weight = max(0, (year - 2000) * 1.9)
    depreciation = max(0, (currentYear - year) * 5)

    totalPrice = (basePrice * WEIGHT_OPTIONS["CATEGORIES"][category]) + WEIGHT_OPTIONS["BRANDS"][brand] + WEIGHT_OPTIONS["FUEL"][fuel_type] + WEIGHT_OPTIONS["TRANSMISSION"][transmission] + year_weight - depreciation

    return round(totalPrice, 2)


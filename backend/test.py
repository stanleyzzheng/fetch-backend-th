import re


def get_points(retailer, items, purchaseDate, purchaseTime, total):
    points = 0
    points += len(re.sub("[\W_]", "", retailer))
    # print(len(re.sub("[\W_]", "", retailer)))
    if total.is_integer():
        points += 50

    if total % 0.25 == 0:
        points += 25

    points += (int(len(items) / 2)) * 5
    print(int(len(items) / 2))

    return points


items1 = [
    {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
    {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
    {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
    {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
    {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"},
]
print(get_points("target and things___--11", items1, "2022-01-01", "13:01", 35.35))

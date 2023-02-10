import re
import datetime
import math


def get_points(retailer, items, purchaseDate, purchaseTime, total):
    points = 0
    points += len(re.sub("[\W_]", "", retailer))
    # print(len(re.sub("[\W_]", "", retailer)))

    if float(total).is_integer():
        points += 50

    if float(total) % 0.25 == 0:
        points += 25

    points += (int(len(items.all()) / 2)) * 5
    # date = datetime.datetime.strptime(purchaseDate, "%Y-%m-%d")

    if int(purchaseDate.day) % 2 == 1:
        # print(purchaseDate.day)
        # print("purchaseDate % 2 == 1")
        points += 6

    # time = datetime.time(
    #     int(purchaseTime.split(":")[0]), int(purchaseTime.split(":")[1])
    # )
    time1 = datetime.time(14, 0)
    time2 = datetime.time(16, 0)
    if time1 < purchaseTime < time2:
        print("time1 < purchaseTime < time2")
        points += 10
    print(items.all())
    for item in items.all():
        print(len(item["shortDescription"]))
        if len(item["shortDescription"]) % 3 == 0:
            points += math.ceil(item["price"] * 0.2)
    return points


# items1 = [
#     {"shortDescription": "Mountain Dew 12PK", "price": 6.49},
#     {"shortDescription": "Emils Cheese Pizza", "price": 12.25},
#     {"shortDescription": "Knorr Creamy Chicken", "price": 1.26},
#     {"shortDescription": "Doritos Nacho Cheese", "price": 3.35},
#     {"shortDescription": "Klarbrunn 12-PK 12 FL OZ", "price": 12.00},
# ]
# print(
#     get_points(
#         "Target",
#         items1,
#         datetime.datetime.strptime("2022-01-01", "%Y-%m-%d"),
#         datetime.time(13, 1),
#         35.35,
#     )
# )

# items2 = [
#     {"shortDescription": "Gatorade", "price": 2.25},
#     {"shortDescription": "Gatorade", "price": 2.25},
#     {"shortDescription": "Gatorade", "price": 2.25},
#     {"shortDescription": "Gatorade", "price": 2.25},
# ]


# print(
#     get_points(
#         "M&M Corner Market",
#         items2,
#         datetime.datetime.strptime("2022-03-20", "%Y-%m-%d"),
#         datetime.time(14, 33),
#         9.00,
#     )
# )

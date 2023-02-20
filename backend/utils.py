import re
import datetime
import math


def get_points(retailer, items, purchaseDate, purchaseTime, total):
    """Genertes points gained from receipt object

    Args:
        retailer (string): retailer name
        items (JSON object/dictionary): array of items on receipt
        purchaseDate (date): date receipt was processed
        purchaseTime (time): time receipt was processed
        total (float): total of receipt

    Returns:
        float: points
    """
    points = 0
    #  points += 1 for each alphanumeric in name
    points += len(re.sub("[\W_]", "", retailer))
    # calculate if total is a flat integer
    if float(total).is_integer():
        points += 50
    # calculate if total is a multiple of .25
    if float(total) % 0.25 == 0:
        points += 25
    # calcaulte points for pairs of items
    points += (int(len(items) / 2)) * 5

    #  calculate for if the date is odd
    date = datetime.datetime.strptime(purchaseDate, "%Y-%m-%d")
    if date.day % 2 == 1:
        points += 6
    # calculate for if time is between 14:00 and 16:00
    time = datetime.time(
        int(purchaseTime.split(":")[0]), int(purchaseTime.split(":")[1])
    )
    time1 = datetime.time(14, 0)
    time2 = datetime.time(16, 0)
    if time1 < time < time2:
        # print("time1 < purchaseTime < time2")
        points += 10

    # calculate points for each item length that is a multiple of 3 * .2
    for item in items:
        if len(item["shortDescription"]) % 3 == 0:
            points += math.ceil(float(item["price"]) * 0.2)
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

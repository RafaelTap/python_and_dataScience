import csv

data = [
    ["order", "name", "height (cm)"],
    [1, "George Washington", 189],
    [2, "John Adams", 170],
    [3, "Thomas Jefferson", 180]
      ]

try:
    with open("president_height.csv", 'w') as doc:
        writer = csv.writer(doc)
        writer.writerows(data)
except Exception as error:
    print(error)

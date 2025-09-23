try:
    with open("president_height.csv", 'r') as doc:
        document = doc.read()
        print(document)
except FileNotFoundError as error:
    print(error)



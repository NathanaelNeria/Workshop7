from guitar import Guitar
guitars = []
while True:
    name=input('Name: ')
    if name == "":
        break
    year=int(input('Year: '))
    cost=float(input('Cost: '))

    print('{} ({}) : $ {}  added'.format(name, year, cost))
    guitars.append(Guitar(name, year, cost))

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
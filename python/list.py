#list
cars = ["BMW", "Tyota", "Audi", "Bugatti", "Acura", [ "cycle", "byke"]]


print(cars) # print the cars list

print(cars[3]) # print car 4 in cars
print(cars[5]) # print car 6 in cars

# update a list
cars[3] = "Motor Byke"
print(cars) # print the cars list
print(cars[3]) # print car 4 in cars


print("============================================")
# string as list

str = "Hello python 3.5"
print(str) # print the string
print(str[6]) # print a index from the string

print("============================================")

new_cars = ["vespa", "local bus", "charger", "tesla"]
print(new_cars)
print(cars+new_cars)


print("============================================")

numbers = [1, 2, 5, 6, 7]
print(numbers * 4) # multiply list by 4
print(str * 2) # multiply str by 2

print("============================================")

print("Does Tyota in cars? ")
print("Tyota" in cars) # element existance check

print("============================================")

numbers.append(99) # append an element in numbers
print(numbers)

numbers.insert(3, 40) # insert an element in a position
print(numbers)

print(cars.index("Audi")) # check the index number of Audi car
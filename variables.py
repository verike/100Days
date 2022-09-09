# Variable value switching test

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a="+a)
print("b="+b)

# Band Name Generator
 
welcome_text = 'Welcome to the Band Name Generator.'

print(welcome_text)

city_name = input('What\'s name of the city you grew up in?\n')
# print(city_name)
pets_name = input('What\'s your pet\'s name?\n')
# print(pets_name)
print(f'Your band name could be {city_name} {pets_name}')
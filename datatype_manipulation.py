

# Datatypes : Strings, Boolean, Integer, Float


# num_char = len('Hello dear how are you doing')
# print(f'Your name has {num_char} charcters')
# print(type(num_char))
# new_num_char = str(num_char)
# print(new_num_char)


x = 450
y = 36

z = '300'

# Datatype casting
x_mod = str(x)
y_mod = str(y)

testing = x_mod + z

print(x + float(y_mod))

type(testing)

print(testing)




# from inspect import Parameter, signature

# def gfg(x:str, y:int):
#     pass

# t = signature(gfg) # store signature of the function in a variable 

# print(t) # print the signature of the function

# print(t.parameters['y']) # prints the signature of parameter  
# print(t.parameters['y'].annotation) # prints the annotation of the parameter of the function

# print(t.parameters['x']) # prints the signature of the parameter 
# print(t.parameters['x'].annotation) # prints the annotation of the parameter of the function
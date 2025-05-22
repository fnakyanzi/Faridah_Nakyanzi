#1.single line comment in python
#2.variables
name =("Flamingo") #string
#3.data types
feet = 2 #integer
feathers = 35
height = 5.5 #float
is_bird = True #boolean
list_of_birds=["hen", "parrot","flamingo", "eagle"] #list
tuple_of_birds = ("hen", "parrot", "flamingo", "eagle") #tuple
classifiaction_of_birds = {
    "hen": "domestic bird",
    "parrot": "talking bird",
    "flamingo": "pink bird",
    "eagle": "bird of prey"
} #dictionary
set_of_birds = {"hen", "parrot", "flamingo", "eagle"} #set

#4.type checking Birds
print(type(name)) #<class 'str'> will return string because name is string
print(type(feet)) #<class 'int'> will return integer because feet is integer
print(type(height)) #<class 'float'> will return float because height is float
print(type(is_bird)) #<class 'bool'> will return boolean because is_bird is boolean 
print(type(list_of_birds)) #<class 'list'> will return list because list_of_birds is list
print(type(tuple_of_birds)) #<class 'tuple'> will return tuple because tuple_of_birds is tuple
print(type(classifiaction_of_birds)) #<class 'dict'> will return dictionary because classifiaction_of_birds is dictionary
print(type(set_of_birds)) #<class 'set'> will return set because set_of_birds is set

#5.user input
bird_name = input("What is this bird called?  ") #example: flamingo,eagle,parrot
print("This bird is called: ", + bird_name) #will return the name of the bird the user has entered 
#user input but converting to integer
bird_feathers = int(input("How many feathers does this bird have?  ")) #example: 35
print("This bird has: ", + str(bird_feathers) + " feathers") #will return the number of feathers the user has entered

#6.type conversions
w = 10
x = str(w) #convert integer to string
print(x) #will return "10"
y = float(w) #convert integer to float
print(y) #will return 10.0

#7.operators
f =5
g = 10
print(f + g) #addition
print(f - g) #subtraction
print(f * g) #multiplication
print(f / g) #division
print(f % g) #modulus
print(f ** g) #exponentiation
print(f // g) #floor division

#8.logical operators
a = 7
print(a>6 and a<10) #will return True because 7 is greater than 6 and less than 10
print(a>6 or a<5) #will return True because 7 is greater than 6
print(a<5 or a>10) #will return False because 7 is not less than 5 and not greater than 10
print(not(a>6)) #will return False because 7 is greater than 6
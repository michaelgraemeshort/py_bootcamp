# how do you create a function that modifies another function when that function takes an argument?

# you can't do this:

def shout(func):
	return func(name).upper()

# because NameError: name 'name' is not defined

# and you can't do this:

def shout(func(name)):
	return func(name).upper()

# because this is invalid syntax. you have to do this:



def shout(func):
	def wrapper(name):
		return func(name).upper()
	return wrapper

# i.e. you have to pass name to func by creating a nested function which takes name as an argument

@shout
def greet(name):
	return f"Hi {name}."

# greet = shout(greet)		<- equivalent to decorator

print(greet("Bob"))

'''
you need three functions

the function you wish to decorate
the decorator function
a function inside the decorator function that modifies the first function, conventionally named "wrapper"

the decorator function takes one argument - the function to be decorated
"wrapper" takes whatever arguments are passed to that function

it's all a bit weird
because of the scoping
wrapper takes an argument (name) that is not, on the face of it, passed to shout
but name is passed to greet, which is passed to shout
so wrapper can access that which is passed to shout
if you want wrapper to be flexible in what it accepts, give it the parameters *args and **kwargs
@ syntax ("pie syntax") seems pretty lame as "syntactic sugar" goes
also, why would you write greet = shout(greet)
why wouldn't you write shouty_greet = shout(greet)
maybe pie syntax isn't completely lame
so a decorator takes a function
and returns a function
and has a function in it
'''
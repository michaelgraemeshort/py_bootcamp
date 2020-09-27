from functools import wraps

def eggs(func):
	# @wraps(func)
	def wrapper():
		"""unhelpful wrapper function"""
		return f"fuck you, {func.__name__}"
	return wrapper

@eggs
def spam():
	"""helpful function"""
	return None

print(spam.__name__)
print(spam.__doc__)
help(spam)
# help(wrapper)				<-- doesn't work (name 'wrapper' is not defined)
# print(wrapper.__doc__)	<-- doesn't work either

# looks as though @wraps makes wrapper's docstring inaccessible
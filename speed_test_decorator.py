import time
from functools import wraps

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		"""speed_test wrapper"""
		start_time = time.time()
		result = fn()
		end_time = time.time()
		interval = end_time - start_time
		print(f"Executing {fn.__name__}")
		print(f"Time Elapsed {interval}")
		return result
	return wrapper

@speed_test
def sum_generator_expression():
	"""sums the numbers 1 to 99 using a generator expression"""
	return sum(i for i in range(100))

@speed_test
def sum_list_comprehension():
	"""sums the numbers 1 to 99 using a list comprehension"""
	return sum([i for i in range(100)])

print(sum_generator_expression())
print(sum_list_comprehension())
print(sum_generator_expression.__doc__)
print(sum_list_comprehension.__doc__)
# print(wrapper.__doc__)		<-- rendered inaccessible by @wraps decorator, as far as i can tell
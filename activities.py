from random import choice

def eat(food, is_healthy):
	if not isinstance(is_healthy, bool):
		raise ValueError("is_healthy must be a Boolean")
	elif is_healthy:
		return f"I'm eating {food}, because my body is a temple"
	return f"I'm eating {food}, because YOLO!"

def nap(num_hours):
	if num_hours == 1:
		return f"I'm feeling refreshed after my 1 hour nap"
	return f"Ugh, I overslept. I didn't mean to nap for {num_hours} hours!"

def is_funny(name):
	if name == "tim":
		return False
	return True

def laugh():
	return choice(("haha", "lol"))
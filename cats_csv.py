# with open("cats.csv") as f:
# 	print(f.read())

from csv import reader, DictReader, writer, DictWriter

# with open("cats.csv") as f:
# 	cats_rows = reader(f)
# 	print(cats_rows)			# csv_reader object
# 	for row in cats_rows:
# 		print(row)				# each row is a list

# with open("cats.csv") as f:
# 	cats_dics = DictReader(f)
# 	print(cats_dics)			# csv_DictReader object
# 	for dic in cats_dics:
# 		print(dic)				# each row is a dict

# with open("cats.csv", "w") as f:
# 	add_cat = writer(f)
# 	add_cat.writerow(["Duggee", "huge", "brown"])		# this OVERWRITES

# with open("cats.csv") as f:
# 	cats_lists = reader(f)
# 	cats_lists_allcaps = [[word.upper() for word in lst] for lst in cats_lists]

# with open("cats_allcaps.csv", "w") as f:
# 	add_cat_allcaps = writer(f)
# 	for lst in cats_lists_allcaps:
# 		add_cat_allcaps.writerow(lst)

# with open("new_cats.csv", "w") as f:
# 	csv_writer = DictWriter(f, fieldnames=["Name", "Size", "Colour"])
# 	csv_writer.writeheader()
# 	csv_writer.writerow({"Name": "Jasper", "Size": "small", "Colour": "grey"})

with open("users.csv") as file:
	csv_reader = reader(file)
	next(csv_reader)
	for row in csv_reader:
		print(*row)
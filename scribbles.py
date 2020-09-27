'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''
from csv import reader, writer

def update_users(first_name, last_name, new_first_name, new_last_name):
    with open("users.csv", "r+") as file:
        csv_reader = reader(file)
        csv_writer = writer(file)
        master_list = []
        updates = 0
        for row in csv_reader:
        	if row[0] == first_name and row[1] == last_name:
        		master_list.append([new_first_name, new_last_name])
        		updates += 1
        	else:
        		master_list.append(row)
        for sub_list in master_list:
        	csv_writer.writerow(sub_list)
        return "Users updated: {}.".format(updates)
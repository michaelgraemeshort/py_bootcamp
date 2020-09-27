import re

title = "Significant Others (1987)"

# def reformat_title(string):
#     pattern = re.compile(r"^([\w ]+ )\((\d{4})\)$")
#     result = pattern.match(title)
#     return result.group(2) + " - " + result.group(1)

# alternatively...

def reformat_title(string):
    pattern = re.compile(r"^([\w ]+ )\((\d{4})\)$")
    result = pattern.sub("\g<2> - \g<1>", title)
    return result

print(reformat_title(title))

# text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow." 

# pattern = re.compile(r"M(r|rs|s)\. \w+")
# result = pattern.sub("REDACTED", text)
# print(result)

# # same as...

# pattern = r"M(r|rs|s)\. \w+"
# result = re.sub(pattern, "REDACTED", text)
# print(result)

# # but with the former, you can use COMPLIATION FLAGS. Not sure you can with the latter

# pattern = re.compile(r"(Mrs.|Mr.|Ms.) ([a-z])[a-z]*", re.IGNORECASE)
# result = pattern.sub("\g<1> \g<2>", text)
# print(result)

# def extract_first_phone_number(text):
#     pattern = r"\b(\d{4})|(\(\d{4}\)) \d{3} \d{4}\b"
#     phone_number = re.search(pattern, text)
#     if phone_number:
#         return phone_number.group()

# def extract_phone_numbers(text):
#     pattern = r"\(?\d{4}\)? \d{3} \d{4}"
#     phone_number = re.findall(pattern, text)
#     if phone_number:
#         return phone_number

# # print(extract_first_phone_number("urble wurble"))
# # print(extract_first_phone_number("0191 257 6705"))
# # print(extract_first_phone_number("argle bargle (1234) 123 4567"))
# # print(extract_phone_numbers("(0191) 257 6705 fnar fnar 1234 123 1234 bracket time (4321) 321 4321"))

# def is_valid_phone_number(phone_number):
#     pattern = r"^\(?\d{4}\)? \d{3} \d{4}$"
#     if re.match(pattern, phone_number):
#         return True
#     return False

# numbers = extract_phone_numbers("(0191) 257 6705 fnar fnar 1234 123 1234 bracket time (4321) 321 4321")

# # for number in numbers:
# #     print(is_valid_phone_number(number))

# if all(is_valid_phone_number(number) for number in numbers):
#     print("All numbers are valid phone numbers.")
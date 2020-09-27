def make_song(bottles_remaining=99, drink="soda"):
    while bottles_remaining > -1:
        if bottles_remaining > 1:
            yield "{} bottles of {} on the wall.".format(bottles_remaining, drink)
            bottles_remaining -= 1
        elif bottles_remaining == 1:
            yield "Only 1 bottle of {} left!".format(drink)
            bottles_remaining -= 1
        elif bottles_remaining == 0:
            yield "No more {}!".format(drink)
            bottles_remaining -= 1

kombucha_song = make_song(3, "kombucha")
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))


# def next_prime():

#     def is_prime(num):
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True

#     yield 2
#     count = 3
#     while True:
#         if is_prime(count):
#             yield count
#         count += 2

# get_primes = next_prime()
# for i in range(100):
#     print(next(get_primes))

# def once(fn):
#     already_called = False
#     def inner(*args, **kwargs):
#         nonlocal already_called
#         if not already_called:
#             already_called = True
#             return fn(*args, **kwargs)
#     return inner

# def letter_counter(string):
#     def inner(char):
#         return string.lower().count(char.lower())
#     return inner

# def running_average():
#     nums = []
#     def inner(num):
#         nums.append(num)
#         return round(sum(nums) / len(nums), 2)
#     return inner

# def mode(l):
#     s = set(l)
#     d = dict.fromkeys(s, 0)
#     for i in l:
#         d[i] += 1
#     rev_d = {d[k]: k for k in d}
#     return rev_d[max(rev_d)]

# from collections import Counter

# def mode(l):
#     c = Counter(l)
#     return c.most_common()[0][0]

# def three_odd_numbers(l):
#     for i in range(len(l) -2):
#         if sum(l[i:i + 3]) % 2 == 1:
#             return True
#     return False

# def reverse_vowels(string):
#     vowel_list = [i for i in string if i in "aeiouAEIOU"]
#     vowel_list.reverse()
#     print(vowel_list)
#     new_string = ""
#     for i in string:
#         if i in "aeiouAEIOU":
#             new_string += vowel_list[0]
#             del(vowel_list[0])
#         else:
#             new_string += i
#     return new_string

# def valid_parentheses(string):
#     start_parens = 0
#     end_parens = 0
#     for i in string:
#         if i == "(":
#             start_parens += 1
#         else:
#             end_parens +=1
#         if end_parens > start_parens:
#             return False
#     return string.startswith("(") and string.endswith(")") and string.count("(") == string.count(")")

# def find_greater_numbers(l):
#     greater_than_count = 0
#     start = 1
#     end = 1
#     for i in l[start:]:         # 2, 3, 4
#         for j in l[:end]:       # 1
#             if i > j:
#                 greater_than_count += 1
#         end += 1
#     return greater_than_count

# def sum_up_diagonals(l):
#     diag_1 = []
#     a = 0
#     for i in l:
#         diag_1.append(i[a])
#         a += 1
#     diag_2 = []
#     b = -1
#     for i in l:
#         diag_2.append(i[b])
#         b -= 1
#     return sum(diag_1) + sum(diag_2)

# def range_in_list(l1st, start=0, end=None):
#         return sum(l1st[start:(None if end == None else end + 1)])
    
# def truncate(string, number):
#     if number < 3:
#         return "Truncation must be at least 3 characters."
#     if len(string) >= number:
#         return string[:number - 3] + "..."
#     return string

# def includes(collection, value, start_index=None):
#     if type(collection) == dict:
#         return value in dict.values()
#     return value in collection[start_index:]

# def titleize(string):
#     words = string.split()
#     new_words = []
#     for word in words:
#         new_word = word[0].upper() + word[1:]
#         new_words.append(new_word)
#     return " ".join(new_words)
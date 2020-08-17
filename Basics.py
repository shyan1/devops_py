thinkers = ['Plato', 'PlayDo', 'Gumby']

while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as e:
        print("We tried to pop too many thinkers")
        print(e)
        break

# IOError
# KeyError
# ImportError


class FancyCar():
    wheels = 4

    def driveFast(self):
        print("Driving so fast")


my_car = FancyCar()
my_car.driveFast()

# list
# tuple
# range
# string
# binary
print(2 in [1, 2, 3])
print('a' not in 'cat')
print(10 not in range(2, 3))

my_sequence = 'Bill Gates'
print(my_sequence[-1])
print(my_sequence[-2])
print(my_sequence.index('B'))  # retrurn the first occurrence of the item
print(my_sequence.index('a', 0, 10))

my_sequence = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(my_sequence[2:5])
print(my_sequence[:5])
print(my_sequence[-6:])

print(len(my_sequence))
print(min(my_sequence))
print(max(my_sequence))

print(list())
print(list(range(10)))
print(list("Hello World!"))

empty_list = []

pies = ['cherry', 'apple']
print(pies)
pies.append('rhubarb')
print(pies)
pies.insert(1, 'cream')
print(pies)

desserts = ['cookies', 'paste']
desserts.extend(pies)  # 'extend' to add another list to its own content
print(desserts)

desserts.pop()  # remove the last element
print(desserts)

desserts.remove('apple')  # remove the first occurrence of an item
print(desserts)

# list comprehensions
squares = [i * i for i in range(10) if i % 2 == 0]
print(squares)

# As of Python 3, stings default to using UTF-8 encoding
print(str(12))
print('str(list()) == ', str(list()))
print("str")
print('str')
multi_line = """This is a 
multi-line string,
which includes linebreaks
.
"""
print(multi_line)

input = "  I want more     "
print(input, "|")
print(input.strip(), "|")
print(input.rstrip(), "|")
print(input.lstrip(), "|")

print("HELLO".ljust(10), "|")
print("HELLO".rjust(10), "|")
print("HELLO".rjust(10, "*"), "|")

print("hello world !".split())
url = "gt.motomomo.io/v2/api/asset/143"
print(url.split("/"))

items = ['cow', 'milk', 'break', 'butter']
print(" and ".join(items))

name = "bill Gates"
print(name.capitalize())
print(name.upper())
print(name.title())
print(name.swapcase())
print(name.lower())

name = "William"
print(name.startswith("W"))
print(name.startswith("Wi"))
print(name.endswith("am"))
print(name.endswith("m"))

print("abc123".isalnum())
print("abc123".isnumeric())
print("abc123".isalpha())
print("abc123".istitle())
print("AA".istitle())
print("AA".islower())
print("aa".isupper())

str1 = "%s + %s = %s" % (1, 2, "Three")
print(str1)

f1 = "%.3f" % 1.234565
print(f1)  # 1.235

str2 = "{} comes before {}".format("first", "second")
print(str2)

str3 = "{1} comes after {0}, but {1} comes before {2}".format(
    "first", "second", "third")
print(str3)

str4 = "{country} is an island. {country} is off of the coast of {continent} in the {ocean}".format(
    ocean='Indian Ocean', continent='Africa', country='Madagascar')
print(str4)

values = {'first': 'Bill', 'last': 'Gates'}
str5 = "Won't you come home {first} {last}?".format(**values)
print(str5)

format = "|{0:>22}||{0:<22}|"
print(format.format("O", "O"))

str6 = f"a is {1+2}, b is {2*3}"
print(str6)

# format specifications in f-strings happen within the curly brackets
count = 43
print(f"{count:5d}")

from string import Template
greeting = Template("$hello Bill Gates!")
str_greeting1 = greeting.substitute(hello="Bonjour")
print(str_greeting1)

# Dict

map = dict()
print(map)

kv_list = [['key-1', 'value-1'], ['key-2', 'value-2']]
map = dict(kv_list)
print(map)

map = {'key-1': 'value-1', 'key-2': 'value-2'}
print(map)

print(map['key-1'])
map['key-3'] = 'value-3'
print(map)

if 'key-3' in map:
    print('key-3 in map', map['key-3'])
else:
    print('key-3 not in map')

print(map.get('key-4', 'default-value'))

# remove a key-value pair
del (map['key-1'])
print(map)

print(map.keys())
print(map.values())

for k, v in map.items():
    print(k, v)


def positioned(first=1, second=2):
    """
    doc string...
    """
    print(f"first: {first}")
    print(f"second: {second}")


positioned()
positioned(2, 1)


def no_return():
    """No return defined"""
    pass


res = no_return()
print(res)


def double(input):
    return input * 2


def triple(input):
    return input * 3


funcs = [double, triple]
for func in funcs:
    print(func(1))

items = [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]

sorted_items = sorted(items, key=lambda item: item[2])
print(items)
print(sorted_items)

# Regular Expressions
cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
Rostam Batmanglij <rostam@vpwk.com>,
Chris Tomson <ctomson@vpwk.com,
Bobbi Baio <bbaio@vpwk.com'''

print(cc_list)

import re

# `re.search`, which returns a `re.Match` object only if there is a match
res2 = re.search(r'Rostam', cc_list)
print(res2.span())

re.search(r'[R,B]obb[i,y]', cc_list)

re.search(r'Chr[a-z][a-z]', cc_list)  # Chris

re.search(r'[A-Za-z]+', cc_list)  # one or more
re.search(r'[A-Za-z]{6}', cc_list)  # exact 6 letters

re.search(r'[A-Za-z]+@[a-z]+\.[a-z]', cc_list)

re.search(r'\w+', cc_list)  # r'\w+' is equivalent to [a-zA-Z0-9_]+
re.search(r'\d+', cc_list)  # r'\d+' is equivalent to [0-9]

re.search(r'\w+\@\w+\.\w+', cc_list)

matched = re.search(r'(\w+)\@(\w+)\.(\w+)', cc_list)

print(matched.group(0))
print(matched.group(1))

# Named groups
matched = re.search(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
print(f"""name: {matched.group("name")}
Secondary Level Domain: {matched.group("SLD")}
Top Level Domain: {matched.group("TLD")}""")

# Find All
matched = re.findall(r'\w+\@\w+\.\w+', cc_list)
print(matched)

matched = re.findall(r'(\w+)\@(\w+)\.(\w+)', cc_list)
print(matched)

# Find Iterator
matched = re.finditer(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
for m in matched:
    print(m.groupdict())

# Substitution
# regexes can be used to substitute part or all of a string
print(re.sub("\d", "#", "The passcode you entered was 09876"))

users = re.sub("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)",
               "\g<TLD>.\g<SLD>.\g<name>", cc_list)
print(users)

# Compiling
regex = re.compile(r'\w+\@\w+\.\w+')
regex.search(cc_list)

# Lazy Evaluation


# Generators
# To write a generator function, use the `yield` keyword rather than a return statement
def count():
    n = 0
    while True:
        yield n
        n += 1


counter = count()
print(next(counter))
print(next(counter))
print(next(counter))


def fib():
    first = 0
    last = 1
    while True:
        first, last = last, first + last
        yield first


f = fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

for x in f:
    print(x)
    if x > 12:
        break

# Generator Comprehensions
list_o_nums = [x for x in range(100)]
gen_o_nums = (x for x in range(100))
print(list_o_nums)
print(gen_o_nums)

import sys
print(sys.getsizeof(list_o_nums), sys.getsizeof(gen_o_nums))

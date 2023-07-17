from collections import namedtuple, deque, Counter, defaultdict, OrderedDict

# namedtuple
# Person = namedtuple("Person", ["name", "children"])
# pers_1 = Person("John Doe", ["Timmy", "Jimmy"])
# print(pers_1.name)
# print(pers_1.children)
# pers_1.children.append("Tina")
# print(pers_1.children)

# deque
# dq = deque(maxlen=3)
# for i in range(6):
# 	dq.append(i)
# print(dq)
# dq.appendleft(90)
# print(dq)

Counter
list1 = ['x', 'y', 'z', 'x', 'x', 'x', 'y', 'z', 1]
list_counter = Counter(list1)
print(list(list_counter.elements()))
list_counter[1] = 0
print(list(list_counter.elements()))
print(list(list_counter.most_common()))

counter1 = Counter({'x': 5, 'y': 12, 'z': -2, 'x1': 0})
counter2 = Counter({'x': 2, 'y': 5})

# substract()
counter1.subtract(counter2)
print(counter1)

# update()
counter1.update(counter2)
print(counter1)


# Use case: count the words in a text file
def word_count(filename):
	word_counter = Counter()
	with open(filename, 'r') as f:
		for line in f.readlines():
			words = line.split(" ")
			for word in words:
				word_counter[word] += 1
	return word_counter


counter = word_count('collections_heapq.txt')
print(counter)
print(counter.most_common(4))


# # defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for item in d.items():
# 	print(item)
#
# # One caution with defaultdict is that it will automatically create
# # dictionary entries for keys accessed later on (even if they
# # aren’t currently found in the dictionary).
# # If you don’t want this behavior, you might use setdefault()
# # on an ordinary dictionary instead
#
# regular_dict = {}    # A regular dictionary
# regular_dict.setdefault('a', []).append(1)
# regular_dict.setdefault('b', []).append(2)
# print(regular_dict)
#
#
# # OrderedDict
# number_odict = OrderedDict()
# number_odict["one"] = 1
# number_odict["two"] = 2
# number_odict["three"] = 3
#
# print(number_odict)  # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
#
# number_dict = dict(one=1, two=2, three=1)
# print(number_dict)
# assert number_dict == number_dict
#
# number_odict.move_to_end("one")
# print('moved to end:', number_odict)
# # if pass last=False parameter, then the item moves to the beginning
# number_odict.move_to_end("one", last=False)
# print('moved to end, last=False ->move to beginning:', number_odict)
#
#
# # .popitem() removes and returns an item in LIFO (Last-In/First-Out) order:
# # it removes items from the right end
# number_odict.popitem()
# print(number_odict)
# # if pass last=False parameter, then it removes the item from the beginning
# number_odict.popitem(last=False)
# print(number_odict)

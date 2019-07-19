'''I wanted an easy way to track my harvesting.
This would be the OOP version.'''

# class Harvest(object):
#     def __init__(self, total=0, food={}):
#         self.total = total
#         self.food = food


#     def harvest(self, name, weight):
#     	if name in self.food:
#     		self.food[name] += weight
#     	else:
#     		self.food[name] = weight

#     def get_food(self):
#     	return self.food

# zuke1 = Harvest()
# zuke1.harvest('zucchini', 858)
# print(zuke1.get_food())

# zuke2 = Harvest()
# zuke2.harvest('zucchini', 940)
# print(zuke2.get_food())

# squash1 = Harvest()
# squash1.harvest('Radu squash', 630)
# print(squash1.get_food())


'''Now a function-only version (though not functional,
since it changes the state of a dict), with a scary global variable:'''

food = {}

def harvest(name, weight):
	'''name of the produce, and either weight in grams
	or number of items for small produce,
	such as chili peppers'''
	if name in food:
		food[name] += weight
	else:
		food[name] = weight
	return food

# Let's add some produce

print(harvest('zucchini', 858))
print(harvest('zucchini', 940))
print(harvest('zucchini', 1518))
print(harvest('Radu squash', 630))
print(harvest('Radu squash', 456))
print(harvest('chili pepper', 7))

'''And, finally, let's write it to a file, so I have a running total on an 
easily-accesible separate file:'''

with open('harvest.txt', 'w') as f:
	f.write(f"I have harvested {food['zucchini']/1000} kg of zucchinis so far.\n")
	f.write(f"I have harvested {food['Radu squash']/1000} kg of Radu squash so far.\n")
	f.write(f"I have harvested {food['chili pepper']} chili peppers so far.\n")


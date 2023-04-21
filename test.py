#this file is printed by me to revise python courses 
print("hello me")  #first code:)
if 1>3:
    print("l7ama9")
else:
    print("c faut")

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)
#DATA TYPE----------------------------------------------------------------------------------------------
#Text Type: str 
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType #
#EXAMPLE:
x = 1    # int
y = 2.8  # float
z = 1j   # complex'
print(type(z))  #OUTPUT:<class 'complex'>
#to make a random number
import random
print(random.randrange(1, 10))
#list-------------------------------------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
"""List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) ##  This example returns the items from the beginning to, but NOT including, "kiwi":
print(thislist[2:]) #This example returns the items from "cherry" to the end:


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")  #Check if "apple" is present in the list:

######################################Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
###########################################isertion
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#ajout
thislist.append("orange")
print(thislist)
#                   pour ajouter une liste a la fin d une liste donneee
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
##ajouter un tuple a la fin d une liste
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)            #output:['apple', 'banana', 'cherry', 'kiwi', 'orange']
#supprimer un element de la liste  
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #outpu ['apple', 'cherry']
#remore un elt with his index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) ####################################pop
del thislist[0]  ############################################del
del thislist # SUPPRIMER TOUTE LA LISTE
print(thislist)
#PARCOU5 LIST
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in range(10)]
print(newlist) #OUTPUT : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#functions
def name(name):
   print("mme "+name)
name("chaymaa")
"""now 'if we don't know how many  arguments will be passed into your function,  we should add a * before the parameter name in the function definition."""
def name(*noms):
   print("names are"+noms) 
name("Emil", "Tobias", "Linus")
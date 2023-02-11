#-----------------------------------------------------------Different types of sets 

# set of integers
my_set = {1, 2, 3,3,3}
print(my_set) #output: {1,2,3}-> set cannot have duplicates !!

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set) #output: {1.0, (1, 2, 3), 'Hello'}

# we can make set from a list
my_set = set([1, 2, 3, 2])
print(my_set)# Output: {1, 2, 3}

# initialize a Empty set()
a = set()

my_set = {1, 3}
print(my_set) #Output: {1, 3}


#-----------------------------------------------------------add/update/discard


#add a single element using the add() method
my_set.add(2)
print(my_set) #output:{1, 2, 3, 4}

#add multiple elements using update() method
my_set.update([2, 3, 4,5,6,7])
print(my_set) #output: {1, 2, 3, 4, 5, 6, 7}

#remove a item with discard() method
my_set.discard(4)
print(my_set) #output: {1, 2, 3, 5, 6, 7}


#-----------------------------------------------------------Pop/Clear
 
my_set = set("HelloWorld")
print(my_set)# Output:{'e', 'o', 'H', 'W', 'l', 'r', 'd'}

# pop an element
 
print(my_set.pop())# Output:e

# pop another element
my_set.pop()
print(my_set) # pop: o Output:{'H', 'W', 'l', 'r', 'd'}


# clear my_set
my_set.clear()
print(my_set)# Output: set()

#-----------------------------------------------------------Examples 
#-------------------------------------------------------------------Set Union


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}


# use | operator
print(A | B)# Output: {1, 2, 3, 4, 5, 6, 7, 8}

#-------------------------------------------------------------------Set Intersection


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
print(A & B)# Output: {4, 5}

#-------------------------------------------------------------------Set Diffrence 

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
print(A - B)# Output: {1, 2, 3}


#Autor:     MAX WÖLFEL
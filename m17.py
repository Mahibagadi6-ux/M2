# sets are also is collection of the unique ithmes these are the unordered unindexed , can be represedted as {}
s = {1,2,3,4,5,6,7,8,9}
print(s)
#print(s[0]) # this line error because of the indexing not allows indexing


s1 = {1,2,3,4,5,6,7,8,9}
s2 = list(s)
print(s2)
s3 = (1,2,3,4,5,6,7,8,9)
s4 = tuple((3,4,5,6,7,8,9))
print(s4)


# we want  write empty set went write like this
s = set() # if pyhon interpreter take dictionry
print(type(s))


# very very imp thing in sets are in operation , already we learnt aboubt union , inter section  and minus opertetr
s1 = {1,2,3,4,5,6,7,8,9}
s2 = {9,10,11,12,13,14,15,16,17,18,19,20}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)

# we can add other element
s4 = {1,2,3,4,5,6,7,8,9}
s4.pop()
print(s4)

#  we want check which element is poped
print(s4.pop())
print(s4.discard(4))

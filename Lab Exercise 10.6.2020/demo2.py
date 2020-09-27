## List Demo
## Author: nmessa
## Date: 9.26.2017
def friend(lst, name):
    lst.append(name)
    return lst
    
def unfriend(lst, name):
    if name in lst:
        lst.remove(name)
    else:
        print(name + " is a non-existent friend")
    return lst

def printFriends(friendsList):
    for friend in friendsList:
        print(friend, end = ' ')
    print()

#Create an empty list
friends = []

#Add friends
friends = friend(friends, "Bob")
friends = friend(friends, "Mary")
friends = friend(friends, "Alice")
friends = friend(friends, "Jack")
print("My friends are", end = ' ')
printFriends(friends)

#Remove a friend
print("I am unfriending Jack")
friends = unfriend(friends, "Jack")
print("My friends are now", end = ' ')
printFriends(friends)

#Remove a friend that does not exist
friends = unfriend(friends, "Mason")
print("My friends are now", end = ' ')
printFriends(friends)

#Re-friend Jack
friends = friend(friends, "Jack")
print("My friends are now", end = ' ')
printFriends(friends)

## Output
## My friends are Bob Mary Alice Jack 
## I am unfriending Jack
## My friends are now Bob Mary Alice 
## Mason is a non-existent friend
## My friends are now Bob Mary Alice 
## My friends are now Bob Mary Alice Jack



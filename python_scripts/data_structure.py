







my_group = ["Ian","Jian","Carla","Niamh","Ahmed"]
print(my_group)

my_group.append("David")
print(my_group)

#print the 3rd and the 5th element of the list
print(my_group[2],my_group[4])

#sort the list
my_group.sort()
print(my_group)

print(my_group[2],my_group[4])

#Select the first 2 letters of the third value

third_value = my_group[2]

print(third_value[:2])

#or
print(my_group[2][:2])

#Convert a list to a dictionary

grade = ["participant", "participant" , "trainer" , "participant" , "participant"]

mygroup_dictionary = dict(zip(my_group, grade))
print(mygroup_dictionary)

#Using a loop

team={}
for name in my_group:
    if name == "David":
        team [name] = "trainer"
    else:
        team [name] = "participant"
    
print(team)


#print selected eements of a dictionary

for name, grade in team.items():
    if grade == "participant":
        print(name)
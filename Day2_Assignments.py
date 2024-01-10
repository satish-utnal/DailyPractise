# 1- write a program which takes single input from user contaning first name,last name and age as comma separated value and display then in 3 lines in given format below.

# example user input : Ankit,Bansal,35

# output:
# First name is Ankit
# last name is Bansal
# Ankit is 35 years old
#
# note : do not hardcode name at any place

pDetail = input("Enter person details first name last name and age : ")
pDetailList = pDetail.split(",")

print(f'First Name is ' + pDetailList[0])
print(f'Last Name is ' + pDetailList[1])
print(f'' + pDetailList[0] + ' is ' + pDetailList[2] + ' years old')

# 2- given 2 list as list1= [1,3,4] and list2 = [2,4,6]
#
# combined the 2 list and diplay the same without using extend method

list1 = [1, 3, 4]
list2 = [2, 4, 6]
listconcatenated = list1 + list2
print(listconcatenated)

# 3- given a list list1=[1,2,3,4,5,6,7,8]
# display a new list which contains only odd position index values from above list.

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
listOdd = []
listOdd.append(list1[1])
listOdd.append(list1[3])
listOdd.append(list1[5])
listOdd.append(list1[7])
print(listOdd)


# 4- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a ipl team name as input from user and display a list of all elements from that name.
# example : input : KKR
# output : ['KKR','LSG','PBKS']

ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
print(ipl)
tName = input("Enter Team Name to display a list of all elements from that name : ")
try:
    print(ipl[ipl.index(tName):])
except ValueError:
    print("Team name not found")


# 5- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take an ipl team name as input from user and display a list of all elements except input one
# example : input : KKR
# output : ['CSK','MI','LSG','PBKS']

ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
print(ipl)
tName = input("Enter team name to remove from list : ")
try:
    ipl.remove(tName)
    print(ipl)
except ValueError:
    print("Team name not found to remove")


# 6- ipl= ['CSK','MI','KKR','LSG','PBKS'] take a user input contains 2 comma separated values index,new_team . replace
# the index element of list with new value and display the same
# example : input : 2,SRH
# output : ['CSK','MI','SRH','LSG','PBKS']

ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
print(ipl)
tName = input("Enter index number and team name to replace with existing list: ")
tList= tName.split(',')
try:
    ipl[int(tList[0])] = tList[1]
    print(ipl)
except ValueError:
    print("Team name not found in the existing list")

# 7- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take ipl team name as user input. display True if the team exists else display False.

ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
print(ipl)
tName = input("Enter Team Name to check whether its present in list or not : ")
print(tName in ipl)

# 8-ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma separated values index,new_team . Add the new value at that index in the list.
# Display the old list , new list,length of original and new list

# example : input : 2,SRH
# output :
# old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
# new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
print(ipl)
tName = input("Enter index name and team name to add to existing list : ")
oldteam = ipl
newteam = ipl.copy()
tName1=tName.split(',')
newteam.insert(int(tName1[0]),tName1[1])
print(f'Old list : '+str(oldteam)+' and length '+str(len(oldteam)))
print(f'Old list : '+str(newteam)+' and length '+str(len(newteam)))

# 9- given a list of numbers, write a program to find the mean of the numbers in list

list1=[1,2,3,4,5,6,7,8,9,10]
print(f'Mean of given list is : '+str(sum(list1)/len(list1)))

# 10- create a dictionary to store following attributes of CSK
# key "CSK" ; attributes : team full name , captain , playing 11 for each match(name of players), oppenont name (assume there are 3 matches only against MI, RCB , GT ) and result won/loss

dict = {"CSK": {"name": "Chennai super kings", "captain": "MSD",
                "players": ["MSD", "Player1", "Player2", "Player3", "Playe4", "Player5", "Player6", "Player7", "Player8", "Player9", "Player10"],
                "Opponents": ["MI", "RCB" , "GT"],
                "results" :["win", "loss", "loss"]
               }
       }
print(dict["CSK"])

# 11- in the previous dictionary add one more item for RCB. you can choose any 3 opponents.
dict.update({"RCB":{"name":"royal challengers Bengaluru" ,"captain": "Virat","players":["Virat", "Player1", "Player2", "Player3", "Playe4", "Player5", "Player6", "Player7", "Player8", "Player9", "Player10"], "Opponents": ["MI", "CSK", "KKR"], "results": ["win", "Win", "Win"]}})
print(dict["RCB"])
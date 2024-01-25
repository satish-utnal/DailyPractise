


#Calclulating BMI
#1- write a program which takes 2 inputs from the user : weight(kg) and height(meter) and prints the BMI in the output.
#BMI = weight / (square of height)
weight=input("Enter weight of the person: ")
height=input("Enter height of a person: ")
print("Calculating BMI...")
BMI=float(weight)/(float(height)**2)
print(f'Restricted to 4 decimal places'+format(BMI,'.4f'))
print(f'Without restricting decimal places'+str(BMI))


#2- write a program which takes the name of the user as input and 
#replace all the occurence of character 'a' in the name to 'b' and print it.
name= input("Enter name of a person")
name.replace('a','b')



#3.write a program which takes 2 inputs from user as principle amount (int) and rate of annual 
#interest (float) and print the expected total amount  after  2 years.
p=int(input("enter principle amount : "))
rt=float(input("Enter rate of interest"))
totalamt=p*((1+(rt/100))*(1+(rt/100)))
print(format(float(totalamt),'.2f'))


#4- write a program which takes city name from user input. irrespective of in which case user enters the city name, print the city name in camel case meaning 
#first letter should be capital and rest in small.
input("Eneter City Name to print it as first letter capital : ").capitalize()





#5- write a program which takes the name of the user as input and print the index of character 'a' in the string. 
#if 'a' is not there then return -1.
uname=input("Enter User Name to get index of letter a ")
try:
    print(uname.index('a'))
except ValueError:
    print('-1')




#6-  Display the number of letters in the below string
my_word = "antidisestablishmentarianism"
len(my_word)




#7- take 3 inputs from user : first name , last name and age . Display the information in below format
#exmaple 
#first name : MOhit
#last name : sharma 
#age 32

#Display : my name is Mohit Sharma and I am 32 years old.

#note that first letter of first name and last name both should be in capital letters and rest in smal
fname=input("Enter First name: ")
lname=input("Enter Last name : ")
age=input("Enter the age: ")
print(f'My name is '+fname.capitalize()+' '+lname.capitalize()+' and I am '+age+' years old.')





#8-take 3 inputs from user : first name , last name and company name. create the email alias for the user and display it.  Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
#example 
#first name : MOhit
#last name : sharma 
#company : infosys

#Display : morma@infosys.com 

#note full email id should -be in lower case
fname=input("Enter First name: ")
lname=input("Enter Last name : ")
company=input("Enter the company name: ")
print(fname.lower()+'.'+lname.lower()+'@'+company.lower()+'.com')








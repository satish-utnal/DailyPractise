# 8- given below dictonaries of states and their capital:

capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}

# pick a state from above dictonary and ask user to enter the capital of the state.If the user answers incorrectly, then repeatedly ask them
# for the capital until they either enter the correct answer or type "exit".
# If the user answers correctly, then display "Correct" and end the program. However, if the user exits without guessing correctly, display
# the correct answer and the word "Goodbye".
#
# Note: Make sure the user isn’t punished for case sensitivity. In other words, a guess of "Denver" is the same as "denver". Do the same for exiting—"EXIT" and "Exit" should work the same as "exit".
print(f'Enter Correct answer or enter exit ')

st = input("Enter state name from dictionary : ")

while(True):
    answer = input("Enter capital name from dictionary : ")
    if answer.lower() == 'exit':
        print(f'Good bye the Capital of {st} is {capitals_dict[st]}')
        break
    elif capitals_dict[st].lower() == answer.lower():
        print(f'Correct')
        break
    else:
        pass

#9- write a program to take state as input from user and print the capital of the state using above dictonary.
# If the state is not there in dictonary then print "sorry , information not available"
print(f'Enter state name : ')
st = input("Enter state name from dictionary to check whether its preset or not: ")
if st in capitals_dict.keys():
    print(capitals_dict[st])
else:
    print(f"Sorry no such state in dictionary")




#Determined loops

#For
list1 = [1,2,3] #you can loop through list
for c in list1:
    print("hello")

string1 = "Hola" #you can loop through strings
for c in list1:
    print("hello")


#Range data type

for c in range(5):         #f type function (special notation)
    print(f"value is {c}") #c between keys works like a variable even that it is inside a string, helps to not to use concatenation operators

for c in range(4,10,3): #lowerbound, upperbound and step 
    print(c)

email = "emailtest@gmail.com"
for i in range(len(email)):
    if email[i]== "@":
        valido = True
print(valido)



#Undetermined loops

#determined while loop: you can determine previously a while loop before excecution
i = 1
while i <= 10:
    print("execution" + str(i))
    i += 1

print("execution finished")


#undetermined while loop: we don't know how many times the loop will run, depends on user input

""" age = int(input("introduce age"))

while age<0:
    print("negative age, try again")
    age = int(input("introduce age")) """

#Continue: jumps to the next loop iteration

for i in [1,2,3]:
    if i == 2:
        continue
    print(i)

#Pass: loop returns null. Ignores the loop statement: used place the loop and code it later.

for i in [1,2,3]:
    pass

#else: works as an normal else in conditional statements, when the loops iterations ends, else is executed.

while 1 != 1:
    print("condition matched")
else:
    print("condition not matched or loop ends")

#break: terminates the loop

for i in [1,2,3]:
    if i == 2:
        break
    print(i)
from random import randint

# Open the file for appending text to the end
f = open("textfile.txt", "w+")


num = randint(1,25)

for i in range(num):
    f.write("This is line " + str(i+1) + "\n")

f.close()

y = open("textfile.txt", "r")

if (y.mode == 'r'):
    fl = y.readlines()
    for x in fl:
        print (x)

y.close()


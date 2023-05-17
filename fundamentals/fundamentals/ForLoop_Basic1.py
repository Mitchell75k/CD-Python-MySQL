#1- print all integers from 0-151
for i in range(0,151):
    print(i)

#2- print all the multiples of 5 from 5-1000
for i in range(5,1001, 5):
    print(i)

#3- print integers 1-100. if divisible by 5, print "coding" instead. if divisible by 10, print "coding dojo"
for i in range(1,101):
    if i % 10 == 0: # we add == 0 because we want to know if the remainder is 0, meaning it is divisible by 10. a remainder of 1 means it is not divisible by 10
        print ("coding dojo")
    elif i % 5 == 0:
        print ("coding")
    else:
        print (i)

#4- 'that sucka's huge'- add all the odd integers from 0-500,000, and print the final sum
sum= 0
for i in range (1,500000,2):
    sum= sum + i
print(sum)

#5- print positive numbers starting at 2018, counting down by fours
for i in range(2018,0,-4):
    print(i)

#6- set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum,
# only print  the integers that are a multiple of mult. 
# for example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum=0
highNum=17
mult=4
for i in range(lowNum,highNum):
    if i % mult == 0:
        print(i)

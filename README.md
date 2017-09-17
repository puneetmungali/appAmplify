# appAmplify
Random Number Generator

#a list containing all the random numbers generated

randomNumbers = []



#mid value of the range between which the random numbers must occur.

mid = int((self.start+self.end)/2)



#giving value to variables for keeping a record of how many ranodm numbers will be > mid and how manu numbers will be < mid, based on how many random numbers we want

maxrange = int(.73*self.count)
minrange = int(.27*self.count)
        
        
        
#mod will act as a controller to limit the number generate within the range of numbers we want, (end - start) will give a integer number

mod = self.end - self.start + 1

#we will run a loop based on how many random numbers we want

for i in range(1,self.count+1):


#find a pseudo random number

pseudo_rand = (self.id+(self.end-self.id)*i)%mod

#pseudo_rand number will be in range of 0 to mod variable to find actual random number we have to add it to start\

ranNum = pseudo_rand + self.start

#providing biasing

#if generated number is less than mid

if ranNum < mid:

#and if we have already created enough numbers which are less than mid then add mid to it to make it greater than mid

if minrange == 0:

ranNum += mid

#decrease the counter keeping track of amount of generated numbers which are greater than mid 

maxrange -= 1

#if we haven't created enought numbers which are less than mid then keep it same

else:

#decrease the counter keeping track of amount of generated numbers which are less than mid 

minrange -= 1

#if number generated is greater than mid

else:

#and if we have already created enough numbers which are greater than mid then substract mid to it to make it less than mid

if maxrange == 0:

ranNum -= mid

#decrease the counter keeping track of amount of generated numbers which are less than mid

minrange =- 1

#if we haven't created enought numbers which are greater than mid then keep it same

else:

#decrease the counter keeping track of amount of generated numbers which are greater than mid

maxrange -= 1

#adding random number to list

randomNumbers.append(ranNum)

self.id=ranNum

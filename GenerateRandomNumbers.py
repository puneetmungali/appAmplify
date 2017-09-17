class GenerateRandonNumber():
    def __init__(self,start,end,count):
        self.start = start
        self.end = end
        self.count = count
        self.id = id(self)

    def getNumbers(self):
        randomNumbers = []
        #count of random numbers greater than mid value
        maxrange = int(.73*self.count)
        #count of random numbers less than mid value
        minrange = int(.27*self.count)
        #mid value
        mid = int((self.start+self.end)/2)
        #will determine in what range do we require the random numbers
        mod = self.end - self.start + 1
        for i in range(1,self.count+1):
            #find a pseudo random number
            pseudo_rand = (self.id+(self.end-self.id)*i)%n
            ranNum = pseudo_rand + self.start
            #providing biasing
            if ranNum < mid:
                if minrange == 0:
                    ranNum += mid
                    maxrange -= 1
                else:
                    minrange -= 1
            else:
                if maxrange == 0:
                    ranNum -= mid
                    minrange =- 1
                else:
                    maxrange -= 1
            #adding random number to list
            randomNumbers.append(ranNum)
            self.id=ranNum
        return randomNumbers

obj = GenerateRandonNumber(1,10,100)
lists = obj.getNumbers()
less,greater = 0,0
for item in lists:
    if item < 5:
        less += 1
    else:
        greater += 1
print(less)
print(greater)

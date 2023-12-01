#2023 - Day1 - Part1 - COMPLETED

dataFile = open("data.txt","r")
#line = dataFile.readline()
#print(line)
#dataFile.close()
score = 0
count = 0
# Strips the newline character
for line in dataFile:
    
    count += 1
    lineLen = len(line)
    listDig = []
    
    for i in range(lineLen):
      loc = line[i]
      x = loc.isnumeric()
      if x == True:
        listDig.append(loc)  
    
    if len(listDig) == 1:
      amount = str(listDig[0]) + str(listDig[0])
      score = score + int(amount)
      
    else:
      amount = str(listDig[0]) + str(listDig[-1])
      score = score + int(amount)
print("Day one answer is: ",score)
      
    
      
        
    
    
    
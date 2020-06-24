import random  
def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end))  
    return res 
num = 50
start = 1
end = 10000
print(Rand(start, end, num)) 
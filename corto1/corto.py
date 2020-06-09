
def Collatz(num):
    
    res = []  
    numero = 0                                      
    for i in range (2, num +1):
        numero = i+1
        while (i > 1):           
            if i % 2 == 0:
                numero = i/2
            else:
                numero = (i*3)+1
            res.append(numero) 

    return res
      
print(Collatz(5)) 
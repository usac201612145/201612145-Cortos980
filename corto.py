
def Collatz(num):
    
    res = []  
    numero = 0                                      
    for i in range (1, num +1):
        numero = i+1

        while numero != 1:
            if numero % 2 == 0:    #mukltplica por dos
                numero = numero/2
            else:
                numero = (numero*3)+1
            res.append(numero) 
      
print(Collatz(145)) 
def calcula(v):
    vf = 1
    for i in range(1,v+1):
        vf *= i
    return vf
n = int(raw_input())
print calcula(n)

    

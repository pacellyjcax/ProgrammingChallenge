def c(vi,pv,vd):
    if len([x for x in range(vi,vi+pv) if x == vd]) == 1:
        #calculo
    else:
        c(vi+pv,pv+6)
    
    

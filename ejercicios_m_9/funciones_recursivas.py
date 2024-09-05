def sumatorio(numero):
    if(numero>0):
        numero=numero+sumatorio(numero-1)
    return numero

print(sumatorio(5))
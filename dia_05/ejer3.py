def ceros_vecionos(*args):
    contador = 0
    for num in  args:
        if contador +1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False

print(ceros_vecionos(5,6,8,7,4,52,1,8,97,0,0,4))
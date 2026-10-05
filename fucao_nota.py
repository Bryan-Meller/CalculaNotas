def media_ponderada(n1, n2,n3):
    '''calcular a media ponderada de 3 notas'''
    p1=2
    p2=3
    p3=5
    if n1>p1 or n2>p2 or n3>p3:
        print("Nota invalida")
        exit()
    return (n1*p1+n2*p2+n3*p3)/(p1+p2+p3)

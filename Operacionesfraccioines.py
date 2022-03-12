def MCD(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a
def simplificacion(a,b):
    c=MCD(a,b)
    n=str(int(a/c))
    m=str(int(b/c))
    return('{}/{}'.format(n,m))
def sumafra(a1,b1,a2,b2):
    f=a1*b2
    g=a2*b1
    o=b1*b2
    p=f+g
    i=MCD(p,o)
    e=str(int(p/i))
    u=str(int(o/i)) 
    if o==0:
        print("no se puede dividir por 0")
    return('{}/{}'.format(e,u))
def restafra(a1,b1,a2,b2):
    f=a1*b2
    g=a2*b1
    o=b1*b2
    p=f-g
    i=MCD(p,o)
    e=str(int(p/i))
    u=str(int(o/i)) 
    if o==0:
        print("no se puede dividir por 0")
    return('{}/{}'.format(e,u))
def multifra(a1,b1,a2,b2):
    l=a1*a2
    m=b1*b2
    i=MCD(l,m)
    e=str(int(l/i))
    u=str(int(m/i))
    if m==0:
        print("no se puede dividir por 0")
    return('{}/{}'.format(e,u))
def divisionfra(a1,b1,a2,b2):
    l=a1*b2
    m=b1*a2
    i=MCD(l,m)
    e=str(int(l/i))
    u=str(int(m/i))
    if m==0:
        print("no se puede dividir por 0")
    return('{}/{}'.format(e,u))
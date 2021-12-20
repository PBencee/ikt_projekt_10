def temp(c):
    if c>100 :
        print("forr")
    elif c==100 :
        print("forr.pont")
    elif 80<c<100:
        print("forró")
    elif 40<c<81:
        print("meleg")
    elif 0<c<41:
        print("normál")
    elif 0 == c :
        print("fagypont")
    elif c < 0:
        print("fagy") 

for x in reversed(range(-20,121,20)): 
    print(x, end="")
    print("°C -> ", end="")   
    temp(x)
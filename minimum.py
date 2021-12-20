#Írj egy Python programot,amely bekér egy dolgozat pontszámot(x)a felhasználótól és kiír egy érdemjegyet az alábbi szerint! 1:x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.

x=int(input("Hány pontszámot kaptál? "))

if(x<50):
    print("1-es")

elif(50<=x<60):
    print("2-es")

elif(60<=x<70):
    print("3-as")

elif(70<=x<85):
    print("4-es")

else:
    print("5-ös")
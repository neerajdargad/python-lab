#name:neeraj dargad
#batch no.:p1       roll no.:9

d={}
x=int(input('number of students '))
for i in range (x):
    n=input("name of student: ")
    g=int(input("Gr no.: "))
    b=input("Batch no.: ")
    d[g]=(n,b)
    print(d)

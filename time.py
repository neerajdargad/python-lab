#name:neeraj
#div:p      batch no.=1
'''a programme to covert seconds into days,hours,minutes and seconds'''
x=int(input('time in seconds '))
q1=x//86400
r1=x%86400
q2=r1//3600
r2=r1%3600
q3=r2//60
r3=r2%60
q4=r3
print(q1,q2,q3,q4)


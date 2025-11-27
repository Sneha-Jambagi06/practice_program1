import sys
if len(sys.argv)==6:
  script_name=sys.argv[0]
  m1=sys.argv[1]
  m2=sys.argv[2]
  m3=sys.argv[3]
  m4=sys.argv[4]
  m5=sys.argv[5]
else:
  script_name=sys.argv[0]
  m1=85
  m2=65
  m3=95
  m4=100
  m5=95
total=m1+m2+m3+m4+m5
avg=total/5
if(avg>90):
   grade='A'
elif(avg>80):
  grade='B'
elif(avg>70):
  grade='C'
elif(avg>60):
  grade='D'
elif(avg>50):
  grade='E'
elif(avg<40):
  grade='Fail'
  
print("Marks1:",m1)
print("Marks2:",m2)
print("Marks3:",m3)
print("Marks4:",m4)
print("Marks5:",m5)
print("Average:",avg)
print("Grade:",grade)

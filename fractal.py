from turtle import*
import random
import string
alphabet = list(string.ascii_lowercase)
speed(10)
keys = []
values  = []
x = []
y = []
prop = float(input("Proportio = "))
num_dots = int(input("Number of points = "))
point_ = [random.randint(1,300),random.randint(0,300)]


for i in range(0,num_dots):
    keys.append(alphabet[i])
    values.append(i)
points=dict(zip(keys, values))

for i in range(0,num_dots):
    x.append(int(input(f"x{i} = ")))
    y.append(int(input(f"y{i} = ")))
#print(x)
#print(y)

for i in range(0,num_dots):
    up()
    goto(x[i],y[i])
    down()
    circle(1)
  
up()
goto(point_[0],point_[1])
down()
dot(2)

while True:
    choose = random.randint(0,num_dots-1)
    point=x[points[keys[choose]]],y[points[keys[choose]]]
    point_=[(point_[0]+point[0])/prop,(point_[1]+point[1])/prop] #formula
    #print(point_)
    up()
    goto(point_[0],point_[1])
    down()
    dot(2)








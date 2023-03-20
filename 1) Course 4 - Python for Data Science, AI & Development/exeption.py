a = 1

# try:
#     b = int(input("Please enter a number to divide a"))
#     a = a/b
#     print("Success a=",a)
# except:
#     print("There was an error")

x="Go"

if(x=="Go"):

  print('Go ')

else:

  print('Stop')

print('Mike')

x=5
while(x!=2):
  print(x)
  x=x-1
  
  
class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p1=Points("A","B")
p1.print_point()

class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p2=Points(1,2)

p2.x=2

p2.print_point()

a=1

def do(x):
    a=100
    return(x+a)

print(do(1))
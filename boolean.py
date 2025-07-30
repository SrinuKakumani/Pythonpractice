# To check whether the boolean value is True or False
print(20 > 10)
print(10 < 5)

#Print a message based on whether the condition is True or False
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate a string and a number
print(bool("Hello"))
print(bool("15"))

#Almost any value is evaluated to True if it has some sort of content.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#However, some values are evaluated to False, such as empty strings, the number 0, and the value None.
print(bool(""))
print(bool(None))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#To create functions that returns a Boolean Value:
def myFunction() :
  return True

print(myFunction())
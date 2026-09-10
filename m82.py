# exception handling :
# the occures is due to the wrong code error like syntax error and invalidnumber like number of the erro occures is due to wrond
# while uses the try,else,except,finally
# they most imp for any project remeber all
a = 10
b = 0
try:
    print(a/b)
except:
    print("error")
finally:
    print("error banto baralillavo nang enn matter aagalla ")
a = 10
b = 20
try:
    print(a/b)
except Exception as e:
    print(f"error  {e}")
finally:
    print("error banto baralillavo nang enn matter aagalla ")


a = int(input("a : "))
b = int(input("b : "))
try:
    print(a/b)
except Exception as e:
    print("error",e)
    b = int(input("b : "))
finally:
    print("error banto baralillavo nang enn matter aagalla ")

name = input(" Tell me ,whom want you marry ____  ")
try:
    if name.lower() == "mahesh":
        print("yes you choose best option ")
except Exception as e:
    print("you choose wrong dicision please choose him , and temm me agin below column ,",e)
    name = input(" Tell me ,whom want you marry ____  ")
else:
    print("you choose wrong option ")
    name = input(" Tell me ,whom want you marry ____  ")
    if name.lower() == "mahesh":
        print("yes you choose best option ")
finally:
    print("i choosed invalid name ")

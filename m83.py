#file handling
#file handling means to read and write the files and to build a very real world application (storing data,logging , vlog etc)
#why file handling :1.to store the dat perminantaly and to read the content in the file
# adress books
# billing system
# REPORT CART GENEARTER
file  = open("massage txt","r")
content = file.read()
print(content)
file.close()


# write is over rides the olds files means delete it self and put the new data
file  = open(".student.massage txt","w")
file.write("mahesh\n vishwa \n vidya \n jassu \n indramma \n sulappa ")
file.close()

# to stop the over ride useing one funtion that is "a"
file  = open("student.massage txt","a")
file.write("\n mallikajun \n malappa \n pacchi")
file.close()


file  = open("student.massage txr","a")
file.write("\n mallikajun \n malappa \n pacchi")
file.close()

try:
    file = open("family.massage txt","w")
    file.write("\n mallikajun \n malappa \n pacchi")
except Exception as e:
    print(f"error found {e}")
else:
    print("error bandilla  well done you wrote current code ")
finally:
    file.close()





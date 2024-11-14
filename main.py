# file=open("abc.txt","r")
# # print(file.read(10))

# # print(file.readline())
# # print(file.readline())
# for line in file:
#     print(line1)
file1=open("abc.txt","r")
file2=open("xyz.txt","w")

for line in file1.readlines():
      if not (line.startswith("coding")):
        print(line)  

        file2.write(line)
file1.close()
file2.close()
str1="i'm umar farooq"
length=len(str1)
print(length)
print(str1[9])
slice1=str1[5:9]
print(slice1)
print(str1.endswith("oq"))
str1.capitalize()#does't change the old string for permanant change store the string in original
str1=str1.capitalize()
str1= str1.replace("farooq","faruq")
print(str1)
print(str1.find("f")) #return index of first occurence of what we searching for
print(str1.count("a"))
str2=input("name : ")
print(len(str2))
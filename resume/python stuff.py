
# while True:
#     word = input("Enter a word: ")
#     times = int(input("Enter how many times to repeat: "))
#     if times >0:
#         break
#     print("Please enter a positive number for repetitions.")

# for i in range(1, times+1):
#     print(word)

# str=input("enter a word")
# if str==str[::-1]:
#     print("pali")
# else :
#     print("not")

# adjectivel = input ( "Enter an place name (description) : ")
# nounl = input("Enter (person, place, thing) : ") 
# adjective2 = input ("Enter an expression (happy,sad,arogant,etc): ") 
# verbl = input("Enter a verb ending with 'ing'") 
# adjective3 = input("Enter an expression : ")

# print (f" Today I went to a {adjectivel } at benglore")
# print (f"In an zoo exhibit, I saw a {nounl}" ) 
# print (f" {nounl} was {adjective2} and {verbl}")
# print (f"I was so {adjective3}")

# num= int(input("enetr num :"))
# print("positive" if num>=0 else "negative")
# name=input("enter name :")
# result=len(name)
# print(f"your name is of { result} no of words")


# name=str(input("give string: "))
# string=name[::-1]
# print(string)


# s1=int(input("enter no "))
# s2=int(input("enter no "))
# s3=int(input("enter no "))
# if s1==s2==s3:
#     print("equilateral triangle")
# elif s1+s2==s3 or s2+s3==s1 or s1+s3==s2:
#     print("isosceles triangle")
# else:
#     print("scallin triangle")
    

# rating=float(input("enter ratings : "))
# salary=int(input("enter salary:"))
# if rating>=4.5:
#     print(salary*0.30 ,"is your bonus")
# elif 4.0 <=rating<4.49:
#     print(salary*0.20 ,"is your bonus")
# elif 3.5 <=rating<3.99:
#     print(salary*0.10 ,"is your bonus")
# elif rating < 3.0:
#     print("no bonus")

score=int(input("enter no :"))
if 90<=score<=100:
    print("A grade")
elif 80<=score<=89:
    print("B grade")
elif 70<=score<=79:
    print("C grade")
elif 60<=score<=69:
    print("D grade")
elif 0>=score<=59:
    print("F grade")    
else:
    print("invalid")
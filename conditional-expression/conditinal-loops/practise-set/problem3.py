# write an program a spam comment is text defineing as text containsfollwing key words  "make a lot of money" , "buy now" ,"click this" , "subscribe now"

p1 = "make a lot of money" 
p2 =  "buy now"
p3 = "click this"
p4 = "subscribe now"


message = input("Enter Your commnet: ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this comment is the spam ")

else:
    print("this comment not spam")


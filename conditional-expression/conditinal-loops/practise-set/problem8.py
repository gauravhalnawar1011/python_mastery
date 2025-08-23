# write an program to find out the the given post talking about the devops or not 

post = input("Enter Your Post: ")

if ("Devops".lower() in post.lower()):
    print("This post talking about the devops:")
else:
    print("this post is not talking about the devops")
# Write an Python function to remove given word from list ad strip in at same time 


# def rem(l,word):
#     for item in l:
#          n= []
#          if not(item == word):
#               n.append(item.strip(word))
#     return n

# l = ["Gaurav", "Shubham", "Ankit", "yash", "sh"]

# print(rem(l,"sh"))


def rem(l, word):
    n = []   # keep outside the loop
    for item in l:
        if item != word:  # skip if it's exactly the word
            n.append(item.replace(word, "").strip())  
    return n

l = ["Gaurav", "Shubham", "Ankit", "yash", "sh"]

print(rem(l, "sh"))

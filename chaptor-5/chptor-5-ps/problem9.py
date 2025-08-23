# can you chnage the values in list which is inside the set

# s = {8.7,12,"Devops",[1,2]} # TypeError: unhashable type: 'list'

#Because sets can only contain hashable (immutable) elements. Lists are mutable, so they can’t be part of a set.


#we can not update it we can not include list inside the set 

# we can not chnae vaalues via indexing in set 

# but we can use the tuple which immutable 


s = {8.7, 12, "Devops", (1,2)}

# Remove (1,2) and add (0,2)
s.remove((1,2))
s.add((0,2))

print(s)  # {8.7, 12, 'Devops', (0,2)}

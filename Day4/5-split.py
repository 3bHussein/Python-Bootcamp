import random
name = input("enter names ")


splits = name.split()
lens = len(splits)
rn_split_name = random.randrange(0, lens)
t = int(rn_split_name)
print(splits[t])



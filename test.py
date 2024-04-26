value = [1,2,3,4,5,6]
weights = [10,10,10,10,10,50]
values = []
for val in range(len(value)):
  for num in range(weights[val]):
    values.append(value[val])

print(values)


#!DICE goblin 1:10,2:30,3:60
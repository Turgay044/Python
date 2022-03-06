input=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output = []
def flatten(data):
    for i in data:
        if type(i) == list:
            flatten(i)
        else:
            output.append(i)
flatten(input)
print("input : " + str(input))
print("output : " + str(output))
print()

def flattens(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flattens(list_of_lists[0]) + flattens(list_of_lists[1:])
    return list_of_lists[:1] + flattens(list_of_lists[1:])

out = flattens(input)
print("input : " + str(input))
print("output : " + str(out))
print()

input1=[[1, 2], [3, 4], [5, 6, 7]]
output1=[]
for i in sorted(input1,reverse = True):
    output1.append(sorted(i, reverse = True))
print("input : " + str(input1))
print("output : " + str(output1))


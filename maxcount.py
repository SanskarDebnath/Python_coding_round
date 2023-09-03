num = ['1','2','3','1','4','1','2','1','5','6','1']
most = max(num)

print(most) #it search the max number from a python list


most2 = max(num, key=num.count)
print(most2) # it will serach that value which is mostly used in this list

#for more optimization we will set this like this
#most2 = max(set(num), key=num.count)


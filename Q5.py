# creates the empty list 
l1 = [] 
  
#variable to store numbers in list
num1 = int(input("Please enter maximum number in you want to update in list: ")) 
  
# for loop for storing number in list
for i in range(1, num1 + 1): 
    newNum = int(input("Please enter elements: ")) 
    l1.append(newNum) 
      
# print largest number
print("Largest element is:", max(l1))
# for i in range(0,1):
#     print(i)
################################################


# Create a list in a range of 10-20 
My_list1 = list(map(str, range(3)))

# ', '.join("'" + item + "'" for item in color_list
# My_list1 = ', '.join("'" + item + "'" for item in range(4)

# Print the list 
print(My_list1) 



################################################
# Create an empty list 
My_list = [] 
  
# Value to begin and end with 
start, end = 10, 20
  
# Check if start value is smaller than end value 
if start < end: 
    # unpack the result 
    My_list.extend(range(start, end)) 
    # Append the last value 
    My_list.append(end) 
  
# Print the list 
print(My_list) 
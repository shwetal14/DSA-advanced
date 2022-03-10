#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1.  Implement Binary Search.




def binary_search(item_list,item):
    first = 0
    last = len(item_list)-1
    found = False
    while( first<=last and not found):
   mid = (first + last)//2
   if item_list[mid] == item :
        found = True
   else:
        if item < item_list[mid]:
           last = mid - 1
       else:
           first = mid + 1
    return found

print(binary_search([1,2,3,5,8], 5))


  # 2. Implement Merge Sort



def mergeSort(myList):
    if len(myList) > 1:
   mid = len(myList) // 2
   left = myList[:mid]
   right = myList[mid:]

   mergeSort(left)
   mergeSort(right)

   # Two iterators for traversing the two halves
   i = 0
   j = 0
   
   # Iterator for the main list
   k = 0
   
   while i < len(left) and j < len(right):
       if left[i] <= right[j]:
         # The value from the left half has been used
         myList[k] = left[i]
         # Move the iterator forward
         i += 1
       else:
           myList[k] = right[j]
           j += 1
       # Move to the next slot
       k += 1

   # For all the remaining values
   while i < len(left):
       myList[k] = left[i]
       i += 1
       k += 1

   while j < len(right):
       myList[k]=right[j]
       j += 1
       k += 1

myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)



# 3. Implement Quick Sort



def QuickSort(array):

    elements = len(array)
    
    if elements < 2:
   return array
    
    current_position = 0

    for i in range(1, elements): 
    if array[i] <= array[0]:
           current_position += 1
           temp = array[i]
           array[i] = array[current_position]
           array[current_position] = temp

    temp = array[0]
    array[0] = array[current_position] 
    array[current_position] = temp 
    
    left = QuickSort(array[0:current_position]) 
    right = QuickSort(array[current_position+1:elements]) 

    array = left + [array[current_position]] + right 
    
    return array

array_to_be_sorted = [4,2,7,3,1,6]
print("Original Array: ",array_to_be_sorted)
print("Sorted Array: ",QuickSort(array_to_be_sorted)





# 4. Implement Insertion Sort
 
   def insertionSort(array):
   for i in range(1, len(array)):
 key = array[i]
 j = i-1
 while j >=0 and key < arr[j] :
    array[j+1] = arr[j]
    j -= 1
 array[j+1] = key

array = ['t','u','t','o','r','i','a','l']
insertionSort(array)
print ("The sorted array is:")
for i in range(len(array)):
   print (array[i])
   
 
 
 
# 5. Write a program to sort list of strings (similar to that of dictionary)



def main():
    
    #List Of Strings
    listOfStrings = ['hi' , 'hello', 'at', 'those', 'there', 'from']
    
    print(listOfStrings)
    
    
    Sort List of string alphabetically
    
    listOfStrings.sort()
    
    # Print the list
    print(listOfStrings)
    
    
    Sort List of string alphabetically in Reverse Order
    
    listOfStrings.sort(reverse=True)
    
    print(listOfStrings)
    
    Sort List of string by Length by using len() as custom key function 
    
    listOfStrings.sort(key=len)
    
    print(listOfStrings)
    
    
    Sort List of string by Numeric Order
    
    listOfNum = ['55' , '101', '155', '98', '245', '30', '67']
    
    # It will sort in alphabetical order
    listOfNum.sort()
    
    print(listOfNum)
    
    
   Sort in Ascending numeric order, pass key function that should convert string to integer i.e using int()
    
    listOfNum.sort(key=int)
    
    print(listOfNum)
    
    
    Sort in Descending numeric order, pass reverse flag along with key function
    
    
    listOfNum.sort(reverse=True, key=int)
    
    
    print(listOfNum)
    
    
if __name__ == '__main__':
    main()   
 
   


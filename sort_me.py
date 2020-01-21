import numpy as np

'''Can apply to anything that needs to be 
ordered, even dates if presented in correct format'''

nums = [1,3,4,7,5,2,6,9,8]


def select_sort(arr):        


    for i in range(len(arr)):
        minimum = i
        

        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j


        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
    
    
    return arr

print(select_sort(nums))

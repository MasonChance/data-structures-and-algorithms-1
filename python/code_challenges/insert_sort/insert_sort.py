# InsertionSort(int[] arr)
# === one input: an array of Int elements ====

    # FOR i = 1 to arr.length
    #  ^^^ instantiate a for loop on the arr argument starting at index one (exclude index 0)
    #   int j <-- i - 1
    # ^^^ assign variable j to value of current index - 1 (starts at 0)
    #   int temp <-- arr[i]
    # ^^^ store current index
    #   WHILE j >= 0 AND temp < arr[j]
    # ^^^ check if J is greater==0 and current is less than the array element at J^^^
    #     arr[j + 1] <-- arr[j] 
    # ^^^ reassign array at J + 1 to the value of array at J.
    #     j <-- j - 1
    # ^^^ re-assign j to j - 1
    #   arr[j + 1] <-- temp
    # ^^^ re-assign J + 1 to current index stored in temp. 

def insert_sort(arr: list):
    



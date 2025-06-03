def count_frequency(arr):
    
    hash_array = {}
    
    for el in arr:
        if el in hash_array:
            hash_array[el]+=1
        else:
            hash_array[el] = 1
    
    for ele in hash_array:
        print(f"{ele}:{hash_array[ele]}")



if __name__ == '__main__':
    arr = [10,5,5,5,5,5,5,5,5,5,5,10,15,10,5,5,10,15,10,5,10,10,5,10,15,10,5]
    count_frequency(arr)
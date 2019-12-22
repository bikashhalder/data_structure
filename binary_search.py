data = [1,2,3,4,5,6,8,9,20,29,30,50,56,78,98,99]
target = 20

#linear search
def linear_search(data,target):
    for i in range(len(data)):
        if data[i] == target:
            return True  
    return False 
print(linear_search(data,target))

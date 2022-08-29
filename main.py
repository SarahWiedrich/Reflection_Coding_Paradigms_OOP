#Initialize array     
my_array = [[1,2], [6,5,4], [9,12,10,11]]

flatten_list = []

# flatten array
for nums in my_array:
    for num in nums:
        flatten_list.append(num)
print(flatten_list)

arr = flatten_list;     
base = 0;    
     
#Displaying elements of original array    
print("Elements of original array: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
     
#Sort the array in ascending order    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] > arr[j]):    
            base = arr[i];    
            arr[i] = arr[j];    
            arr[j] = base;    
     
print();    
     
#Displaying elements of the array after sorting    
    
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" "); 

# OOP
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = ["perfect", "trashed", "repaired"]
        self.price = price

    def repair(self, condition):
        return self.condition[2]

class AnakinsPod(Podracer):
    def __init__(self):
        super().__init__()

    def boost(max_speed):
       speed = max_speed * 2
    return speed

class SebulbasPod(Podracer):
    def __init__(self):
        super().__init__()

    def  flame_jet(self, condition):
        return self.condition[1]

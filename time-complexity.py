# Contant

x = 10 #assignment operation

y = x *2 #math operation

if y > 5:
    print('yes')

def double_even(num): #Accepts an int, if it is even, double it
    if num%2 == 0: #comparison operator
        return num *2;#math operation
    else:
        print('nothing')

print(double_even(100))

# Logarithmic

#Binary Search Stay tuned
# But essentially just has to do with continuously cutting your graph in half until you either reach your target or you completely exhausted your graph, and you're down to the last portion of it


# Linear: Operations for piece of data pumped in

def double_evens(list):
    output = []  #Constant Time Complexity

    for num in list: #This for loop requires my solution to do an operation for each piece of data I input.
        # For loop: Linear Time Complexity
        if num%2 == 0: #Constant Time Complexity
            output.append(num*2)#Constant Time Complexity
    return output;

nums = [1,2,3,4,5,6,7,8,9,10]

print(double_evens(nums))





def double_split(list): #Stacked for loops is linear operation has negligible effect on time complexity
    #And nested loops makes it quadratic
    evens = []
    odds = []

    for num in list:
        if num%2==0:
            evens.append(num*2)
    
    for num in list:
        if num%2==1:
            odds.append(num*2)

    return(evens, odds)


def searcher(list, target): #Time complexity is determined by the worse-case scenario
    for num in list:
        if num == target:
            return "Target Aquired"
        
list = [1,2,3,4,5]
target = 1

print(searcher(list, target))



# Linear Logarithmic O(n logn)
def largest(list):
    sorted_list = sorted(list)#automatically becomes a O(n logn) solution

    largest = sorted_list[-1] # Selects the last element in the list

    return largest

print(largest([23,90,44,64,78,83]))





def highest_count(list):
    highest_counter = 0
    high_num = 0

    for num in list: #.count function is a loop under the hood and its in a for loop, hence its the same as nesting for loops
        if list.count(num) > highest_counter:
            high_num = num
            highest_counter= list.count(num)
    return high_num

alist = [1,1,1,1,2,2,2,3,3,3,3,3,4,5]
print(highest_count(alist))


#Be careful built in functions, a lot of them use for loops

def counter(self, target):
    count = 0;
    for num in self:
        if num == target:
            count+=1
    return count
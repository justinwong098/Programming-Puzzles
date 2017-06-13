
def get_input_lists():
    T = int(input())
    all_lists = []
    for entry in range(T):
        size = int(input())
        unsorted_list = list(map(int, input().split(" ")))        
        all_lists.append(unsorted_list)
    return all_lists

def count_shifts(lists):
    for lst in lists:
        num_shifts = 0
        for i in range(1,len(lst)):    #since we want to swap an item with previous one, we start from 1
            j = i                    #bcoz reducing i directly will mess our for loop, so we reduce its copy j instead
            while j > 0 and lst[j] < lst[j-1]: #j>0 bcoz no point going till k[0] since there is no value to its left to be swapped
                lst[j], lst[j-1] = lst[j-1], lst[j] #syntactic sugar: swap the items, if right one is smaller.
                j=j-1 #take k[j] all the way left to the place where it has a smaller/no value to its left.
                num_shifts += 1
        print(num_shifts)
    
    

count_shifts(get_input_lists())

  
    

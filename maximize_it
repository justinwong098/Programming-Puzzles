# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput

input = [];
for line in fileinput.input():
    li = map(int, line.split());
    input.append(li);    
    pass

M = input[0][1];

listoflists = input[1:]
for li in listoflists:
    li.pop(0);
    
## ListOfList -> ListOfList
## produces a list of list of numbers, 
## all combinations of one from each list
def getAllCombos(lists):  
    result = [];
    firstList = lists[0];
    if(len(lists) == 1):
        for item in firstList:
            result.append([item]);
        return result;
    else:        
        rest = lists[1:];
        nextLayer = getAllCombos(rest);
        for item in firstList:            
            currentLayer = map(lambda x: [item] + x, nextLayer);            
            result.extend(currentLayer);            
        return result;   


maxResult = 0;
for loi in getAllCombos(listoflists):    
    listOfSquares = map(lambda x: x ** 2, loi);
    result = sum(listOfSquares) % M;
    if (result > maxResult):
        maxResult = result;

print maxResult

    

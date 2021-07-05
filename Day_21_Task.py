#Day 21
# Gokul Dhakshana Murthy

#1. program using zip() fn and list() func = create a merged list of tuples from the two lists given

def FUNC1(List1, List2):
    print(list(zip(List1, List2)))

#2. First create a range from 1 to 8 then using zip  - merge the given list and the range together to create a new list of tuples 
def FUNC2(List2):
    print(list(zip(List2, range(1, 9))))

#3. Using a sorted() func - sort the list in ascending order
def FUNC3(LIST):
    print(sorted(LIST))

#4. program using filter function - filter the even numbers so that only odd numbers are passed to the new list
def FUNC4(LIST):
    print(list(filter(lambda x : x%2 != 0, LIST)))

if __name__ == '__main__':
    List1 = [342, 217, 1111, 439, 30]
    List2 = [71, 72, 73, 74, 75, 76, 77, 78]
    FUNC1(List1, List2)
    FUNC2(List2)
    FUNC3(List1)
    FUNC4(List1)

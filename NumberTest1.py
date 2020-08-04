
# 对数据类型的一些认识及一些简单操作
# 输出数据类型
# 数量自身的一些计算语法

def NumberTest():
    x = 3
    print("大鹏")
    print (type(x)) # Prints "<type 'int'>"
    print(x)
    print (x + 1)
    x *=2
    y=2.5
    print(type(y))
    print(x)
    a="dapeng"
    b="xiaoxiong"
    print(a+"  "+b)
    str1='%s %s %s'%(a,b,12)
    print(str1)
    pass

# 容器类
# 列表（lists）、字典（dictionaries）、集合（sets）和元组（tuples）

#简单的list容器
def Lists():
    a=["a","b","c","d"]
    print(a);
    print(a[-2])
    # b=a.pop(1)
    # print(a)
    # print(b)
    print(a[0])
    c = a[1:4]
    print(c)
    pass

# list下的一些切片操作
def Slicing():
    nums = list(range(5))  # range is a built-in function that creates a list of integers
    print(nums)  # Prints "[0, 1, 2, 3, 4]"
    print(nums[2:4])  # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
    print(nums[2:])  # Get a slice from index 2 to the end; prints "[2, 3, 4]"
    print(nums[:2])  # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
    print(nums[:]) # Get a slice of the whole list; prints ["0, 1, 2, 3, 4]"
    print(nums[:-1])  # Slice indices can be negative; prints ["0, 1, 2, 3]"
    nums[2:4] = [8, 9]  # Assign a new sublist to a slice
    print(nums)
    pass

# 对数组指针的引用
def Loops():
    animals = ['cat', 'dog', 'monkey']
    for idx, animal in enumerate(animals):
        print('%d: %s' % (idx + 1, animal))
    # Prints "#1: cat", "#2: dog", "#3: monkey
    pass


# 列表推导 常用于将一个数组中的数据类型转化为另外一种 或者列表内的数据进行更换
def LoopsAppend():
    num1=list(range(5))
    num2=[x**2 for x in num1]
    # 列表推导中也可以包含条件
    num3=[x for x in num1 if x%2==0]
    print(num3)
    print(num2)
    pass

# 字典 可以存储key value 和java中map差不多
def Dictionaries():
    d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
    print(d['cat'])  # Get an entry from a dictionary; prints "cute"
    print('cat' in d)  # Check if a dictionary has a given key; prints "True"
    d['fish'] = 'wet'  # Set an entry in a dictionary
    print ("fish"+d['fish'] ) # Prints "wet"
    # print d['monkey']  # KeyError: 'monkey' not a key of d
    print(d.get('monkey',"dpp"))
    print(d.get('monkey', 'N/A') ) # Get an element with a default; prints "N/A"
    print(d.get('fish', 'N/A'))  # Get an element with a default; prints "wet"
    del d['fish']  # Remove an element from a dictionary
    print(d.get('fish', 'N/A'))  # "fish" is no longer a key; prints "N/A"
    pass
    return

# 字典循环
def DictionariesLoops():
    d = {'person': 2, 'cat': 4, 'spider': 8}
    for animal in d:
        legs = d[animal]
        print('A %s has %d legs' % (animal, legs))
    # Prints "A person has 2 legs", "A spider has 8 legs", "A cat has 4 legs"
    pass

# 字典推导，可以对字典的内容进行推导，像数组一样
def Dictionarycomprehensions():
    nums = [0, 1, 2, 3, 4]
    even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
    print(even_num_to_square)
    pass


# 集合SETS
# set是一个不同个体的无序集合 （值都是唯一的，有新的元素进来时如果有重复的则替换）
def Sets():
    animals = {'cat', 'dog'}
    print('cat' in animals)  # Check if an element is in a set; prints "True"
    print('fish' in animals ) # prints "False"
    animals.add('fish')  # Add an element to a set
    print('fish' in animals ) # Prints "True"
    print(len(animals))  # Number of elements in a set; prints "3"
    animals.add('cat')  # Adding an element that is already in the set does nothing
    print(len(animals))  # Prints "3"
    animals.remove('cat')  # Remove an element from a set
    print(len(animals))  # Prints "2"
    pass


def SetsLoops():
    lsit1= list(range(5))
    set1= {x for x in lsit1}
    for index , items in enumerate(set1):
        print(index+1,items)
        pass
    print(set1)
    pass
from math import sqrt


# set的循环 以及 推导
def SetsLoops():
    lsit1 = list(range(5))
    set1 = {x for x in lsit1}
    set2 = {int(sqrt(x)) for x in list(range(300))}
    print(set2)
    pass



# 元祖
# 元祖是一个有序的列表，和列表很相似，但是元祖可以用作键，可以作为集合的元素，但是列表不行
def Tuples():
    d = {(x,x+3) : x for x in range(10)};
    print(d)
    pass


if __name__ == '__main__':
    Tuples()

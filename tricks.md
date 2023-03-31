# 数据结构

## 字符串

### 1 去除非数字、非字母

```python
s = 'Colour Temperature is 2700 Kelvin'
```

#### 保留数字

```python
''.join(filter(str.isdigit, s))
```

输出

```
'2700'
```

#### 保留字母

```python
''.join(filter(str.isalpha, s))
```

```python
re.sub(r'[^a-zA-Z]', "", s)
```

输出

```
'ColourTemperatureisKelvin'
```

#### 保留字母和数字

```python
''.join(filter(str.isalnum, s))
re.sub(r'[\W_]',"",s)
re.sub(r'[^a-zA-Z0-9]',"",s)
```

输出

```
'ColourTemperatureis2700Kelvin'
```

### 2 字母ASCII码

0-9: 48-57

a-z: 97-122

A-Z: 65-90

#### 字符转ASCII码

```python
ord('a')
```

输出

```
97
```

#### ASCII码转字符

```python
chr(48)
```

输出

```
'0'
```

## 列表

### 1 字符串转为列表

```python
from ast import literal_eval
strs = literal_eval("[1,2,3,4]")
strs
```

输出

```
[1, 2, 3, 4]
```

### 2 生成随机数

```python
random.randint(n,m) #生成一个n到m之间的随机数
random.random()  #生成一个0到1之间的浮点数
random.uniform(n,m) #生成一个n到m之间的浮点数
random.choice([])  #从列表之间随机选取一个数
```

## 链表

## 堆栈

### 1 小顶堆

```python

```

## 字典

带默认值的字典

```python
from collections import defaultdict
s = defaultdict(int)
s[0]
# 0
```

# 基本算法

## 排序

### 1 冒泡排序

# 常用方法库

## map 函数

```python
map(function, iterable, ...)
```

- function -- 函数
- iterable -- 一个或多个序列

例:

```python
>>> list(map(str,range(10)))
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

>>> list(map(pow,range(10),range(10)))
[1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]

>>> list(map(lambda x,y:x+y ,range(10),range(10)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

>>> def f(a,b,c):
...   return a+b+c
>>> list(map(f,range(10),range(10),it.repeat(1)))  
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

## lambda 表达式

### 概念

匿名函数 `lambda`：是指一类无需定义标识符（函数名）的函数或子程序。所谓匿名函数，通俗地说就是没有名字的函数，`lambda`函数**没有名字**，是一种**简单的**、**在同一行中定义函数**的方法。

* `lambda`函数一般功能简单：单行expression决定了`lambda`函数不可能完成复杂的逻辑，只能完成非常简单的功能。由于其实现的功能一目了然，甚至不需要专门的名字来说明。

* `lambda` 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。

* `lambda` 表达式只允许**包含一个表达式**，不能包含复杂语句，该**表达式的运算结果**就是**函数的返回值**。

* `lambda` 函数实际生成了一个`lambda`对象。

### 语法

`lambda`表达式的基本语法如下：

` lambda arg1,arg2,arg3… :<表达式>`

arg1/arg2/arg3为函数的**参数（函数输入）**，表达式相当于**函数体**，运算结果是表达式的运算结果。

例如：

` lambda x, y: x*y`；函数输入是x和y，输出是它们的积x*y

`lambda:None`；函数没有输入参数，输出是None

`lambda *args: sum(args)`; 输入是任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)

`lambda **kwargs: 1`；输入是任意键值对参数，输出是1

```python3
#测试lambda函数
f=lambda a,b,c,d:a*b*c*d
print(f(1,2,3,4))  #相当于下面这个函数
def test01(a,b,c,d):
    return a*b*c*d
print(test01(1,2,3,4))


g=[lambda a:a*2,lambda b:b*3]
print(g[0](5))  #调用
print(g[1](6))
```

### 扩展用法

由于 `lambda`语法是固定的，其本质上只有一种用法，那就是定义一个 `lambda`函数。在实际中，根据这个 `lambda`函数应用场景的不同，可以将 `lambda`函数的用法扩展为以下几种：

**1.将 `lambda`函数赋值给一个变量，通过这个变量间接调用该 `lambda`函数。**

**2.将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换。**

**3.将lambda函数作为参数传递给其他函数。**

### 内置函数接受函数传参

**部分Python内置函数接受函数作为参数**,典型的**此类内置函数有**这些:



* **filter函数** 此时lambda函数用于指定过滤列表元素的条件。例如filter(lambda x: x % 3 == 0, [1, 2, 3])指定将列表[1,2,3]中能够被3整除的元素过滤出来，其结果是[3]。

* **sorted函数** 此时lambda函数用于指定对列表中所有元素进行排序的准则。例如sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]按照元素与5距离从小到大进行排序，其结果是[5, 4, 6, 3, 7, 2, 8, 1, 9]。

* **map函数** 此时lambda函数用于指定对列表中每一个元素的共同操作。例如map(lambda x: x+1, [1, 2,3])将列表[1, 2, 3]中的元素分别加1，其结果[2, 3, 4]。

* **reduce函数** 此时lambda函数用于指定列表中两两相邻元素的结合条件。例如reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])将列表 [1, 2, 3, 4, 5, 6, 7, 8, 9]中的元素从左往右两两以逗号分隔的字符的形式依次结合起来，其结果是'1, 2, 3, 4, 5, 6, 7, 8, 9'。

另外，部分Python库函数也接收函数作为参数，例如gevent的spawn函数。此时，lambda函数也能够作为参数传入。

## itertools 库

```python
import itertools as it
```

### 1 Infinite iterators

> Make an iterator that returns evenly spaced values starting with number start. Often used as an argument to map() to generate consecutive data points. Also, used with zip() to add sequence numbers. 

创建一个能生成均匀分布序列（或者说等差数列）的迭代器，start指定起点，step指定步长。start, step不限于浮点数。注意，count()生成的是无限序列迭代器，所以用于循环中时，需要另外的条件来控制循环的终止。

#### count

`count(start=0, step=1)`

```python
k = 0
for item in it.count(10.7,1.1):
    k += 1
    if k == 10 : break    
    print('k={0}, item={1})'.format(k,item))
```

```
k=1, item=10.7)
k=2, item=11.799999999999999)
k=3, item=12.899999999999999)
k=4, item=13.999999999999998)
k=5, item=15.099999999999998)
k=6, item=16.2)
k=7, item=17.3)
k=8, item=18.400000000000002)
k=9, item=19.500000000000004)
```

> When counting with floating point numbers, better accuracy can sometimes be achieved by substituting multiplicative code such as: `start + step * i for i in count()`.

如以上例子所示，如果step为浮点数时，改用`start + step * i for i in count()`可能能获得更好的精度。如下例所示。

```python
for k in it.count(0):
    item = 10.7 + 1.1 * k
    if k == 10 : 
        break    
    print('k={0}, item={1})'.format(k,item))  
```

```
k=0, item=10.7)
k=1, item=11.799999999999999)
k=2, item=12.899999999999999)
k=3, item=14.0)
k=4, item=15.1)
k=5, item=16.2)
k=6, item=17.3)
k=7, item=18.4)
k=8, item=19.5)
k=9, item=20.6)
```

#### cycle

`cycle(iterable)`

> Make an iterator returning elements from the iterable and saving a copy of each. When the iterable is exhausted, return elements from the saved copy. Repeats indefinitely.


创建一个迭代器，从一个iterable中循环取出元素并输出。以下例子会输出比如：ABCDEABCDE...

```python
k = 0
for item in it.cycle('ABCDE'):
    print('k={0}, item={1}'.format(k,item))      
    k += 1
    if k == 10 : break    
```
```
k=0, item=A
k=1, item=B
k=2, item=C
k=3, item=D
k=4, item=E
k=5, item=A
k=6, item=B
k=7, item=C
k=8, item=D
k=9, item=E
```
> Note, this member of the toolkit may require significant auxiliary storage (depending on the length of the iterable).

需要注意的是，该迭代器会将从输入iterable中取出的元素存储一份copy，在第一遍遍历完iterable后，是从copy中循环取出元素并输出。所以需要一份额外的存储空间。

#### repeat

`repeat(object[, times])`

> Make an iterator that returns object over and over again. Runs indefinitely unless the times argument is specified. Used as argument to map() for invariant parameters to the called function. Also used with zip() to create an invariant part of a tuple record.

创建迭代器，重复输出object。如果未指定times会无限输出，如果指定了times则重复输出指定次数。

```python
for item in it.repeat('Do not answer!',3):
    print('{0}'.format(item)) 
```

> A common use for repeat is to supply a stream of constant values to map or zip.

 一个典型的用法是用于给map或者zip提供一个常数值串，如下所示：

```python
>>> list(map(pow, range(12), it.repeat(2)))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
>>> list(zip(range(12), it.repeat(2)))      
[(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2)]
```

### 2 Iterators terminating on the shortest input sequence

#### accumulate

`accumulate(iterable[, func, *, initial=None])`

> Make an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument).

生成能够返回输入iterable参数的部分和的迭代器。

```python
list(it.accumulate([1,2,3,4,5]))
```

```
[1, 3, 6, 10, 15]
```

以上语句将输出[1,3,6,10,15]，即原输入[1,2,3,4,5]的滚动和(running sum). 利用这个功能可以很方便地生成级数.

缺省情况下是进行求和运算，但是并不仅限于此，用func可以指定想执行的运算（当然必须是二元的数值运算符），比如说，如果想要求running product的话，如下例所示：

```python
import operator
list(it.accumulate([1,2,3,4,5],operator.mul)) 
```

```
[1, 2, 6, 24, 120]
```

以上语句将输出[1,2,6,24,120]。利用这个功能可以很方便地生成级数.

缺省情况下如上所示，输出的个数等于输入的个数。但是如果通过参数initial指定初始值的话，第一个输出是由initial指定，然后才是running result，因此输出会比输入多出一个来。如下例所示：

```python
list(it.accumulate([1,2,3,4,5],initial=10))
```

```
[10, 11, 13, 16, 20, 25]
```

以上语句将返回：[10, 11, 13, 16, 20, 25]。第一个值为initial，其后才是以initial为基础的running sum.

#### chain

`chain(*iterables)`

> Make an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next iterable, until all of the iterables are exhausted. Used for treating consecutive sequences as a single sequence. 

创建一个迭代器，接收多个iterables参数，将它们串接起来，然后进行遍历。比如：

```python
list(it.chain('ABCD','EFG','HIJ'))
```

```
 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
```

注意，和上面几个例子以上，这里采用了用list(iterator)的方式将iterator转换成list。

#### compress

`compress(data, selectors)`

> Make an iterator that filters elements from data returning only those that have a corresponding element in selectors that evaluates to True. Stops when either the data or selectors iterables has been exhausted. Roughly equivalent to:

根据selectors所列的各元素对原数据进行滤波处理，挑选出对应的selectors元素为True的data元素。selectors与data的元素是一一对应的。

```python
list(it.compress('ABCDEFG', [0,0,1,0,0,1,1]))
```


只有selector参数中1所对应的data的元素才被选中输出。

#### dropwhile

#### filterfalse

#### groupby

#### islice

`islice(iterable, stop)`
`islice(iterable, start, stop[, step])`

> Make an iterator that returns selected elements from the iterable. If start is non-zero, then elements from the iterable are skipped until start is reached. Afterward, elements are returned consecutively unless step is set higher than one which results in items being skipped. If stop is None, then iteration continues until the iterator is exhausted, if at all; otherwise, it stops at the specified position. Unlike regular slicing, islice() does not support negative values for start, stop, or step. Can be used to extract related fields from data where the internal structure has been flattened (for example, a multi-line report may list a name field on every third line). 

以slicing的方式从一个可迭代对象(iterable)种取元素并输出。可以把islice()理解为升级版的range()，range()就是islice的第1个iterable参数设为一个连续整数序列时的行为相同。

第一种调用形式只指定一个参数，这个参数是stop，相当于取iterable[:stop]然后一个一个输出。

```python
>>> A = [k for k in range(10)]
>>> list(it.islice(A, 13))     
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
>>> A = [2,1,1,22,3,4,5]   
>>> list(it.islice(A, 3))  
[2, 1, 1]
```

第二种调用形式只指定两个或三个参数，第2个是start，第3个是stop，第4个step可选，如果不设置step的话，缺省为1。

```python
>>> list(it.islice(A,1,7,2)) 
[1, 22, 4]
```

#### starmap

#### takewhile

#### tee

#### zip_longest

`zip_longest(*iterables, fillvalue=None)`

> Make an iterator that aggregates elements from each of the iterables. If the iterables are of uneven length, missing values are filled-in with fillvalue. Iteration continues until the longest iterable is exhausted. 
> If one of the iterables is potentially infinite, then the zip_longest() function should be wrapped with something that limits the number of calls (for example islice() or takewhile()). If not specified, fillvalue defaults to None.

`itertools.zip_longest`可以看作是python内置的zip()的功能补充工具。zip在处理多个iterables的并行迭代时迭代次数是以其中长度最小的为准。但是在有些应用场合需要以其中长度最长的为准，`itertools.zip_longest`即是以解决这个问题而生。

```python
fruits = ['apple', 'banana', 'melon', 'strawberry']
prices = [10, 20, 30]
list(it.zip_longest(fruits, prices))
```

```
[('apple', 10), ('banana', 20), ('melon', 30), ('strawberry', None)]
```

由于prices的元素比fruits的少一个，所以python自动为fruits的最后一个元素'strawberry'配了一个None。当然如果你希望这里能给出更有参考意义的信息，那么可以通过可选参数fillvalue来指定，如下例所示：

```python
fruits = ['apple', 'banana', 'melon', 'strawberry']
prices = [10, 20, 30]
list(it.zip_longest(fruits, prices, fillvalue='Sold out'))
```

```
[('apple', 10), ('banana', 20), ('melon', 30), ('strawberry', 'Sold out')]
```


这样为'strawberry'配上了“Sold out(售罄，卖光了)”就显得自然多了。 关于zip与zip_longest的差异还可以参考： Python zip, unzip, zip_longest的用法

### 3 Combinatoric iterators

#### product

`product(*iterables, repeat=1)`

> Cartesian product of input iterables. Roughly equivalent to nested for-loops in a generator expression. For  example, product(A, B) returns the same as ((x,y) for x in A for y in B).

生成输入各iterable（分别看作一个集合）的笛卡尔积.大致等价于生成器表达式中的嵌套循环。最右侧的iterable处于最内层循环，最左侧的iterable处于最外层循环。打个比方说，如果输入有三个iterable，product(A,B,C)，则C可以看作是秒针，B可以看作是分针，A可以看作是时针。或者C是里程计的最右侧读数，而A是最左侧读数。

如果要计算一个iterable自身的笛卡尔积，可以通过repeat指定重复次数。比如说，product('ABC',repeat=4)等价于product('ABC','ABC','ABC','ABC').

it.product('AB','CD'):


print('\nproduct example 2 ...')
for item in it.product('AB', repeat=4):
    print(item)
Before product() runs, it completely consumes the input iterables, keeping pools of values in memory to generate the products. Accordingly, it is only useful with finite inputs.
product()是先把输入iteables全部保存到memory用于随后的生成。所以product()不能接收无限长的iterable作为参数。

4.2 permutations(iterable, r=None)
Return successive r length permutations of elements in the iterable.

If r is not specified or is None, then r defaults to the length of the iterable and all possible full-length permutations are generated.

The permutation tuples are emitted in lexicographic ordering according to the order of the input iterable. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Elements are treated as unique based on their position, not on their value. So if the input elements are unique, there will be no repeat values in each permutation.
返回p中任意取r个元素做排列的元组的迭代器. 注意，参数列表中的[,r]表示第2个参数是可选项。如果不设置的话，就缺省地取第一个参数的长度，此时返回的结果为全排列。

import itertools as it

for p in it.permutations(['a','b','c']): 
    # Has the same behaviour as the above statement    
    print(p, end=', ')

print('')
for p in it.permutations(['a','b','c'],2 ): 
    # Return any permutations of length 2
    print(p, end=', ')
运行结果:

        ('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a'), 
        ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b'), 

令输入iterable长度为n, 如果指定参数r<=n，则返回的排列数为；如果r>n返回0项。如果不指定r，则返回项。

4.3 combinations(iterable, r)
Return r length subsequences of elements from the input iterable.

The combination tuples are emitted in lexicographic ordering according to the order of the input iterable. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Elements are treated as unique based on their position, not on their value. So if the input elements are unique, there will be no repeat values in each combination.
返回输入iterable中元素的长度为r的组合。令输入iterable元素个数为n，则返回的组合数为

#### combinations
print('\ncombinations example1:')
for item in it.combinations(['A', 'B', 'C', 'D'], 2):
    print(item)
4.4 combinations_with_replacement(iterable, r)
Return r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

The combination tuples are emitted in lexicographic ordering according to the order of the input iterable. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Elements are treated as unique based on their position, not on their value. So if the input elements are unique, the generated combinations will also be unique.
与combinations()的区别在于允许同一元素重复取用。

#### combinations_with_replacement
print('\combinations_with_replacement example1:')
k = 0
for item in it.combinations_with_replacement(['A', 'B', 'C', 'D'], 3):
    print(item)
    k += 1
print('Totally there are {0} combinations'.format(k))    
n个不同元素的允许重复取用的r-组合数的闭式表达式是什么呢？值得思考一下。

5. itertools.pairwise() 
        pairwise()是从python3.10引入的一个方法。

        它用于按顺序返回一个iterable中每两个相邻的item构成的tuple的列表。注意，不是任意items两两成对，只有相邻的两个成对，而且在tuple中的排序与在原iterable中的顺序相同。

    
    ​    

from itertools import pairwise

lst = [1,2,3,4,5]
print("Successive overlapping pairs - ", list(pairwise(lst)))

string = "hello educative"
print("Successive overlapping pairs of characters in a string- ", list(pairwise(string)))
        第一个例子返回的是： 

[(1, 2), (2, 3), (3, 4), (4, 5)]

        第二个例子返回的是：

 [('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o'), ('o', ' '), (' ', 'e'), ('e', 'd'), ('d', 'u'), ('u', 'c'), ('c', 'a'), ('a', 't'), ('t', 'i'), ('i', 'v'), ('v', 'e')]

Reference:
itertools — Functions creating iterators for efficient looping — Python 3.9.7 documentation

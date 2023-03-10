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

## 排序

### 1 冒泡排序


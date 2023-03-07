## 1 字符串

### 1.1 去除非数字、非字母

```python
s = 'Colour Temperature is 2700 Kelvin'
```

#### 保留数字

```python
''.join(filter(str.isdigit, s))
```

#### 保留字母

```python
''.join(filter(str.isalpha, s))
```

#### 保留字母和数字

```python
''.join(filter(str.isalnum, s))
```

```python
re.sub(r'[^a-zA-Z]', "", s)
```


### Adding items to the list in Python (with code snippets)

There are mainly 3 methods to add items to a Python list

1. append
2. extend
3. insert

#### 1. append
append method add the object to the end of the list

```
numbers = [1,2,3]
numbers.append(4)
print(numbers) # [1,2,3,4]

numbers.append(['Afiz', 10, 20])
print(numbers) # [1,2,3,4, ['Afiz', 10, 20]] 
```

#### 2. extend
extend takes iterator object and expands the list

```
numbers = [1,2,3]
numbers.extend([4,5,6])
print(numbers) # [1,2,3,4,5,6]

numbers.extend('Afiz') 
print(numbers) ] # [1,2,3,4,5,6,'A','f','i','z']
numbers.extend(100) # 🔥🔥 Error not allowed 
```

#### 3. insert

insert method add the item at the specific given position.

```
numbers = [1,2,3]
numbers.insert(1, 99)
print(numbers) # [1, 99, 2, 3]
```

# `break` statement: 
The `break` statement is used to exit or terminate the current loop prematurely. When the break statement is encountered, the program immediately exits the loop and resumes execution at the next statement after the loop.

Code examples:

Example 1: Breaking out of a loop based on a condition
```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)

```
Output: 
```
1
2
```
Explanation: In this example, the for loop iterates from 1 to 5. When i becomes 3, the break statement is executed, and the loop is terminated. 

Example 2: Breaking out of nested loops. 
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
        if j == 2:
            break
```
Output: 
```
1 1
1 2
2 1
2 2
3 1
3 2
```
Explanation: In this example, there are two nested for loops. When j becomes 2, the break statement is executed, and the inner loop is terminated. However, the outer loop continues its iterations.

# `continue` statement:  

The `continue` statement is used to skip the remaining code in the current iteration of a loop and move to the next iteration. When the `continue` statement is encountered, the program jumps to the next iteration without executing the remaining code inside the loop for that particular iteration.

Code examples:
Example 1: Skipping specific values in a loop 
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```
Output: 
```
1
2
4
5
```
Explanation: In this example, the for loop iterates from 1 to 5. When i becomes 3, the continue statement is executed, and the remaining code inside the loop is skipped for that iteration. As a result, the number 3 is not printed.

Example 2: Skipping even numbers in a loop
```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```
Output:
```
1
3
5
7
9
```
Explanation: In this example, the for loop iterates from 1 to 10. When i is an even number, the continue statement is executed, and the remaining code inside the loop is skipped for that iteration. As a result, only the odd numbers are printed.

####usage
pass the test array into the Computer object and call evaluate

```
    # eg - 
    lis = ['-214748364801','-214748364802']
    com_obj = Computer(lis)
    com_obj.evaluate()
```

### approach
each string 'x' can be converted into a hash function that returns some value such that <br>
if `x1 > x2`  then `f(x1) > f(x2)` <br>
where x1 & x2 are 2 strings and f(x) is special hash function. <br>

example of one such hash function can be-
let x be the string of length L
```
    f(x) = x[0] * L + x[1] * (L-1) + x[2] * (L-2) ......x[L-1] * 1
```
#### Time Complexity
N + 1024(worst case) * N + N (worst)

= 1026* N
= O(N)

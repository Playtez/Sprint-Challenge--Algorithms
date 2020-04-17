# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II
n = 5
f = 3

Suppose that you have an n-story building and plenty of eggs. 
  - building with 5 stories
  - infinite amount of eggs

Suppose also that an egg gets broken if it is thrown off floor f or higher, 
  - building has a floor f (3-floor)
  - if an egg is thrown from 3-floor or higher the egg breaks

and doesn't get broken if dropped off a floor less than floor f.
  - if the egg is thrown off of every floor less than 3-floor 
  - i.e. if dropped from 2-floor or 1-floor egg wont break

Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.
  - the value of the floor is found when
  - 

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

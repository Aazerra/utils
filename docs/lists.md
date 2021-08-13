# Lists

## chunks

Yield successive n-sized chunks from arr.

```python
from utils.lists import chunks

chunks([1, 2, 3, 4], 2)  # => [[1,2],[3,4]]
chunks([1, 2, 3], 2)  # => [[1,2],[3]]
chunks([1, 2], 2)  # => [[1,2]]
chunks([1], 2)  # => [[1]]
```

## take

Returns n element of the arr.

```python
from utils.lists import take

take([1, 2, 3, 4], 2)  # => [1,2]
take([1, 2], 2)  # => [1,2]
take([1], 2)  # => [1]
```

## sublists

Returns a list with sublists with length specified in n

```python
from utils.lists import sublists

sublists([x for x in range(1, 10)], 9, 2, 3)  # => [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], []]
sublists([x for x in range(1, 10)], 3, 2, 3)  # => [[1, 2, 3], [4, 5], [6, 7, 8]]
sublists([x for x in range(1, 11)], 1, 2, 3, 4)  # => [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
```

## flatten

Returns flatten list

```python
from utils.lists import flatten

flatten([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])  # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
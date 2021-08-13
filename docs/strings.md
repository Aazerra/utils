# Strings

## strip

Strip string <br>
if x is list it going to strip all members of the list<br>
if x is str its going to do strip on that string only

```python
from utils.strings import strip

strip("aazerra  ")  # => "aazerra"
strip(["aazerra  ", " Hi "])  # => ["aazerra", "Hi"]

```

## is_null_or_empty

check string is empty or None

```python
from utils.strings import is_null_or_empty

is_null_or_empty(None)  # => True
is_null_or_empty("")  # => True
is_null_or_empty("Hi")  # => False
```

## translate

translate character you given to what you want

```python
from utils.strings import translate

translate("123456", {
    "1": "2",
    "2": "3",
    "3": "4"
})  # => output: 234456
```


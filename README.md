# utils-aazerra
My common utility functions

## Install
```shell script
pip install utils-aazerra
```

## Persian
- convert_digits: convert english digits to persian digits
```python
from utils.persian import convert_digits
convert_digits("0987654321")    # => ۰۹۸۷۶۵۴۳۲۱
```    
## Strings
- is_null_or_empty: check string is empty or None
```python
from utils.strings import is_null_or_empty
is_null_or_empty(None)  # => True
is_null_or_empty("")    # => True
is_null_or_empty("Hi")  # => False
```
- translate: translate character you given to what you want
```python
from utils.strings import translate
translate("123456", {
    "1": "2",
    "2": "3",
    "3": "4"
}) # => output: 234456
```

## Lists
- chunks: Yield successive n-sized chunks from arr.
```python
from utils.lists import chunks
chunks([1,2,3,4], 2)  # => [[1,2],[3,4]]
chunks([1,2,3], 2)  # => [[1,2],[3]]
chunks([1,2], 2)  # => [[1,2]]
chunks([1], 2)  # => [[1]]
```
- take: Returns n element of the arr.
```python
from utils.lists import take
take([1,2,3,4], 2)  # => [1,2]
take([1,2], 2)  # => [1,2]
take([1], 2)  # => [1]
```

## Urls
- join: join url with paths and url queries
```python
from utils.url import join
join("www.sadtech.ir", "start", "?ok=true") # => 'www.sadtech.ir/start/?ok=true'
```

## To-do
- [ ] create documentation for all of the functions
- [ ] type checking
- [ ] add more functionality
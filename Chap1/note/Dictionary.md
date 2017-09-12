
# Dictionary
Dictionaries are another example of a data structure, and, like lists, they are one of the most commonly used data structures in programming. A dictionary is used to map or associate things you want to store to keys you need to get them.

**What is the difference between a list and a dictionary?**

A list is for an ordered list of items. A dictionary (or dict) is for matching some items(called “keys“) to other items (called “values“).

> cmp(dict1, dict2) compare 2 dicts

> len(dict) calculate the length of dict (how many keys are in the dict)

> str(dict) output dict as string

> dict.clear() clear dict

> dict.copy() copy dict

> dict.has_key(key) if dict has key, then return True, or return False

> dict.keys()　output all keys in dict

> dict.values() output all values in dict


```python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
 
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Alice']: ", dict['Alice'])
```

    dict['Name']:  Zara
    dict['Age']:  7
    


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-5-aa922b487680> in <module>()
          3 print ("dict['Name']: ", dict['Name'])
          4 print ("dict['Age']: ", dict['Age'])
    ----> 5 print ("dict['Alice']: ", dict['Alice'])
    

    KeyError: 'Alice'



```python
dict1 = {"a":[1,2]} 
print (dict1["a"][1])
```

    2
    


```python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
dict['Age'] = 8 # update existing entry
dict['School'] = "DPS School" # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
```

    dict['Age']:  8
    dict['School']:  DPS School
    

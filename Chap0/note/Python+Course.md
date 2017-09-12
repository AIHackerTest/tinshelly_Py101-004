
# Here begins your Python journey!

## 1. Environment Set-up (for Windows)

> ### 1.1 Atom – Text editor
>> Go to [link](https://atom.io) with your browser, get the Atom text editor, and install it.

> ### 1.2	Multi-version Python (Python2.7 + Python3.6) – Coding Language
>> a. Download different version of Python from [link](https://www.python.org/downloads) and install it. Be sure to check the box that says to add Python 2.7/3.6 to your path.
>>> i. Set up multi-version python environment

>>> ii.	Follow “This PC > Properties > Advanced system settings > Environment Variables > Path” and check whether the Python 2.7/3.6 has been added or not. 
If not, edit the path and manually add python directory path into the “Variable value” under “Path” with ; as the separator.

>>> iii.	Or type CLI [Environment]::SetEnvironmentVariable("Path", "$env:Path;**C:\Python27"**, "User") in powershell (**C:\Python27** could be changed according to the python path in your computer.)

>> b.	Change python.exe file of different versions into unique one like python2.exe, python3.exe but caution that the commanding line need to be changed accordingly in specific step operations. 

> ### 1.3	Powershell - Terminal
>> a.	Run PowerShell from the Start menu. Search for it, and you can just press Enter to run it.

>> b.	Learn the CLI of Powershell

>> c.	Redirect to the directory of python, type “python2/python3” and press Enter to run python.

>> d.	Type “quit()” and press Enter to exit python

> ### 1.4	Jupyter notebook – Recording tool
>> a.	Download via PIP 

>>> $Python3 –m pip install jupyter

>> b.	Run the notebook in website

>>> $ .\jupyter-notebook

## 2. Basic Concept

> ### 2.1 	Input and output
>> * Atom

>>> Create and save the Python file as XX.py (also call it script), and then code in it.

>> * Powershell

>>> Run the script by typing like “**python3** XX.py” (**python3** should be the same name as .exe file under your python package. Go find it and change the name correspondingly.)

> ### 2.2 	General
>> * How to display on the output screen 

>>> String should be inside “” (double-quotes) or ‘’ (single-quotes) and either way is acceptable by python


```python
print ("Hello world!")
```

    Hello world!
    

>> * How to make comments for yourself i/o displaying to other when running the scripts

>>> All the things behind # will be ignored for output


```python
print ("Hello world!") # All the things behind # will be ignored for output
```

    Hello world!
    

>> * Take input from a person


```python
input ("give a number>" )
```

>> * Reading and Writing Files 

>>> file.close() - Closes the file

>>> file.read() - Reads the contents of the file

>>> file.readline() - Reads just one line of a text file

>>> file.truncate() - Empties the file

>>> file.write('stuff') - Writes “stuff” to the file

>>> file.seek(0) - Move the read/write location to the beginning of the file

> ### 2.3	Numbers and Math 

>> plus + - addition

>> minus - - deduction

>> slash / - division

>> asterisk * - multiplication

>> percent % - remainder

>> less-than < - True or False based on judgement

>> greater-than > - True or False based on judgement

>> less-than-equal <= - True or False based on judgement

>> greater-than-equal >= - True or False based on judgement


```python
print ("I will now count my chickens:")

print ("Hens", 25 + 30  / 6)
print ("Roosters", 100 - 25 * 3 % 4)

print ("Now I will count the eggs:")

print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print ("Is it true that 3 + 2 < 5 - 7?")

print (3 + 2 < 5 - 7)

print ("What is 3 + 2?", 3 + 2)
print ("What is 5 - 7?", 5 - 7 )

print ("Oh, that's why it's False.")

print ("How about some more.")

print ("Is it greater?", 5 > -2)
print ("Is it greater or equal?", 5 >= -2)
print ("Is it less or equal?", 5 <= -2)
```

    I will now count my chickens:
    Hens 30.0
    Roosters 97
    Now I will count the eggs:
    6.75
    Is it true that 3 + 2 < 5 - 7?
    False
    What is 3 + 2? 5
    What is 5 - 7? -2
    Oh, that's why it's False.
    How about some more.
    Is it greater? True
    Is it greater or equal? True
    Is it less or equal? False
    

> ### 2.4	Variables and Names 
>> * = (single-equal) assigns the value on the right to a variable on the left	

>>> a = b means assigning value of b to variable a (Variable name should start with a character – 1 cannot be a variable but a1 can be)

>> * == (double-equal) tests whether two things have the same value.

>> * How to make strings that have variables embedded in them

>>> f(“string {var}”)

> ### 2.5	Function
>> * Start function with “def” (define)

>> * Global and function variables are separate, so avoid to make them have the same names for confusion

>> * Different ways could be used to give the function the values it needs to print them.


```python
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print ("You have %d cheeses!" % cheese_count)
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    print ("Man that`s enough for a party!")
    print ("Get a blanket.\n")

print ("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print ("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)
```

    We can just give the function numbers directly:
    You have 20 cheeses!
    You have 30 boxes of crackers!
    Man that`s enough for a party!
    Get a blanket.
    
    OR, we can use variables from our script:
    You have 10 cheeses!
    You have 50 boxes of crackers!
    Man that`s enough for a party!
    Get a blanket.
    
    We can even do math inside too:
    You have 30 cheeses!
    You have 11 boxes of crackers!
    Man that`s enough for a party!
    Get a blanket.
    
    And we can combine the two, variables and math:
    You have 110 cheeses!
    You have 1050 boxes of crackers!
    Man that`s enough for a party!
    Get a blanket.
    
    

> ### 2.6	Truth term
>> not Fale - True

>> not True - False

>> True or False - True

>> True or True - True

>> False or True - True

>> False or False - False

>> True and False - False

>> True and True - True

>> False and True - False

>> False and False - False

>> not (True or False) - False

>> not (True or True) - False

>> not (False or True) - False

>> not (False or False) - True

>> not (True and False) - True

>> not (True and True) - False

>> not (False and True) - True

>> not (False and False) - True

>> 1 != 0 - True

>> 1 != 1 - False

>> 0 != 1 - True

>> 0 != 0 - False

>> 1 == 0 - False

>> 1 == 1 - True

>> 0 == 1 - False

>> 0 == 0 - True

> ### 2.7	What if
>> Create “branch” in the code

>>> * If … :

>>> * Elif…:

>>> * Else…:


```python
people = 30
cars = 40
buses = 15

if cars > people and buses > cars:
    print ("We should take the cars.")
elif cars < people:
    print ("We should not take the cars.")
else:
    print ("We can't decide")

if buses > cars:
    print ("That's too many buses.")
elif buses < cars:
    print ("Maybe we could take the buses.")
else:
    print ("We still can't decide.")

if people > buses:
    print ("Alright, Let's just take the buses.")
else:
    print ("Fine, Let`s stay home then.")
```

    We can't decide
    Maybe we could take the buses.
    Alright, Let's just take the buses.
    

> ### 2.8	Loops
>> In order to do repetitive things efficiently, loops programs are needed. 

>> * for-loop


```python
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print ("This is count %d" % number)

# same as above
for fruit in fruits:
    print ("A fruit of type: %s" % fruit)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print ("I got %r" % i)

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print ("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print ("Element was: %d"  % i)

```

    This is count 1
    This is count 2
    This is count 3
    This is count 4
    This is count 5
    A fruit of type: apples
    A fruit of type: oranges
    A fruit of type: pears
    A fruit of type: apricots
    I got 1
    I got 'pennies'
    I got 2
    I got 'dimes'
    I got 3
    I got 'quarters'
    Adding 0 to the list.
    Adding 1 to the list.
    Adding 2 to the list.
    Adding 3 to the list.
    Adding 4 to the list.
    Adding 5 to the list.
    Element was: 0
    Element was: 1
    Element was: 2
    Element was: 3
    Element was: 4
    Element was: 5
    

>> * while-loop

>>> What they do is simply do a test like an if-statement, but instead of running the code block once, they jump back to the “top” where the while is, and repeat. A while-loop runs until the expression is
False.

>>  Usually a for-loop is better because you need to define the range for for-loop to run several times or it will only run one time but while-loop sometimes could be infinite and cannot stop. 


```python
i = 0
numbers = []

while i < 6:
    print ("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print ("Numbers now: ", numbers)
    print ("At the bottom i is %d" % i)

print ("The numbers: ")

for num in numbers:
    print (num)

# use for-loop

for i in range(0, 6):
    numbers.append(i)

#for num in numbers:
#    print num
print (numbers)
```

    At the top i is 0
    Numbers now:  [0]
    At the bottom i is 1
    At the top i is 1
    Numbers now:  [0, 1]
    At the bottom i is 2
    At the top i is 2
    Numbers now:  [0, 1, 2]
    At the bottom i is 3
    At the top i is 3
    Numbers now:  [0, 1, 2, 3]
    At the bottom i is 4
    At the top i is 4
    Numbers now:  [0, 1, 2, 3, 4]
    At the bottom i is 5
    At the top i is 5
    Numbers now:  [0, 1, 2, 3, 4, 5]
    At the bottom i is 6
    The numbers: 
    0
    1
    2
    3
    4
    5
    [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
    

# Practice, practice and practice!

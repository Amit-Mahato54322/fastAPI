# let's define a variable which is a list of strings
def process_items(items: list[str]):
    for item in items:
        print(item)

# we can also do this in python
def process2(items: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

# This means that in a tuple there are three items, out of which first two are integers and the third one is a string. 

# for dictionary:
def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

# we can also decalre that a particular variable can be of several types
def process_item(item: int| str):
    print(item)

# here variabele 'item' can be integer or a string.


#Possibly None
# You can delcare that a value could have a type, like a str, but that it could also be a None.
from typing import Optional
def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}")
    else:
        print("hello world ")
# OR

def say_hi(name: str|None =  None):
    if name is not None:
        print(f" Hey {name}")
    else:
        print("hello world")

        

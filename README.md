# Session 10 - Tuples & Named Tuples and Modules
# EPAi Session10 Assignment

#### Objective of Assignment:

1. Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age and average age

2. Use Faker library to get 10000 random profiles. Using dictionary, calculate the largest blood type, mean-current_location, oldest_person_age and average age. Prove that namedtuple is faster.

3. Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value stock market started at, what was the highest value during the day and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple.

## Tuple and NamedTuple:

A tuple is a collection which is ordered and immutable. Python supports a type of container like dictionaries called namedtuplepresent in module, collections. Like dictionaries they contain keys that are hashed to a particular value. But on contrary, it supports both access from key value and iteration, the functionality that dictionaries lack.

A named tuple is a tuple. It does everything a tuple can. But it's more than just a tuple. It's a specific subclass of a tuple that is programmatically created to your specification, with named fields and a fixed length.

## Faker:

Faker is a Python package that generates fake data for you. Faker has the ability to print/get a lot of different fake data, for instance, it can print fake name, address, email, text, etc. We make use of fake profiles and companies for our purpose.

```python
from faker import Faker

fake = Faker() # creating faker object
fake.profile() # generates a fake profile
fake.company() # generates a fake company name
```

## faker_namedtuple:

Generates random profiles Using the namedtuple and calculates the largest blood type, mean-current_location, oldest_person_age and average age


## faker_dict:

Generates random profiles Using the dictionary and calculates the largest blood type, mean-current_location, oldest_person_age and average age

## check_performance:

This function executes the faker_namedtuple and faker_dict functions for the number of iterations specified. Then it calculates the time taken by both Named Tuple and Dictionary. Finally it returns the one which took less time to execute


## stock_market_data:

This function generates a company stock profile for market value using faker library and stores the stocks details as a namedtuple. It simulates instantaneous market trend and returns the stock index.


Created a test functions to validate the functions.

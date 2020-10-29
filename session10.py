from collections import namedtuple, Counter
from datetime import date, timedelta
from random import uniform, randint
from typing import Callable
from faker import Faker
import time
import random
import pandas as pd
import re

# Question-1: Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age and average age

def faker_namedtuple():
    """ 
    10000 random profiles Using the namedtuple calculate the largest blood type, mean-current_location, oldest_person_age and average age

    """

    today = date.today()
    fake = Faker()
    fake_list=[]
    for i in range(10000):
        test = fake.profile()
        Fake_Profile = namedtuple('Fake_Profile',sorted(test))
        tuple_x = Fake_Profile(**test)
        fake_list.append(tuple_x)

        start = time.perf_counter()

        tuple_summary = namedtuple('tuple_summary',['blood_group','mean_location','old_age','avg_age','total_time'])
        # start = time.perf_counter()

        mean_location = sum(sum(x.current_location) for x in fake_list)/10000

        blood_group = max(Counter(x.blood_group for x in fake_list))

        older = min(fake_list, key=lambda k: k.birthdate).birthdate
        today = date.today()
        old_age = today.year - older.year

        years = [today.year - x.birthdate.year for x in fake_list]
        avg_age = sum(years)/len(years)

        stop = time.perf_counter()

        total_time = stop - start

        print(f'Blood Group: {blood_group} \nMean Current Location: {mean_location} \nOldest Person Age: {old_age} \nMean Age: {avg_age} \nTime Taken to Run Named Tuple: {total_time}')
        # return faker_namedtuple

        return tuple_summary('blood_group','mean_location','old_age','avg_age','total_time')


# Question-2: Use Faker library to get 10000 random profiles. Using Dictionary, calculate the largest blood type, mean-current_location, oldest_person_age and average age

def faker_dict():
    """ 
    10000 random profiles Using the Dictionary calculate the largest blood type, mean-current_location, oldest_person_age and average age
    
    """

    today = date.today()
    fake = Faker()
    fake_list=[]
    for i in range(10000):
        test = fake.profile()
        # Fake_Profile = namedtuple('Fake_Profile',sorted(test))
        # tuple_x = Fake_Profile(**test)
        fake_list.append(test)

        start = time.perf_counter()

        tuple_summary = namedtuple('tuple_summary',['blood_group','mean_location','old_age','avg_age','total_time'])
        

        mean_location = sum(sum(x["current_location"]) for x in fake_list)/10000

        blood_group = max(Counter(x["blood_group"] for x in fake_list))

        older = min(fake_list, key=lambda k: k["birthdate"])["birthdate"]
        today = date.today()
        old_age = today.year - older.year

        years = [today.year - x["birthdate"].year for x in fake_list]
        avg_age = sum(years)/len(years)

        stop = time.perf_counter()

        total_time = stop - start

        print(f'Blood Group: {blood_group} \nMean Current Location: {mean_location} \nOldest Person Age: {old_age} \nMean Age: {avg_age} \nTime Taken to Dictionary: {total_time}')
        # return faker_namedtuple

        return tuple_summary('blood_group','mean_location','old_age','avg_age','total_time')

def check_performance():
    '''
    This function executes the above two functions for the number of iterations specified
    Then it calculates the time taken by both Named Tuple and Dictionary
    Finally it returns the one which took less time to execute
    '''
    start = time.perf_counter()
    val = faker_namedtuple()
    end = time.perf_counter()
    elapsed_time_tuple = (end-start)

    start = time.perf_counter()
    val = faker_dict()
    end = time.perf_counter()
    elapsed_time_dict = (end-start)

    if elapsed_time_tuple > elapsed_time_dict:
        print(f'The Tuple is Slower than the Dictionary by {elapsed_time_tuple - elapsed_time_dict} secs')
        return 'Named Tuple Slower'
    else:
        print(f' The Dictionary is Slower than the Tuple by {elapsed_time_dict - elapsed_time_tuple} secs')
        return 'Dictionary Slower'


# Question-3: Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value stock market started at, what was the highest value during the day and where did it end by using NamedTuple

def stock_market_data(n):
    '''
    function generates a company stock profile for market value using faker library and stores the stocks details as
    a namedtuple.it simulates instantaneous market trend and returns the stock index.
    '''

    company_stock_list=[]
    company_stock = namedtuple('company_stock', 'company_name symbol stock_o stock_h stock_c')
    company_stock.__doc__ = "Company stock profile with current market values"

    for i in range(n):
        fake = Faker()
        name = fake.company()
        sys = re.split(r'\s|-|,', name)
        while("" in sys) :
            sys.remove("")

        symbol = "".join(e[0] for e in sys)
        stock_o = random.uniform(0, 4000)
        stock_h = stock_o * random.uniform(1, 1.3)
        stock_c = stock_h * random.uniform(0.7,1)
        company_stock_list.append(company_stock(name, symbol, stock_o, stock_h, stock_c))

    weights = [random.uniform(0,1) for i in range(n)]
    norm_weights = [i/sum(weights) for i in weights]

    stock_open = sum([(i.stock_o * weight)  for (i,weight) in zip(company_stock_list, norm_weights)])
    stock_high = sum([(i.stock_h * weight) for (i,weight) in zip(company_stock_list, norm_weights)])
    stock_close = sum([(i.stock_c * weight) for (i,weight) in zip(company_stock_list, norm_weights)])
    
    stock_index = {'number of companies':len(company_stock_list),'stock index open':stock_open,'stock index high':stock_high,'stock index close':stock_close}
    return company_stock_list,stock_index

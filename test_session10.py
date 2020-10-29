
import inspect
import os
import re
import time
import pytest
from freezegun import freeze_time
from datetime import datetime
import session10 as s10
from unittest import TestCase
from decimal import Decimal





README_CONTENT_CHECK_FOR = ["odd_sec_run","log_func","authenticate","time_it","privilege","htmlize"]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 400, "Make your README.md file interesting! Add atleast 400 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 6

# def test_indentations():
#     ''' Returns pass if used four spaces for each level of syntactically \
#     significant indenting.'''
#     lines = inspect.getsource(s10)
#     spaces = re.findall('\n +.', lines)
#     for space in spaces:
#         assert len(space) % 4 == 2, "Your script contains misplaced indentations"
#         assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(s10, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_docstring():
    functions = inspect.getmembers(s10, inspect.isfunction)

    for func in functions:
        assert not func.__doc__ is None, f"docstring not included in {func}"

def test_faker_namedtuple():
    assert bool(s10.faker_namedtuple()), 'no value true returned something is wrong'

def test_faker_dict():
    assert bool(s10.faker_dict()), 'no value true returned something is wrong'


def test_nt_blood_group():
    x=s10.faker_namedtuple()
    assert bool(x.blood_group), 'no value true returned something is wrong'

def test_nt_location_count():
    x=s10.faker_namedtuple()
    assert bool(x.mean_location), 'no value true returned something is wrong'

def test_nt_oldest_person():
    x=s10.faker_namedtuple()
    assert bool(x.old_age), 'no value true returned something is wrong'

def test_nt_avg_age():
    x=s10.faker_namedtuple()
    assert bool(x.avg_age), 'no value true returned something is wrong'

def test_dc_blood_group():
    x=s10.faker_dict()
    assert bool(x.blood_group), 'no value true returned something is wrong'

def test_dc_location_count():
    x=s10.faker_dict()
    assert bool(x.mean_location), 'no value true returned something is wrong'

def test_dc_oldest_person():
    x=s10.faker_dict()
    assert bool(x.old_age), 'no value true returned something is wrong'

def test_dc_avg_age():
    x=s10.faker_dict()
    assert bool(x.avg_age), 'no value true returned something is wrong'

def test_performance():
    x=s10.check_performance()
    assert x=="Dictionary Slower","Tuples are running slower"

def test_stock_market():
    company_stock_list, stock_index = s10.stock_market_data(100)
    assert len(company_stock_list) == 100 # check the result
    assert type(stock_index)== dict
    assert len(stock_index)== 4

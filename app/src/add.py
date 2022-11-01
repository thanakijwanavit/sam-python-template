from awsSchema.apigateway import Response, Event
from numbers import Number
from typing import List
import math

def add(event, *args):
    '''
        add numbers for example 
    '''
    numbers = Event.parseBody(event)
    if not isinstance(numbers, List): 
        raise TypeError("input should be a list of numbers")
    result = addNumbers(numbers)
    return Response.returnSuccess(result)

def addNumbers(numbers:List[Number])->Number:
    return sum(numbers)
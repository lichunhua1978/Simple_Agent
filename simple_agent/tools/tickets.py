# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:37:04 2024

@author: lichunhua

票务的tools，用于demo

"""




import json
import requests
import traceback


class TicketTool(object):
    """
    返回指定地区、指定时间段演唱会的票务信息，包括演唱会的名称，具体时间，价格.

    Args:
        
        start_date (str): Start date in format "yyyy-MM-dd".
        end_date (str): End date in format "yyyy-MM-dd".
        location (str): Locations in English separated by commas, e.g., "Beijing,Vancouver,...,Chicago".

    Returns:
        str:  返回指定地区、指定时间段演唱会的票务信息，包括演唱会的名称，具体时间，价格.
    """
    name = "get_tickets_info"
   



    def __init__(self, *args, **kwargs ):
        pass
     

    def __call__(self, start_date, end_date,  location , *args, **kwargs) :
        
  

        return [[start_date,'张学友演唱会','100']]
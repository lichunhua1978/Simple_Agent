# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:37:04 2024

@author: lichunhua

天气tools demo

"""




import json
import requests
import traceback


class WeatherTool(object):
    """
    返回指定地区、指定时间的天气.

    Args:
        
        start_date (str): Start date in format "yyyy-MM-dd".
        end_date (str): End date in format "yyyy-MM-dd".
        location (str): Locations in English separated by commas, e.g., "Beijing,Vancouver,...,Chicago".

    Returns:
        str: 返回指定时间、指定地区的天气.
    """
    name = "get_weather_info"
    # description = 'Get weather info:"get_weather_info", args:"location": <location1,location2,...,in English,required>, "start_date":"<str: yyyy-MM-dd, required>", "end_date":"<str: yyyy-MM-dd, required>", "is_current":"<str, yes or no, required>"'
    



    def __init__(self, *args, **kwargs ):
        pass
     

    def __call__(self, start_date, end_date,  location , *args, **kwargs) :
        
  

        return ['晴']
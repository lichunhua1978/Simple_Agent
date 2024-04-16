
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:37:04 2024

@author: lichunhua

tools初始化

"""


from .weather import WeatherTool
from .tickets import TicketTool
from .search import WebSearchTool

TOOLS_LIST = [  WeatherTool,TicketTool,WebSearchTool]



#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:37:04 2024

@author: lichunhua

搜索tools

"""


import requests
import traceback
import json
from config.config import ServerConfig


class WebSearchTool(object):
    
    """
    Perform an internet search.

    Args:
        text (str): Search query.

    Returns:
        str: Multiple webpage links along with brief descriptions.
    """
    name = "web_search"



    def __init__(self, *args, **kwargs ):
        pass
     

    def __call__(self, text, *args, **kwargs) :
        
    
        
        try:
            rs=[]
            subscription_key = ServerConfig.bing_search_key.strip()
            
            
            
            search_url = "https://api.bing.microsoft.com/v7.0/search"

            
            headers = {"Ocp-Apim-Subscription-Key": subscription_key}
            params = {"q": text, "textDecorations": True, "textFormat": "HTML"}
            response = requests.get(search_url, headers=headers, params=params)
            response.raise_for_status()
            search_results = response.json()
    
            for item in search_results['webPages']['value']:
                rs.append(item['snippet'])

            return rs
        except:
            print(traceback.format_exc())
            return []
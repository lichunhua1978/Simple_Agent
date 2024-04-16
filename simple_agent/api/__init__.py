
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:50:13 2024

@author: lichunhua

初始化访问大模型的API

"""

import time

from api.openai import OpenAI_API

from api.zhipuai import ZhipuAI_API

from config.config import ServerConfig


def chat(message):
    
    if ServerConfig.api_type =='zhupuAI':
        api = ZhipuAI_API(ServerConfig.model.lower())
    else:
        api = OpenAI_API(ServerConfig.model.lower())
        
    response = ''
    
    max_retries = 3
    
    for attempt in range(max_retries):
 
        try:
            
            response = api.chat(message)
            
            if len(response)>0:
                break
            
        except Exception as err:
            
            print(err)
            
        time.sleep(1)
 

    return response
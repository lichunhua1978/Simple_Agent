# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:50:13 2024

@author: lichunhua

openai远程访问api

"""

import openai
import traceback
from api.message import LLM_Message
from config.config import ServerConfig


class OpenAI_API(object):
    
    #初始化
    def __init__(self, model):
        
        self.model = model
        
        openai.api_key=ServerConfig.api_key   
      
        #设置代理服务器
        if ServerConfig.use_proxy:
        
             openai.proxy = ServerConfig.proxy
     
 
    #调用对话接口
    def chat(self, message):
        
        try:
               
            response = openai.ChatCompletion.create(
                    model = self.model,
                    messages=message.get_messages(),
                    temperature = 0.1
                )
            response_text = response['choices'][0]['message']['content']
        except:
            print(traceback.format_exc())
            response_text = ""

        return response_text


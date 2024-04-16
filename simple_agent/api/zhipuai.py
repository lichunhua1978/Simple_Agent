# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:50:13 2024

@author: lichunhua

清华智谱AI访问接口

"""

from zhipuai import ZhipuAI
import traceback
from api.message import LLM_Message
from config.config import ServerConfig


class ZhipuAI_API(object):
    
    #初始化
    def __init__(self, model):
        
        
        
        self.model = model
        self.api_key=ServerConfig.api_key
        self.api_terminal  = ZhipuAI(api_key=self.api_key)
     
 
    #调用对话接口
    def chat(self, message):
        

        try:
            response = self.api_terminal.chat.completions.create(
                model=self.model, 
                messages=message.get_messages()
                )
        
            answer=response.choices[0].message

            response_text=dict(answer)["content"]
 
        except:
            print('zhipuai api error')
            print(traceback.format_exc())
            
            response_text = ""

        
        return response_text
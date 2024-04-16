# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:53:23 2024

@author: lichunhua

封装大模型访问需要的消息

"""

class LLM_Message(object):
    
    def __init__(self, query, system, history):
        self.query=query
        self.system=system
        self.history=history
    
    def get_messages(self):
        
        message = []

        message.append({
            "role": "user",
            "content": self.query
            })     
        
        if self.system:
            message.append({
                "role": "system",
                "content": self.system
            })
            
        for question, answer in self.history:
            message.append({
                "role": "user",
                "content": question
            })
            message.append({
                "role": "assistant",
                "content": answer
            })


        return message
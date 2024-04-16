# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:53:23 2024

@author: lichunhua

一个agent的相关的配置信息

"""



class AgentProfile(object):
    
    def __init__(self, args) :
        
        self.data=args

    # 得到一个配置项的内容
    def get_attribute(self,attr):
        
        if attr in self.data.keys():
            
            return self.data.get(attr)
        else:
            
            return ''

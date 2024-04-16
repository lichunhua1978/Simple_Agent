# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:08:15 2024

@author: lichunhua

系统基础配置类

"""

class ServerConfig(object):
    

    
    #大模型访问API KEY
    api_key=''    # zhipu

    
 
    
    #WebSearchTools所需的bing search key
    bing_search_key=''
    
    #代理服务器地址，国内服务器访问openai时需要，有可能经常被封，不建议使用
    proxy='127.0.0.1:3128'
    
    #是否使用代理服务器地址
    use_proxy=False  
    # use_proxy=True 
    
    #模型的名称
    model='glm-4'
    # model='gpt-3.5-turbo'

    #访问接口的类型
    api_type='zhupuAI'   # or OpenAI 
    # api_type='OpenAI'
    
     

ServerSetting = ServerConfig()
    
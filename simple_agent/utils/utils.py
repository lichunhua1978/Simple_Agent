# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:37:04 2024

@author: lichunhua

公共服务代码

"""

import docstring_parser
from datetime import datetime
import json


#从输入文本里截取json部分的字符       
def get_json_string(input_str):
    input_str=input_str.replace('\n','').replace(' ','')
    
    if input_str.count('[') !=input_str.count(']') or input_str.count('{') !=input_str.count('}') :
        return "[]"
       
    if input_str.count('[')==1 and input_str.count(']')==1:
        
       if "[" in input_str and '}]' in input_str:
        
            st = input_str.index("[")
            end_str = '}]'
            end = input_str.rindex(end_str)
            if end>st:
              return input_str[st:end + len(end_str)].strip()

    if input_str.count('[')==2 and input_str.count(']')==2:
        
        if "[[" in input_str and '}]' in input_str:

            st = input_str.index("[[")+1
            end_str = '}]'
            end = input_str.rindex(end_str)
            if end >st:
               return input_str[st:end + len(end_str)].strip()    
    
    return input_str





#把输入的文本中的json，转成对象
def get_json_obj(json_to_load: str) -> str:
    
    json_to_load=get_json_string(json_to_load)
    try:
        json.loads(json_to_load)
        return json_to_load
    except json.JSONDecodeError as e:
        print("json loads error", e)
        print(json_to_load)
      
    return json_to_load


#把tool类的描述输出
def get_func_meta(func):
    parsed = docstring_parser.parse(func.__doc__)

    description = parsed.short_description

    args = {}
    for param in parsed.params:
        args[param.arg_name] = {
            "type": param.type_name,
            "description": param.description,
            "required":True
        }

    returns = {
        "description": parsed.returns.description if hasattr(parsed.returns, "description") else "",
        "type": parsed.returns.type_name if hasattr(parsed.returns, "type_name") else ""
    }

    return {
        "name": func.name if hasattr(func, "name") else func.__name__,
        "description": description,
        "parameters": {
            "type": "object",
            "properties": args
        },
        "returns": returns,
  
    }

#得到当前的日期
def get_current_time_and_date():
    

    rst = f'''
当前阳日期和时间: {str(datetime.now())}
'''.strip()
    
    return rst

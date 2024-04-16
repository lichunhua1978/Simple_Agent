# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:37:04 2024

@author: lichunhua

prompt模板


"""
from agent.agent_profile import AgentProfile
from utils.utils import get_func_meta
from utils.utils import get_current_time_and_date
import  json

class PromptMaker(object):
    
    
    #生成plan的prompt模板
    planning_prompt_template_zh = """
        你是{agent_name}，{agent_desc}，
        {agent_instructions}，
        
        任务规划的要求：
        当前阶段是任务规划阶段，你将给定目标和任务，你的决策将独立执行而不依赖于人类的帮助，请发挥LLM的优势并且追求高效的策略进行任务规划。
        1.你有~4000字的短期记忆
        2.不需要用户的帮助
        3.规划的时候只能用参考工具中提到的工具，没有提到的工具不能用
        4.互联网搜索、信息聚合和鉴别真伪的能力
        5.保持谦逊，对自己没把握的问题，尽可能调用command，但尽量少调用，可以多次调用
        6.当你从自身知识或者历史记忆中能得出结论，请聪明且高效，完成任务并得出结论
        7.你最多只能规划5个任务，一般3个任务，所以尽可能高效规划任务
        8，每个command的name必须是现有工具列表中包含的名字，不能出现其他名字
      
  
        工具列表：
        {tool_specification}
        
        当前时间：
        {current_date_and_time}
        
        记忆：
        {memory}
        
        目标和任务:{question}
        
        \n根据目标和已有任务，规划一组Task，你只能以以下json列表的格式生成Task，数据结构整体上是一个list，不能有多个list，list的每个元素是一个任务，任务是dict结构，详细的json格式如下所示：
        

[[
         {{
            "task_name": "任务描述",
            "command":{{
                "name":"command name",
                "args":{{
                    "arg name":"value"
                }}
            }}
         }},
         {{
            "task_name": "任务描述",
            "command":{{
                "name":"command name",
                "args":{{
                    "arg name":"value"
                }}
            }}
         }},
         {{
            "task_name": "任务描述",
            "command":{{
                "name":"command name",
                "args":{{
                    "arg name":"value"
                }}
            }}
         }}
]]
 
        确保只生成一个json，不能有多个，生成的json可以被Python的json.loads解析，生成的json不能有注释，不需要解释json中的内容。生成的task名称一定是已有的工具名称列表中的，不要生成新的工具名称。
        
        """.strip()
        
        
    conclusion_prompt_template_zh = """
        你是{agent_name}，{agent_desc}，
        {agent_instructions}，
        当前阶段是总结阶段，在前几次交互中，对于用户给定的目标和问题，你已经通过自己搜寻出了一定信息，你需要整合这些信息用中文给出最终的结论。
        搜寻的信息从很多工具中获取，会出现冗余
      
        
        {current_date_and_time}
        
        {memory}
                
        {knowledge_base}
        
        {result}
        
        问题或目标：{question}\n生成对用户有帮助的中文回答:
    """
    def __init__(self,agent_profile:AgentProfile):
        self.agent_profile=agent_profile
    
    #生成计划的prompt
    def gen_planning_prompt(self,agent_profile, question, tools, memory, lang="zh"):
        tool_spec = self.gen_tool_specification(tools)

        prompt = self.planning_prompt_template_zh.format(**{
            "agent_name": agent_profile.get_attribute('agent_name'),
            "agent_desc": agent_profile.get_attribute('agent_desc'),
            "agent_instructions": agent_profile.get_attribute('agent_instructions'),

            "tool_specification": tool_spec,
            "current_date_and_time": get_current_time_and_date(),
            "memory": memory,
       
            "question": question
         })
        return prompt
    
    #生成工具的描述
    def gen_tool_specification(self,tools):
        
        functions = [get_func_meta(t) for t in tools]
        
        # print(tools)
    
        commands, cnt = [], 1
        for f in functions:
            func_str = json.dumps(f, ensure_ascii=False)
            commands.append(f"{cnt}:{func_str}")
            cnt += 1
    
        used_commands = "\n".join(commands)
    
        tool_spec = f'Commands:\n{used_commands}\n'
        
        
    
        return tool_spec   
    
    #生成总结prompt
    def gen_task_conclusion_prompt(self,agent_profile, question, memory, result, lang="zh"):
    
       prompt = self.conclusion_prompt_template_zh.format(**{
        "agent_name": agent_profile.get_attribute('agent_name'),
        "agent_desc": agent_profile.get_attribute('agent_desc'),
        "agent_instructions": agent_profile.get_attribute('agent_instructions'),
        "current_date_and_time": get_current_time_and_date(),
        "memory": memory,
        "result": result,
        "question": question,
        "knowledge_base":agent_profile.get_attribute('knowledge_base')
         })

       return prompt 



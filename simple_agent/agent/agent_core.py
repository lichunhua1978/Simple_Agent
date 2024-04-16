# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:53:23 2024

@author: lichunhua

执行AI Agent的核心逻辑

"""

from agent.agent_profile import AgentProfile
from tools import TOOLS_LIST
from agent.prompt_maker import PromptMaker
from api import chat
from api.message import LLM_Message
from utils.utils import get_json_obj
import json
import traceback

#负责处理一个AI Agent的核心功能
class AgentCore(object):

    def __init__(self,agent_profile:AgentProfile):
        
        self.agent_profile=agent_profile
     

   
    #针对历史对话记录，生成prompt
    def gen_mem_prompt(self,history):
        
        mem_prompt=''
        
        if history:
            mem_prompt += "* 对话历史:\n"
            for h in history:
                # print(h)
                mem_prompt+= f"User: {h['question']}\nAssistant:{h['answer']}\n"    
        return mem_prompt
    
    
    #初始化工具列表
    def init_tools(self):
        
        tools_desc=self.agent_profile.get_attribute('tools')
        
        if len(tools_desc)>0:
            
            tools_desc_list=tools_desc.split(',')
            active_tools=[]     #本次需要使用的tools
            for t in TOOLS_LIST:
                if t.__name__ in tools_desc_list:
                    active_tools.append(t())
            self.tools=active_tools
        self.name2tools = {t.name: t for t in self.tools}  

    def check_task_list(self,tasks):
        if len(tasks)==0:
            return False
        return True
    
    #生成计划任务列表            
    def gen_task_plan(self, question, mem_prompt):
        
        new_tasks=[]
        
        for i in range(5):
        

            prompt_maker=PromptMaker(self.agent_profile)
            
            plan_prompt=prompt_maker.gen_planning_prompt(self.agent_profile, question, self.tools, mem_prompt,  "zh")
            
            msg=LLM_Message(plan_prompt,'','')
            
            response=chat(msg)
            
            
            # print(response)
            
            try:
                response = get_json_obj(response)
                # print(response)
                task = json.loads(response)
                new_tasks = task
                
                # print(new_tasks)
            except:
                print(traceback.format_exc())
                # print("+" + response)
    
            
            if   self.check_task_list(new_tasks):
                print('\n\n计划完成')
                break

        print(json.dumps(new_tasks ,ensure_ascii=False, indent=4))
        return new_tasks
    
    #执行一个任务
    def task_execute(self, command) :
        try:
            command_name = command.get("name", "")
    
            print('task name:',command_name)
        
            if not command_name:
                return ''
             
            if command_name not in self.name2tools:
                return ''             
                
            tool = self.name2tools[command_name]           

            tool_output = tool(**command["args"])
            
            return tool_output
        
        except:
            
            print(traceback.format_exc())
         
            return []
        
    #总结现有查询到的资源，总结答案
    def gen_answer(self, question, mem_prompt,result):
        

        prompt_maker=PromptMaker(self.agent_profile)
        
        conclusion_prompt=prompt_maker.gen_task_conclusion_prompt(self.agent_profile, question, mem_prompt, result,  "zh")
        msg=LLM_Message(conclusion_prompt,'','')
            
        response=chat(msg)
        
        return response
        
    #回答问题总体流程
    def chat(self):
        
        self.init_tools()

        rs=''
        
        print('\n\n问题：')
        question=self.agent_profile.get_attribute('question')
        history=self.agent_profile.get_attribute('history')
        mem_prompt=self.gen_mem_prompt(history)
        
        print(question)
        
        print('\n\n计划：')
        tasks=self.gen_task_plan( question, mem_prompt)        
        
        print('\n\n执行：')
        
        result=[]
        for task in tasks:

                # print(task)
     
                task_result= self.task_execute(task["command"])

                # print('\n task result:',task_result)
               
                result.append(task_result)
        
        print(result)    
        
        print('\n\n结论：')
        answer=self.gen_answer( question, mem_prompt,result)
        print(answer)
                
        rs=answer
        
        return rs        
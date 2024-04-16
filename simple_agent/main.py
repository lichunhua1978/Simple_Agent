# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:15:34 2024

@author: lichunhua

主程序入口

"""


from agent.agent_profile import AgentProfile

from agent.agent_core import AgentCore

def test_case1():

    agent_config={
        "sessionid":"2",
        "question":"明天天气适不适合看演唱会",
        "history":[{"question":"明天有演唱会吗，","answer":"明天晴"},{"question":"明天天气适合看刘德华的演唱会吗","answer":"明天没有演唱会"}],
        "tools":"WeatherTool,TicketTool",
        "agent_name":"个人事务安排助手",
        "agent_desc":"负责帮助个人完成日常任务",
        "agent_instructions":"注意天气、时间和能不能看演唱会的关系",
        "knowledge_base":"",
        "language":"zh"
    
    }
    
    profile=AgentProfile(agent_config)
    
    agent=AgentCore(profile)
    agent.chat()

def test_case2():

    agent_config={
        "sessionid":"3",
        "question":"什么是传感器",
        "history":[],
        "tools":"WebSearchTool",
        "agent_name":"个人事务安排助手",
        "agent_desc":"负责帮助个人完成日常任务",
        "agent_instructions":"",
        "knowledge_base":"",
        "language":"zh"
    
    }
    
    profile=AgentProfile(agent_config)
    
    agent=AgentCore(profile)
    agent.chat()

test_case2()
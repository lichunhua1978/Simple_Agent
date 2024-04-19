Simple Agent

1、介绍：

Simple Agent是一个简化的Agent，能够完成任务规划、工具调用和结论总结，系统提供了一个web搜索工具，两个用于测试的工具（天气工具、买票工具）
Agent支持清华chatglm、openai两个远程API接口。
目前系统不提供长短期记忆，需要调用Agent的client保存记忆

2、quick start
 
 a、安装需要的库
 
    pip install -r requirements.txt 
	
 b、配置参数
 
    在config.py中配置参数，主要是大模型访问接口、代理、大模型key、bing search api key。
 
 c、执行demo
 
    python main.py
 
3、执行demo

    demo有两个，一个是根据天气、票务信息来规划出行，另一个是通过web搜索，回答用户问题（需要bing search api key）


开发者联系方式： lichunhua@139.com

 
 

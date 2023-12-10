import autogen
from autogen.agentchat.contrib.agent_builder import AgentBuilder

# 1. Configuration
config_path = 'OAI_CONFIG_LIST.json'
config_list = autogen.config_list_from_json(config_path)
default_llm_config = {'temperature': 0}

# 2. Initialising Builder
builder = AgentBuilder(config_path=config_path,builder_model='gpt-4-1106-preview', agent_model='gpt-4-1106-preview')

# 3. Building agents
building_task = "develop a basic task management system in python for a restaurant"
agent_list, agent_configs = builder.build(building_task, default_llm_config,coding=True)


# 4. Multi-agent group chat
group_chat = autogen.GroupChat(agents=agent_list, messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=group_chat, llm_config={"config_list": config_list, **default_llm_config})
agent_list[0].initiate_chat(
    manager, 
    message="develop a basic task management system in python for a restaurant"
)
#clear all agents to start the next task
#builder.clear_all_agents(recycle_endpoint=True)
#save all necessary information of the built group chat agents
saved_path = builder.save()
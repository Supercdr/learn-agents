import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
load_dotenv()

def create_openai_model_client():
    """ 创建并配置OpenAI客户端 """
    return OpenAIChatCompletionClient(
        model=os.getenv("LLM_MODEL_ID","qwen3.5-122b-a10b"),
        api_key=os.getenv("LLM_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL","https://ws-6dqgtj1i0ofw12al.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"),
        # 使用非OpenAI模型时需要的参数
        model_info = {
            "vision": False,  # Qwen文本模型通常不支持图像输入
            "function_calling": True,  # Qwen系列通常支持函数调用
            "json_output": False,  # 视情况调整；若需严格JSON输出可尝试设为True
            "family": "unknown",  # 非OpenAI家族，填"unknown"即可
        }
    )

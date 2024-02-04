"""
    基于pydantic获取

    # pip install pydantic
    # pip install pydantic-settings

    运行环境:
    - Python                :3.12.1
    - pydantic              :2.6.0
    - pydantic_core         :2.16.1
    - pydantic-settings     :2.1.0
    - python-dotenv         :1.0.1
"""

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class EnvFileSettings(BaseSettings):
    user:str
    age:int=10

    """
        env_file: 指定环境变量的文件名 
        extra:额外参数的处理 
            - allow:  允许额外的环境变量参数
            - forbid: 屏蔽额外的环境变量参数(要求取值内容和定义内容保持一致)
            - ignore: 忽略额外的环境变量参数
    """
    model_config = ConfigDict(env_file='.env',extra='forbid')

if __name__ == '__main__':
    a = EnvFileSettings()
    print(a.model_dump())

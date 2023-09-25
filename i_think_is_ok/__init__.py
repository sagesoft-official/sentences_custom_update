'''
Author: Nya-WSL
Copyright © 2023 by Nya-WSL All Rights Reserved. 
Date: 2023-09-25 21:46:47
LastEditors: 狐日泽
LastEditTime: 2023-09-25 22:51:50
'''
from nonebot import on_command
from services.log import logger
from nonebot.adapters.onebot.v11 import MessageEvent
from utils.message_builder import image
from configs.path_config import IMAGE_PATH
from pathlib import Path
import os
import gc
import json
import random

__zx_plugin_name__ = "我觉得行"
__plugin_cmd__ = ["我觉得行"]
__plugin_version__ = 0.1
__plugin_author__ = "Nya-WSL"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["楠桐语录"],
}
__plugin_type__ = ("语录", 1)
__plugin_usage__ = """
usage：
    A：我觉得行
    bot：你行不了一点
""".strip()

send_img = on_command("我觉得行", priority=5, block=True)

ImagePath = IMAGE_PATH / "scu/easter_egg"
ListPath = Path() / "custom_plugins" / "i_think_is_ok" / "group_list.json"

if not os.path.exists(ImagePath):
    os.mkdir(ImagePath)

if not ListPath.exists():
    with open(ListPath, "w", encoding="utf-8") as gl:
        gl.write(r"[]")

@send_img.handle()
async def _(event: MessageEvent):
    with open(ListPath, "r", encoding="utf-8") as gl:
        GroupList = json.load(gl)
    if f"{event.group_id}" in GroupList:
        length = len(os.listdir(ImagePath))
        index = os.listdir(ImagePath)
        if length == 0:
            logger.warning(f"彩蛋图库为空，调用取消！")
            await send_img.finish("哥们没活了呜呜呜")
        img = random.choice(index)
        result = image("scu/easter_egg/" + str(img))
        if result:
            logger.info(
                f"发送:" + result,
                "发送图片",
                event.user_id,
                getattr(event, "group_id", None),
            )
            await send_img.send(result)
            flush = gc.collect()
            print(f"已成功清理内存：{flush}")
        else:
            logger.info(
                f"发送失败",
                "发送图片",
                event.user_id,
                getattr(event, "group_id", None),
            )
            await send_img.finish(f"发生错误！")
            flush = gc.collect()
            print(f"已成功清理内存：{flush}")
# Copyright (C) 2021 By VeezMusicProject

import cache.admins
from typing import List
import time 
from pyrogram.types import Chat
from cache.admins import get as gett
from cache.admins import set


async def get_administrators(chat: Chat) -> List[int]:
    if get := gett(chat.id):
        return get
    time.sleep(3) # control Flood wait 
    administrators = await chat.get_members(filter="administrators")
    to_set = [
        administrator.user.id
        for administrator in administrators
        if administrator.can_manage_voice_chats
    ]
    set(chat.id, to_set)
    return await get_administrators(chat)

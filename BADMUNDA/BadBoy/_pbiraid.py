import asyncio
from random import choice

from Sukh.pbiraid import PBIRAID, RPBIRAID
from pyrogram import Client, filters
from pyrogram.types import Message

from BADMUNDA.Config import *

from .. import sudos
from ..core.clients import *


@Client.on_message(filters.user(sudos) & filters.command(["praid"], prefixes=HANDLER))
async def pbiraid(Badmunda: Client, e: Message):
    usage = f"Command :- {HANDLER}Pbiraid (count) (reply to anyone)\nUsage :- `{HANDLER}Pbiraid 3 <reply to anyone>`\n\nCommand :- {HANDLER}Pbiraid <count> <username>\nUsage :- `{HANDLER}Pbiraid 3 @Hekeke`"
    lol = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    chat = e.chat
    try:
        counts = int(lol[0])
    except ValueError:
        return await e.reply_text(usage)
    if len(lol) == 2:
        if not counts:
            await e.reply_text(
                f"Gib Pbiraid Counts or use `{HANDLER}.upbiraid` for Unlimited Pbiraid!"
            )
            return
        owo = lol[1]
        if not owo:
            await e.reply_text(
                "you need to specify an user! Reply to any user or gime id/username"
            )
            return
        try:
            user = await Badmunda.get_users(lol[1])
        except:
            await e.reply_text("**Error:** User not found!")
            return
    elif e.reply_to_message:
        try:
            user = await Badmunda.get_users(e.reply_to_message.from_user.id)
        except:
            user = e.reply_to_message.from_user
    else:
        await e.reply_text(usage)
        return
    for _ in range(counts):
        pbiraid = choice(PBIRAID)
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_message(chat.id, f"{user.mention} {pbiraid}")
                await asyncio.sleep(0.3)
    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"started Pbiraid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id} \n Counts: {counts}",
            )
        except Exception as a:
            print(a)


USERS = []


@Client.on_message(
    filters.user(sudos) & filters.command(["prraid", "preplyraid"], prefixes=HANDLER)
)
async def rpbiraid(Badmunda: Client, e: Message):
    global USERS
    try:
        lol = e.text.split(" ", 1)[1].split(" ", 1)
    except IndexError:
        lol = None
    if e.reply_to_message and e.reply_to_message.from_user:
        user = e.reply_to_message.from_user
    elif lol:
        user_ = lol[0]
        if user_.isnumeric():
            user_ = int(user_)
        if not user_:
            return await e.reply_text(
                "I don't know who you're talking about, you're going to need to specify a user.!"
            )
        try:
            user = await Badmunda.get_users(user_)
        except (TypeError, ValueError):
            return await message.reply_text(
                "Looks like I don't have control over that user, or the ID isn't a valid one. If you reply to one of their messages, I'll be able to interact with them."
            )
    else:
        return await e.reply_text(
            "I don't know who you're talking about, you're going to need to specify a user...!"
        )
    if int(user.id) in USERS:
        return await e.reply_text("User already in Rpbiraid list!")
    USERS.append(user.id)
    mention = user.mention
    await e.reply_text(f"Reply Rpbiraid Activated On User {mention}")
    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"Activated Reply Rpbiraid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["draid", "dpraid", "dreplyraid"], prefixes=HANDLER)
)
async def dpbiraid(Badmunda: Client, e: Message):
    global USERS
    try:
        lol = e.text.split(" ", 1)[1].split(" ", 1)
    except IndexError:
        lol = None
    if e.reply_to_message and e.reply_to_message.from_user:
        user = e.reply_to_message.from_user
    elif lol:
        user_ = lol[0]
        if user_.isnumeric():
            user_ = int(user_)
        if not user_:
            await e.reply_text(
                "I don't know who you're talking about, you're going to need to specify a user.!"
            )
            return
        try:
            user = await Badmunda.get_users(user_)
        except (TypeError, ValueError):
            await message.reply_text(
                "Looks like I don't have control over that user, or the ID isn't a valid one. If you reply to one of their messages, I'll be able to interact with them."
            )
            return
    else:
        await e.reply_text(
            "I don't know who you're talking about, you're going to need to specify a user...!"
        )
        return
    if int(user.id) not in USERS:
        await e.reply_text("User not in Pbiraid list!")
        return
    USERS.remove(user.id)
    mention = user.mention
    await e.reply_text(f"Reply Pbiraid Deactivated Successfully On User {mention}")
    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f" Deactivated Reply Pbiraid By User: {e.from_user.id} \n\n User: {mention} \n Chat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["rlist", "raidlist"], prefixes=HANDLER)
)
async def rlist(Badmunda: Client, e: Message):
    global USERS
    _reply = "**Pbiraid users list - Pb Bot Spam** \n\n"
    if len(USERS) > 0:
        for x in USERS:
            try:
                user = await Badmunda.get_users(x)
                _reply += f" ✨ Users: {user.mention} \n"
            except:
                _reply += f" ✨ Users: [{x}](tg://user?id={x}) \n"
    else:
        await e.reply_text("Not yet!")
        return
    await e.reply_text(_reply)


@Client.on_message(filters.all)
async def checkraid(Badmunda: Client, msg: Message):
    global USERS
    if int(msg.from_user.id) in USERS:
        await msg.reply_text(choice(RPBIRAID))
          
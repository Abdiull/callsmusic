from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f'<b>👋🏻 Hi {message.from_user.mention()}!</b>\n\n'
        'I am Tlgrm Music bot, '
        'I let you play music in group calls.'
        '\n\nThe commands I currently support are:\n\n'
        '<b>/stop</b> - clear the queue and remove the userbot from the call',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '🔈 Channel', url='https://t.me/iSupCh',
                    ),
                    InlineKeyboardButton(
                        'Group 💬', url='https://t.me/iSupGr',
                    ),
                ],
            ],
        ),
    )

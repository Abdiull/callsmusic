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
        '<a href='https://telegra.ph/Tlgrm-music-commands-09-13'>Click here</a> to view commands I currently support\n\n'
        'Official bot repo:https://github.com/callsmusic/callsmusic',
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

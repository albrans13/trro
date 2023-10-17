from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""**- مرحبـاً بــك {name} ,

- فـي بـوت استخـراج كـود تيرمكـس
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه 🏂
- للحصـول على كـود تيرمكـس بـدون بـانـد🎗
» قم باختيـار نـوع الجلسـه الان
» لـ الحصـول على كـود ترمكس اضغـط الزر ( تلثيون)**
""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="اضـغط لـبدا آسـتـخـراج الــكـود🫵ْٖ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("قـنـاة ســورس ️", url="https://t.me/def_Zoka"),
  InlineKeyboardButton("مـطـوريـن الــبـوت ", url="https://t.me/def_Zoka/865"),
                ]
            ]
        ),
        disable_web_page_preview=True,
    )


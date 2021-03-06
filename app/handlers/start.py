from loader import BOT as bot, KEYBOARD_MAIN_MENU as MAIN_MENU   # noqa
from config import BOT_ADMIN, DIALOGUE    # noqa


@bot.message_handler(commands=["start"])
def start(message):
    if not message.from_user.id == int(BOT_ADMIN):
        text = DIALOGUE["no_admin"]
        bot.send_message(message.from_user.id, text)
    else:
        text = DIALOGUE["intro"]
        bot.send_message(message.from_user.id, text)
        text = DIALOGUE["hello_admin"]
        bot.send_message(message.from_user.id, text, reply_markup=MAIN_MENU)


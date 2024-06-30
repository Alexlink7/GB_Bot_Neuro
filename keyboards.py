from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/fox')
button3 = types.KeyboardButton(text='/weather')
button4 = types.KeyboardButton(text='/num')
button5 = types.KeyboardButton(text='/anecdote')


keyboard1 = [
    [button1, button2, button3],
    [button4, button5]
]

keyboard2 = [
    [button1, button2],
    [button3, button4],
    [button5]
]


kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=False)

# keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
# keyboard.add(button1, button2, button3)
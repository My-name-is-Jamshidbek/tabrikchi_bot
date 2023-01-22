from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



#kontaktni olish uchun butoon
keyboard_kontakt = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_kontakt.add(KeyboardButton(text="kontaktni ulashish", request_contact=True))

keyboard_tillar = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_tillar.add(
    KeyboardButton(text='🇬🇧'),
    KeyboardButton(text='🇺🇿'),
    KeyboardButton(text='🇷🇺'),
)
keyboard_menyu = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menyu.add(
    KeyboardButton(text="Tug'ilgan kun"),
    KeyboardButton(text="Yangi yil")
)
keyboard_menyu1 = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menyu1.add(
    KeyboardButton(text="Fonni ozgartirish"),
    KeyboardButton(text="Ismni ozgartirish"),
    KeyboardButton(text="Asosiy menyu")
)
keyboard_bekor_qilish = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_bekor_qilish.add(
    KeyboardButton(text="Bekor qilish")
)
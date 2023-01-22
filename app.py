from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from loader import bot
from aiogram.dispatcher import FSMContext
from states import Main
from btn import keyboard_kontakt, keyboard_tillar, keyboard_menyu, keyboard_bekor_qilish, keyboard_menyu1
from func import add_contact,read_contact,tek_id
from writer import write_text
import time
@dp.message_handler(CommandStart())
async def start(message: types.Message, state: FSMContext):
    if tek_id(message.from_user.id):
        await message.answer("Kerakli menyuni tanlang:", reply_markup=keyboard_menyu)
        await Main.menu_tanlash.set()
    else:
        await message.answer('Assalomu aleykum botga xush kelibsiz!\nBot ishda davom etishi uchun iltimos kantaktni ulashish tugmasiga bosing.',reply_markup=keyboard_kontakt)
        await Main.kontaktni_ulashish.set()
@dp.message_handler(state=Main.kontaktni_ulashish, content_types=types.ContentType.CONTACT)
async def kontaktni_olish(message: types.Message, state: FSMContext):
    add_contact(dict(message.contact))
    await message.answer("Kerakli menyuni tanlang:",reply_markup=keyboard_menyu)
    await Main.menu_tanlash.set()
@dp.message_handler(state=Main.menu_tanlash, content_types=types.ContentType.TEXT)
async def kontaktni_olish(message: types.Message, state: FSMContext):
    m = message.text
    a = 'ny'
    if m=="Yangi yil":a = 'ny'
    elif m=="Tug'ilgan kun":a = 'hp'
    await state.update_data(menu = a)
    await message.answer('Iltimos tabrik tilini tanlang:',reply_markup=keyboard_tillar)
    await Main.tilni_tanlash.set()
@dp.message_handler(state=Main.tilni_tanlash, content_types=types.ContentType.TEXT)
async def tilni_tanlash(message: types.Message, state:FSMContext):
    m = message.text
    if m == '🇬🇧':lan = 'en'
    elif m == '🇺🇿':lan = 'uz'
    elif m == '🇷🇺':lan = 'ru'
    else:lan = 'uz'
    await state.update_data(lan=lan)
    await message.answer("Tabrik uchun ism kiriting:",reply_markup=keyboard_bekor_qilish)
    await Main.tabrik_ismi.set()
@dp.message_handler(state=Main.tabrik_ismi, content_types=types.ContentType.TEXT)
async def kontaktni_olish(message: types.Message, state: FSMContext):
    if message.text == "Bekor qilish":
        await message.answer("Bekor qilindi.",reply_markup=keyboard_menyu)
        await Main.menu_tanlash.set()
    else:
        m = message.text
        await state.update_data(ism=m)
        await state.update_data(rasm=1)

        mal = await state.get_data()
        rasm = mal.get("rasm")
        print(rasm)
        lan = mal.get('lan')
        a = write_text(id = message.from_user.id, title_text=m, lan=lan)
        time.sleep(6)
        await message.answer_photo(photo=open(str('base/'+str(message.from_user.id)+"/photos/"+str(rasm)+'.jpg'),"rb"),
                                   caption='rasm',
                                   reply_markup=keyboard_menyu1)
        await Main.menyu_tanlash1.set()
@dp.message_handler(state=Main.menyu_tanlash1, content_types=types.ContentType.TEXT)
async def kontaktni_olish(message: types.Message, state: FSMContext):
    m = message.text
    if m == "Fonni ozgartirish":
        mal = await state.get_data()
        rasm = mal.get("rasm")+1
        await state.update_data(rasm = rasm)
        await message.answer_photo(photo=open(str('base/'+str(message.from_user.id)+"/photos/"+str(rasm)+'.jpg'),"rb"),
                                   caption='rasm',
                                   reply_markup=keyboard_menyu1)
        await Main.menyu_tanlash1.set()
    elif m == "Ismni ozgartirish":
        await message.answer("Yangi ismni kiriting:",reply_markup=keyboard_bekor_qilish)
        await Main.tabrik_ismi.set()
    else:
        await message.answer("Asosiy menyu.",reply_markup=keyboard_menyu)
        await Main.menu_tanlash.set()
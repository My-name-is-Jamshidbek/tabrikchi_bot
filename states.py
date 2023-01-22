from aiogram.dispatcher.filters.state import State, StatesGroup




class Main(StatesGroup):
    kontaktni_ulashish = State()
    lan = "uz"
    tilni_tanlash = State()
    menu = 'ny'
    menu_tanlash = State()
    ism = 'Jamshidbek'
    tabrik_ismi = State()
    rasm = 1
    menyu_tanlash1 = State()

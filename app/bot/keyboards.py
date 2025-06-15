from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Информация об организации", callback_data="info_org")],
        [InlineKeyboardButton(text="Продукты", callback_data="products")],
        [InlineKeyboardButton(text="Контакты", callback_data="contacts")]
    ])
    return keyboard

def product_categories_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        # Захардкоженные категории – в будущем можно заменить динамическим получением
        [InlineKeyboardButton(text="Микроэлектроника", callback_data=f"cat_Микроэлектроника")],
        [InlineKeyboardButton(text="Модули", callback_data=f"cat_Модули")],
        [InlineKeyboardButton(text="ПАК (Программно-аппаратный комплекс)", callback_data=f"cat_ПАК")],
        [InlineKeyboardButton(text="Назад", callback_data="back_main")],
    ])
    return keyboard

def products_keyboard(category: str, products: list) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=
        [[InlineKeyboardButton(text=product["name"], callback_data=f"prod_{product['id']}")] for product in products] +
        [[InlineKeyboardButton(text="Назад", callback_data="back_main")]]
    )
    return keyboard

def product_detail_keyboard(product_id: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Заказать", callback_data=f"order_{product_id}")],
        [InlineKeyboardButton(text="В главное меню", callback_data="back_main")],
    ])
    return keyboard

def back_to_main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="В главное меню", callback_data="back_main")],
    ])
    return keyboard

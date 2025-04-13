from aiogram import Router, types
from bot.keyboards import (
    main_menu_keyboard,
    product_categories_keyboard,
    products_keyboard,
    product_detail_keyboard,
    back_to_main_menu_keyboard,
)
from bot.services import (
    get_company_info, get_contacts_info,
    get_products_by_category, get_product_detail,
)

router = Router()

@router.callback_query()
async def menu_handler(callback_query: types.CallbackQuery):
    data = callback_query.data

    if data == 'info_org':
        text = get_company_info()
        await callback_query.message.edit_text(text, reply_markup=back_to_main_menu_keyboard())
    elif data == 'contacts':
        text = get_contacts_info()
        await callback_query.message.edit_text(text, reply_markup=back_to_main_menu_keyboard())
    elif data == 'products':
        keyboard = product_categories_keyboard()
        await callback_query.message.edit_text("Выберите категорию продуктов:", reply_markup=keyboard)
    elif data.startswith('cat_'):
        category = data[len('cat_'):]
        products = get_products_by_category(category)
        if products:
            keyboard = products_keyboard(category, products)
            await callback_query.message.edit_text(f"Продукты категории '{category}':", reply_markup=keyboard)
        else:
            await callback_query.answer("Продукты не найдены", show_alert=True)
    elif data.startswith('prod_'):
        product_id = data[len('prod_'):]
        detail = get_product_detail(product_id)
        if detail:
            # Используем клавиатуру для деталей продукта с кнопкой "Заказать"
            keyboard = product_detail_keyboard(product_id)
            await callback_query.message.edit_text(detail, reply_markup=keyboard)
        else:
            await callback_query.answer("Информация о продукте не найдена", show_alert=True)
    elif data.startswith('order_'):
        # Обработка заказа
        await callback_query.message.edit_text("Перевожу вас на оператора.", reply_markup=back_to_main_menu_keyboard())
    elif data == 'back_main':
        await callback_query.message.edit_text("Главное меню", reply_markup=main_menu_keyboard())
    elif data == 'back_products':
        keyboard = product_categories_keyboard()
        await callback_query.message.edit_text("Выберите категорию продуктов:", reply_markup=keyboard)
    else:
        await callback_query.answer("Неизвестная команда", show_alert=True)
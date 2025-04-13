from static.data import COMPANY_INFO, CONTACTS_INFO, PRODUCTS

def get_welcome_message() -> str:
    return "Вас приветствует бот компании МОДУЛЬ"

def get_company_info() -> str:
    return COMPANY_INFO

def get_contacts_info() -> str:
    return CONTACTS_INFO

def get_products_by_category(category: str) -> list:
    return [p for p in PRODUCTS if p["category"] == category]

def get_product_detail(product_id: str) -> str:
    product = next((p for p in PRODUCTS if str(p["id"]) == product_id), None)
    if product:
        description = product.get("description", "Описание отсутствует")
        price = product.get("price", "Не указана")
        # Добавляем цену в отдельной строке
        return f"{description}\nЦена: {price}"
    return ""
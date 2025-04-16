from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Category, Product
from app.static.data import COMPANY_INFO, CONTACTS_INFO, PRODUCTS


def get_welcome_message() -> str:
    return "Вас приветствует бот компании МОДУЛЬ"

def get_company_info() -> str:
    return COMPANY_INFO

def get_contacts_info() -> str:
    return CONTACTS_INFO

async def get_products_by_category(category: str) -> list:
    """
    Возвращает список товаров в заданной категории.
    Результат приводится к списку словарей с ключами 'id', 'name', 'description', 'price', 'category'.
    """
    stmt = select(Product).join(Category).where(Category.name == category)
    async with get_db() as db_session:
        result = await db_session.execute(stmt)
    products = result.scalars().all()

    products_list = [
        product.__dict__
        for product in products
    ]
    return products_list

async def get_product_detail(product_id: str) -> str:
    """
    Возвращает детальное описание товара по его идентификатору.
    Описание включает информацию о товаре и его цене.
    """
    stmt = select(Product).where(Product.id == int(product_id))
    async with get_db() as db_session:
        result = await db_session.execute(stmt)
    product = result.scalar_one_or_none()
    
    if product:
        description = product.description or "Описание отсутствует"
        price = product.price or "Не указана"
        return f"{description}\nЦена: {price} руб."
    
    return ""
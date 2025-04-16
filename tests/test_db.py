import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from app.models import Category, Product
from app.static.data import PRODUCT_CATEGORIES, PRODUCTS
from app.database import engine, init_db

# Фикстура для инициализации схемы в базе (создание таблиц, если их ещё нет)
@pytest.yield_fixture()
async def setup_db():
    await init_db()
    yield

# Фикстура, создающая сессию с транзакцией, которая будет откатана после теста
@pytest.yield_fixture()
async def db_session() -> AsyncSession:
    async_session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    session: AsyncSession = async_session_factory()
    try:
        yield session
    finally:
        # Фиксируем все изменения и закрываем сессию
        await session.commit()
        await session.close()

# Асинхронный тест, который использует асинхронную сессию
@pytest.mark.asyncio
async def test_insert_products_and_categories(db_session: AsyncSession):
    # Словарь для хранения добавленных категорий по имени
    category_map = {}

    # Добавление категорий из данных
    for cat_name in PRODUCT_CATEGORIES:
        category = Category(name=cat_name)
        db_session.add(category)
        await db_session.flush()
        category_map[cat_name] = category
    await db_session.commit()

    # Добавление продуктов с привязкой к соответствующей категории
    for product_data in PRODUCTS:
        # По названию получаем соответствующий объект категории
        cat = category_map.get(product_data["category"])
        product = Product(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            category=cat
        )
        db_session.add(product)
    await db_session.commit()

    # Проверяем количество записей в таблице categories
    result_cat = await db_session.execute(text("SELECT COUNT(*) FROM categories"))
    count_categories = result_cat.scalar()
    # Проверяем количество записей в таблице products
    result_prod = await db_session.execute(text("SELECT COUNT(*) FROM products"))
    count_products = result_prod.scalar()

    assert count_categories == len(PRODUCT_CATEGORIES), (
        f"Ожидалось {len(PRODUCT_CATEGORIES)} категорий, найдено {count_categories}"
    )
    assert count_products == len(PRODUCTS), (
        f"Ожидалось {len(PRODUCTS)} продуктов, найдено {count_products}"
    )
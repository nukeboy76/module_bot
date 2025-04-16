from app.bot.handlers.start import router as start_router
from app.bot.handlers.menu import router as menu_router

def register_handlers(dp):
    dp.include_router(start_router)
    dp.include_router(menu_router)
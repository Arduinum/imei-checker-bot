from aiogram.fsm.state import State, StatesGroup


class ImeiForm(StatesGroup):
    """Класс форма для получения imei"""
    
    IMEI = State()

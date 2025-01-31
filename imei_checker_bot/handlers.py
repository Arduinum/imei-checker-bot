from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command


router = Router(name=__name__)


@router.message(Command(commands='help'))
async def help_command(message: Message) -> None:
    """Асинхронная функция для отправки сообщения со списком команд"""

    text = ('Меню help:\n\n'
        '/help - список доступных команд\n'
        '/info - информация о боте\n'
        '/check_imei - проверить imei устройства')
    await message.answer(text=text, parse_mode=None)


@router.message(Command(commands='info'))
async def info_command(message: Message) -> None:
    """Асинхронная функция для отправки сообщения информации о боте"""

    text = ('Бот IMEI-Checker info:\n\n'
        'Здесь вы можете проверить IMEI устройства.\n'
        'Для получения полного списка команд отправьте /help')
    await message.answer(text=text, parse_mode=None)


@router.message(Command(commands='check_imei'))
async def check_imei_command(message: Message) -> None:
    """Асинхронная функция для проверки imei устройства"""

    text = 'check_imei'
    await message.answer(text=text, parse_mode=None)

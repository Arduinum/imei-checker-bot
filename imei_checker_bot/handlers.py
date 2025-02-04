from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from imei_checker_bot.views import get_imei_view
from imei_checker_bot.states import ImeiForm
from imei_checker_bot.cruds import check_chat_id


router = Router(name=__name__)


@router.message(CommandStart())
async def start_command(message: Message) -> None:
    """Асинхронная функция для отправки приветственного сообщения"""

    chat_id = await check_chat_id(chat_id=message.chat.id)

    if not chat_id:
        await message.answer(text='У вас ограничен доступ к функционалу бота!')
    else:
        person_title = f"{message.chat.first_name} {message.chat.last_name}" \
            if message.chat.last_name else message.chat.first_name
        text = ('добро пожаловать в бот IMEI-Checker info:\n\n'
            'Здесь вы можете проверить IMEI устройства.\n'
            'Для получения полного списка команд отправьте /help')
        await message.answer(text=f'{person_title} {text}')


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
async def check_imei_command(message: Message, state: FSMContext) -> None:
    """Запрос у пользователя ввода IMEI и установка состояния"""
    
    chat_id = await check_chat_id(chat_id=message.chat.id)
    
    if chat_id:
        await message.answer("Введите IMEI устройства:")
        await state.set_state(ImeiForm.IMEI)
    else:
        await message.answer(text='У вас нет доступа к данному функционалу!')


@router.message(ImeiForm.IMEI, F.text.regexp(r'^\d{15}$'))
async def receive_imei(message: Message, state: FSMContext) -> None:
    """Обработчик для получения данных устройства по imei"""

    imei = message.text
    text = await get_imei_view(imei=imei)
    
    await message.answer(text=text, parse_mode=None)
    await state.clear()

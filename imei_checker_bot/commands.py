from aiogram.types import BotCommand, BotCommandScopeDefault

from imei_checker_bot.settings import bot


async def register_commands():
    commands = [
        BotCommand(
            command='info',
            description='информация о боте'
        ),
        BotCommand(
            command='help',
            description='список доступных команд'
        ),
        BotCommand(
            command='check_imei',
            description='проверка imei устройства'
        )
    ]


    await bot.set_my_commands(
        commands=commands, 
        scope=BotCommandScopeDefault()
    )

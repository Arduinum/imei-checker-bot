import aiohttp
import json

from imei_checker_bot.logger import logger
from imei_checker_bot.settings import settings


logger.name = __name__


async def get_imei_view(imei: str) -> str | None:
    """Асинхронная view для получения imei устройства"""
    
    headers = {
        'Authorization': 'Bearer ' + settings.token_authorization.get_secret_value(),
        'Content-Type': 'application/json'
    }
    
    payload = {
        'deviceId': str(imei),
        'serviceId': settings.service_id
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            settings.api_url, 
            headers=headers, 
            json=payload
        ) as response:
            if response.status == 201:
                data = await response.json()
                
                # получаем данные об устройстве из json
                device_properties = data.get('properties', {})
                
                str_divice = 'Данные об устройстве:\n\n'
                
                for key, value in device_properties.items():
                    str_divice += f'{key}: {value}\n'

                return str_divice
            else:
                logger.warning(
                    f'Неверный статус ответа: {response.status}, {settings.api_url}'
                )


if __name__ == '__main__':
    from asyncio import run

    run(get_imei_view(imei='358858458854584'))

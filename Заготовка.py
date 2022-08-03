import io, inspect
from .. import loader, utils
from asyncio import sleep

@loader.tds
class DerevoMod(loader.Module):
    """Описание модуля"""
    strings = {'name': 'aboba'}
    
    async def commandcmd(self, message):

     a = utils.get_args_raw(message)
     for i in range(int(a)):
        await message.client.send_message(message.to_id, "Видеокарты 🔮")
        await message.client.send_message(message.to_id, "Настройки видеокарты")
        await message.client.send_message(message.to_id, f'{i+1}')
        await message.client.send_message(message.to_id, "Смазать 🛢")
    

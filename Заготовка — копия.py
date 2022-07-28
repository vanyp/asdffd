import io, inspect
from .. import loader, utils
from asyncio import sleep

@loader.tds
class DerevoMod(loader.Module):
    """Описание модуля"""
    strings = {'name': 'abob123a'}
    
    async def termcmd(self, message):

     a = utils.get_args_raw(message)
     for i in range(int(a)):
        await message.client.send_message(message.to_id, "Термопаста 🛢")
        await sleep(0.1)

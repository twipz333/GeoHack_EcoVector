from aiogram.dispatcher import FSMContext


async def mk_dict(message, state):
    async with state.proxy() as proxy:
        print(message.text)

import discord
from classRoomClear import getAllRooms

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$ledig'):
            await message.channel.send(getAllRooms())




client = MyClient()
client.run('your token here')
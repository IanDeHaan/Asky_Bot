import discord
import query_asky

class asky(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.split()[0].lower() == '!asky':
            message_split = message.content.split()
            if len(message_split) == 1:
                await message.channel.send("```Gimme a search term =^..^=```")
            else:
                searchTerm = " ".join(message.content.split()[1:])
                await message.channel.send('```' + query_asky.query(searchTerm) + '```')

client = asky()
client.run('xxxxxxxxxxxxxxxx')
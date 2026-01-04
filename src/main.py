import discord
import dotenv

import pathlib

class Client(discord.Client):
    def __init__(self):
        intents = discord.Intents.none()
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)
    
    async def setup_hook(self):
        await self.tree.sync()
    
if __name__ == "__main__":
    client = Client()
    client.run(dotenv.get_key(pathlib.Path(__file__).parent.joinpath(".env"), "DISCORD_TOKEN"))

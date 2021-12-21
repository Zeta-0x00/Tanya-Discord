from discord.ext import commands
from commands import *

Tanya_Token = '<Bot token>'

# Whitelist order ID
Tanya_whitelist = [] # Here you can add the IDs of the users allowed to bypass the AntiScam system.
Tanya_logs_channel = 0000000000 # Here you can add the ID of the channel where the logs will be sent.
Tanya = commands.Bot(command_prefix='>')
Tanya.remove_command('help') # Remove this line if you want to use the help command.


@Tanya.listen()
async def on_message(message):
    await listening(message=message, bot=Tanya, botname='tanya', whitelist=Tanya_whitelist, muted_role='muted', verified_role='verified', logs_channel = Tanya_logs_channel)


Tanya.run(Tanya_Token)

from AntiScam import AntiScam
from discord.ext import commands
import discord

async def sudo_cmd(message,bot, botname):
    if botname == 'tanya':
        if message.content.lower() == 'sudo rules':
            channel = bot.get_channel('Rules Channel ID')
            with open('Rules.txt') as file:
                dat = file.read()
                msj = discord.Embed(title="**__Titulo en Markdown__**", description=dat, color=0xFF5733)
                await channel.send(embed=msj)
        if message.content.lower() == 'sudo willkommen':
            channel = bot.get_channel('Bienvenida channel ID')
            with open('Bienvenida.txt') as file:
                dat = file.read()
                msj = discord.Embed(title='**__Bienvenida!__**', description = dat, color=0xFF5733)
                await channel.send(embed=msj)
        if message.content.lower() == 'sudo verifiedmessage':
            channel = bot.get_channel('check channel ID')
            with open('Verified.txt') as file:
                dat = file.read()
                msj = discord.Embed(title='**__titulo__**', description=dat, color=0xFF5733)
                await channel.send(embed=msj)



async def listening(message, bot, botname, whitelist, muted_role, verified_role, logs_channel):
	message_content = f'{message.author.id}: {message.content}'
	message_content = message_content.replace("'", "`")
	#test sudo
	if message.author.id in whitelist and message.content.startswith('sudo'):
		await sudo_cmd(message,bot, botname)
	await AntiScam(message, bot = bot, whitelist = whitelist, muted_role=muted_role, verified_role=verified_role, logs_channel=logs_channel) # Here you can change the names of the roles.
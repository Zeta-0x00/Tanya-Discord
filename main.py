from distutils.log import info
from pydoc import describe
from AntiScam import AntiScam
import os
import discord
from discord import client
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.members = True
intents.bans = True

bot = commands.Bot(command_prefix=">", intents=intents)
bot.remove_command("help")

####### Evenvts Bot ###########

@bot.event
async def on_ready():
    print(f"=" * 25)
    print(f"{bot.user.name} is ready : its id is {bot.user.id}")
    print(f"=" * 25)

 ## https://discord.com/api/oauth2/authorize?client_id=916727164605456426&permissions=8&scope=bot
@bot.event
async def on_guild_join(guild):

    bot_entry = await guild.audit_logs(action=discord.AuditLogAction.bot_add).flatten()
    print(bot_entry)
    inviter = bot_entry[0].user
    guild = bot_entry[0].guild

    embed = discord.Embed(title=f"Thanks for add me to your server {inviter}",
                          description="If you want to setup in your server.", color=discord.Color.from_rgb(255, 153, 204))
    embed.set_thumbnail(url="https://i.imgur.com/HWeXztQ.gif")
    embed.add_field(
        name="Prefix", value="The prefix for the bot is **>**.\n**Put** ```>help : For more information in your server ```", inline=True)
    embed.set_author(name=f"{bot.user.name}", icon_url=f"{bot.user.avatar_url}")
    
    embed.set_footer(
        text=f"{bot.user.name}", icon_url=f"{bot.user.avatar_url}")

    await bot_entry[0].user.send(embed=embed)


####### Listen Bot ########

@bot.listen()
async def on_message(message):
    await AntiScam(message, bot=bot) # Here you can change the names of the roles.


####### Help command and other commands that need help for show it info of how to use ##########

@bot.group(invoke_without_command=True)
@commands.has_permissions(send_messages=True)
async def help(ctx):
    url = bot.user.avatar_url_as()
    embed = discord.Embed(title=f"{bot.user.name}", description=f"These are the commands for setup the bot and his feature of AntiScam.", color=discord.Color.dark_magenta())
    embed.set_author(name = f"{ctx.author.name}", icon_url= f"{ctx.author.avatar_url}")
    embed.set_thumbnail(url=url)
    embed.add_field(name=":bat: Commands:",
                    value= info, inline=False)
    embed.add_field(
        name="Warning", value="If you want to know how to use one comman put\n**>help COMMAND**")
    embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


@help.command()
@commands.has_permissions(send_messages=True)
async def white(ctx):
    embed = discord.Embed(title=f"Command >white", description=f"`>white @USERNAME` **:** The command put the user in the whitelist\nThe name is necesessary")
    embed.add_field(name=":bat: Example: ", value="```>white @Ashor```", inline=False)
    embed.set_footer(text=f"{ctx.guild.name}",
                     icon_url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


@help.command()
@commands.has_permissions(send_messages=True)
async def black(ctx):
    embed = discord.Embed(title=f"Command >black",
                          description=f"`>black @USERNAME` **:** The command put the user in the blacklist\nThe name is necesessary")
    embed.add_field(name=":bat: Example: ",
                    value="```>black @Ashor```", inline=False)
    embed.set_footer(text=f"{ctx.guild.name}",
                     icon_url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


@help.command()
@commands.has_permissions(send_messages=True)
async def log(ctx):
    embed = discord.Embed(title=f"Command >log",
                          description=f"`>log ID` **:** The command the id of the channel that will send the logs\nThis is optional")
    embed.add_field(name=":bat: Example: ",
                    value="```>log 916768044670406706```", inline=False)
    embed.set_footer(text=f"{ctx.guild.name}",
                     icon_url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


@help.command()
@commands.has_permissions(send_messages=True)
async def role_mute(ctx):
    embed = discord.Embed(title=f"Command >role_mute",
                          description=f"`>role_mute name_rola` **:** The command save the name of the role mute\nThe name is necesessary")
    embed.add_field(name=":bat: Example: ",
                    value="```>role_mute Muted```", inline=False)
    embed.set_footer(text=f"{ctx.guild.name}",
                     icon_url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


@help.command()
@commands.has_permissions(send_messages=True)
async def veri_role(ctx):
    embed = discord.Embed(title=f"Command >veri_role",
                          description=f"`>veri_role name_role` **:** The command save the name of the role verificated\nThe name is necesessary")
    embed.add_field(name=":bat: Example: ",
                    value="```>veri_role Verificado``", inline=False)
    embed.set_footer(text=f"{ctx.guild.name}",
                     icon_url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


#### Main function #####

def main():
    with open("./config.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()
    print(data)
    bot_token = data["TOKEN_BOT"]
    bot.run(bot_token)


##### Commands #####

@bot.command()
async def white(ctx, user: discord.Member):
    with open("./config.json", "r+", encoding="utf-8") as file:
        data = json.load(file)
        data["white_list"].append(int(user.id))
        file.seek(0)
        json.dump(data, file, indent=4)
        file.close()
    embed = discord.Embed(
        title=f"Info", description=f"{ctx.author.name} added this id {id} to the white list")
    embed.set_author(name=f"{ctx.author.name}",
                     icon_url=f"{ctx.author.avatar_url}")
    embed.set_footer(text=f"{ctx.guild.name}",
                     icon_url=f"{ctx.guild.icon_url}")
    await ctx.channel.send(embed=embed)


@bot.command()
async def black(ctx, user: discord.Member):
    with open("./config.json", "r+", encoding="utf-8") as file:
        data = json.load(file)
        data["black_list"].append(int(user.id))
        file.seek(0)
        json.dump(data, file, indent=4)
        file.close()
    embed = discord.Embed(
        title=f"Info", description=f"{ctx.author.name} added this id {id} to the black list")
    embed.set_author(name=f"{ctx.author.name}",
                     icon_url=f"{ctx.author.avatar_url}")
    embed.set_footer(text=f"{ctx.guild.name}",
                     icon_url=f"{ctx.guild.icon_url}")
    await ctx.channel.send(embed=embed)


@bot.command()
async def log(ctx, id:int):
    with open("./config.json", "r+", encoding="utf-8") as file:
        data = json.load(file)
        data["LOG_CHANNEL"] = id
        file.seek(0)
        json.dump(data, file, indent=4)
        file.close()
    embed = discord.Embed(
        title=f"Info", description=f"{ctx.author.name} added this id {id} as channel to send messages")
    embed.set_author(name=f"{ctx.author.name}",
                     icon_url=f"{ctx.author.avatar_url}")
    embed.set_footer(text=f"{ctx.guild.name}",
                     icon_url=f"{ctx.guild.icon_url}")
    await ctx.channel.send(embed=embed)


@bot.command()
async def mute_role(ctx, name: str):
    with open("./config.json", "r+", encoding="utf-8") as file:
        data = json.load(file)
        data["mute_role"] = str(name)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.close()
    embed = discord.Embed(
        title=f"Info", description=f"{ctx.author.name} added the role {name} as Mute role")
    embed.set_author(name=f"{ctx.author.name}",
                     icon_url=f"{ctx.author.avatar_url}")
    embed.set_footer(text=f"{ctx.guild.name}",
                     icon_url=f"{ctx.guild.icon_url}")
    await ctx.channel.send(embed=embed)


@bot.command()
async def veri_role(ctx, name: str):
    with open("./config.json", "r+", encoding="utf-8") as file:
        data = json.load(file)
        data["veri_role"] = str(name)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.close()
    embed = discord.Embed(title=f"Info", description=f"{ctx.author.name} added the role {name} as Verificated role")
    embed.set_author(name=f"{ctx.author.name}",
                     icon_url=f"{ctx.author.avatar_url}")
    embed.set_footer(text=f"{ctx.guild.name}",
                     icon_url=f"{ctx.guild.icon_url}")
    await ctx.channel.send(embed=embed)


##### info que se utiliza en el comando help #####

info = f""" `whitelist` **:** >white
`blacklist` **:** >black
`log channel` **:** >log
`Muted role` **:** >role_mute
`verifiques role` **:** >veri_role"""


if __name__=="__main__":
    main()


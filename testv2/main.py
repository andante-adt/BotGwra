from discord.ext import commands
import time
from discord import FFmpegPCMAudio
from apikuey import *
import youtube_dl
import discord
import os
import random


client = commands.Bot(command_prefix="?", help_command=None)
# client.remove_command('help')


@client.event
async def on_ready():
    print('login!!!')
    print('========') 


@client.command()
async def hi(ctx):
    await ctx.send("hi gwra have come.")


@client.command()
async def thx(ctx):
    await ctx.send("nevermind.")


@client.command()
async def help(ctx):
    # help
    # send
    emBed = discord.Embed(title="ขอโทษนะคะ กุระกำลังอยู่ในช่วงพัฒนาตน.", description="all available bot commands", color=0x03e3fc)
    emBed.add_field(name="help", value="?hi  ?papa  ?sing  ?join  ?leave  ?tictactoe  ?thx  ?thai  ?oni" ,inline=False)
    emBed.add_field(name="send", value="Gwraaaaa", inline=False)
    emBed.set_thumbnail(url='https://w.wallhaven.cc/full/o3/wallhaven-o399j7.png')
    emBed.set_footer(text="ขอโทษนะคะTvT", icon_url="https://static.wikia.nocookie.net/virtualyoutuber/images/3/31/Gawr_Gura_Mini_Model_%28by_Walfie%29.png/revision/latest/scale-to-width-down/405?cb=20210811060627")
    emBed.set_image(url="https://i.pinimg.com/originals/d9/71/e3/d971e35a985da5def9ddccd6bbc6df6a.png")
    await ctx.channel.send(embed=emBed)


@client.command(pass_context = True)
async def papa(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('gwra-papa.mp3')
        player = voice.play(source)
        time.sleep(5)
        await ctx.guild.voice_client.disconnect()

    else:
        await ctx.send('อยุ่ไหนอะ?')


@client.command(pass_context = True)
async def sing(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('gura-song.mp3')
        player = voice.play(source)
        time.sleep(18)
        await ctx.guild.voice_client.disconnect()

    else:
        await ctx.send('อยุ่ไหนอะ?')



@client.command(pass_context = True)
async def thai(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('thai.mp3')
        player = voice.play(source)
        time.sleep(15)
        await ctx.guild.voice_client.disconnect()

    else:
        await ctx.send('อยุ่ไหนอะ?')


@client.command(pass_context = True)
async def oni(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('oni.mp3')
        player = voice.play(source)
        time.sleep(6)
        await ctx.guild.voice_client.disconnect()

    else:
        await ctx.send('อยุ่ไหนอะ?')


@client.command(pass_context = True)
async def wakeup(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('wake-up.mp3')
        player = voice.play(source)
        time.sleep(37)
        await ctx.guild.voice_client.disconnect()

    else:
        await ctx.send('อยุ่ไหนอะ?')


@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send("haha i'm here.")
    else:
        await ctx.send("กุระมองไม่เห็นว่าคุณอยู่ไหน😢.")


@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Byeeeee.")
    else:
        await ctx.send("Ummm.")


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        await ctx.send("ขอเวลากุระสักครู่"), await ctx.send("."), await ctx.send("."), await ctx.send(".")
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("นี้ตาของคุณ <@" + str(player1.id) + ">")
        elif num == 2:
            turn = player2
            await ctx.send("ตอนนี้ตาคุณ <@" + str(player2.id) + ">")
    else:
        await ctx.send("โปรดเล่นเกมนี้ให้จบก่อนนะ ไม่งั้นกุระจะโกรธคุณเอานะ.")


@client.command()
async def p(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " เก่งจังเล่นชนะด้วย!!!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("พอแค่นั้นแหละ!!!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("เล่นเป็นป่าวเนี้ย.")
        else:
            await ctx.send("หยุดเลยนะนี้ไม่ใช่ตาของคุณ.")
    else:
        await ctx.send("โปรดใช้คำสั่งนี้เพื่อเริ่มเกม !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โปรดระบุผู้เล่น 2 คนสำหรับคำสั่งนี้")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("โปรดระบุ/@ผู้เล่น (เช่น <@ชื่อ>)")



client.run(Token)
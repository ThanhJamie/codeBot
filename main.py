
import time
import asyncio
import discord
from discord import Intents

intents = Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Chào mừng bạn đến với trò chơi giải mật thư!')
        await message.channel.send('Để nắm rõ các câu lệnh để bắt đầu trò chơi vui lòng gõ theo cú pháp !help')

    if message.content.startswith('!help'):
        await message.channel.send('Chào mừng bạn đến với trò chơi giải mật thư (Made by Thanh)!')
        await message.channel.send('Nhiệm vụ của bạn là lần lượt phải giải qua từng vòng mật thư và mỗi vòng bạn sẽ nhận được một số . Ghép những con số sẽ ra đáp án cuối cùng của trò chơi')

        await message.channel.send('Để bắt đầu trò chơi vui lòng gõ theo cú pháp`!start1`')
        await message.channel.send('Sao khi giải được câu đố của mỗi vòng vui lòng gõ theo cú pháp dể kiểm tra kêt quả`!round1 {đáp án của bạn}`')

        # Round 1
    if message.content.startswith('!start1'):
        file = discord.File("./test.png", filename="test.png")
        await message.channel.send("Starting round 1", file=file)
        await message.channel.send('Sao khi giải được câu đố của mỗi vòng vui lòng gõ theo cú pháp dể kiểm tra kêt quả`!round1 {đáp án của bạn}`')
    if message.content.startswith('!round1 Present') or message.content.startswith('!round1 present') or message.content.startswith('!round1 PRESENT'):
        await message.channel.send('Wait to check the answer: 5s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 4s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 3s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 2s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 1s!')
        await asyncio.sleep(1)
        await message.channel.send("Xin chúc mừng bạn đã vượt qua vòng 1!")
        await asyncio.sleep(1)
        await message.channel.send("Keyword : 0")
        await asyncio.sleep(1)
        await message.channel.send('Để bắt đầu vòng tiếp theo vui lòng gõ theo cú pháp`!start2`')
    # Round 2
    if message.content.startswith('!start2'):
        file = discord.File("./test.png", filename="test.png")
        await message.channel.send("Starting round 2", file=file)
        await message.channel.send('Sao khi giải được câu đố của mỗi vòng vui lòng gõ theo cú pháp dể kiểm tra kêt quả`!round2 {đáp án của bạn}`')
    if message.content.startswith('!round2 Google Meet') or message.content.startswith('!round2 GOOGLE MEET') or message.content.startswith('!round2 google meet'):
        await message.channel.send('Wait to check the answer: 5s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 4s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 3s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 2s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 1s!')
        await asyncio.sleep(1)
        await message.channel.send("Xin chúc mừng bạn đã vượt qua vòng 2!")
        await asyncio.sleep(1)
        await message.channel.send("Keyword : 0")
        await asyncio.sleep(1)
        await message.channel.send('Để bắt đầu vòng tiếp theo vui lòng gõ theo cú pháp`!start3`')

    # Round 3
    if message.content.startswith('!start3'):
        file = discord.File("./test.png", filename="test.png")
        await message.channel.send("Starting round 3", file=file)
        await message.channel.send('Sao khi giải được câu đố của mỗi vòng vui lòng gõ theo cú pháp dể kiểm tra kêt quả`!round3 {đáp án của bạn}`')
    if message.content.startswith('!round3 LC Coffee') or message.content.startswith('!round3 lc coffee') or message.content.startswith('!round3  LC COFFEE'):
        await message.channel.send('Wait to check the answer: 5s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 4s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 3s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 2s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 1s!')
        await asyncio.sleep(1)
        await message.channel.send("Xin chúc mừng bạn đã vượt qua vòng 3!")
        await asyncio.sleep(1)
        await message.channel.send("Keyword : 6")
        await asyncio.sleep(1)
        await message.channel.send('Để bắt đầu vòng tiếp theo vui lòng gõ theo cú pháp`!start4`')
    # Round 4
    if message.content.startswith('!start4'):
        file=discord.File("./test.png", filename = "test.png")
        await message.channel.send("Starting round 4", file = file)
        await message.channel.send('Sao khi giải được câu đố của mỗi vòng vui lòng gõ theo cú pháp dể kiểm tra kêt quả`!round4 {đáp án của bạn}`')
    if message.content.startswith('!round4 Vung Tau') or message.content.startswith('!round4 vung tau') or message.content.startswith('!round4 VUNG TAU'):
        await message.channel.send('Wait to check the answer: 5s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 4s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 3s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 2s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 1s!')
        await asyncio.sleep(1)
        await message.channel.send("Xin chúc mừng bạn đã vượt qua vòng 4!")
        await asyncio.sleep(1)
        await message.channel.send("Keyword : 8")
        await asyncio.sleep(1)
        await message.channel.send('Để bắt đầu vòng tiếp theo vui lòng gõ theo cú pháp`!start5`')

    # Round 5
    if message.content.startswith('!start5'):
        file=discord.File("./test.png", filename = "test.png")
        await message.channel.send("Starting round 5", file = file)
        await message.channel.send('Sao khi giải được câu đố của mỗi vòng vui lòng gõ theo cú pháp dể kiểm tra kêt quả`!round5 {đáp án của bạn}`')
    if message.content.startswith('!round5 Discord') or message.content.startswith('!round5 discord') or message.content.startswith('!round5 DISCORD'):
        await message.channel.send('Wait to check the answer: 5s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 4s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 3s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 2s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 1s!')
        await asyncio.sleep(1)
        await message.channel.send("Xin chúc mừng bạn đã vượt qua vòng 5!")
        await asyncio.sleep(1)
        await message.channel.send("Keyword : 7")
        await asyncio.sleep(1)
        await message.channel.send('Để bắt đầu vòng tiếp theo vui lòng gõ theo cú pháp`!start6`')

    # Round 6
    if message.content.startswith('!start6'):
        file=discord.File("./test.png", filename = "test.png")
        await message.channel.send("Starting round 6", file = file)
        await message.channel.send('Sao khi giải được câu đố của mỗi vòng vui lòng gõ theo cú pháp dể kiểm tra kêt quả`!round6 {đáp án của bạn}`')
    if message.content.startswith('!round6 20-11') or message.content.startswith('!round6 20/11'):
        await message.channel.send('Wait to check the answer: 5s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 4s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 3s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 2s!')
        await asyncio.sleep(1)
        await message.channel.send('Wait to check the answer: 1s!')
        await asyncio.sleep(1)
        await message.channel.send("Xin chúc mừng bạn đã vượt qua vòng 6!")
        await asyncio.sleep(1)
        await message.channel.send("Keyword : 5")
        await asyncio.sleep(1)
        await asyncio.sleep(1)
        await message.channel.send("Xin chúc mừng bạn đã vượt qua vòng tổng cộng 6 vòng!")
        await asyncio.sleep(1)
        await message.channel.send("Ứng với mỗi vồng bạn đã nhận được 1 con số. NHIỆM VỤ CUỐI CÙNG: hãy ghép những con số đố lại và tìm ý nghĩa của con số đó")
        await message.channel.send('Ban có thể ghép 6 con số: 50xxxx khi ghép những số lại sẽ thành một dãy số có nghĩa')
        await message.channel.send('Theo trình tự thời gian')
        await message.channel.send("Chuong trinh dich so: ")
    if message.content.startswith('507680'):
        await message.channel.send('Dich: 我一定要追你! <3')
        await message.channel.send('Dich: Anh nhất định sẽ tán đổ em! <3')
    else: 
        await message.channel.send('Sai số rồi nhập lại đi bạn ơi!')


if not client.is_closed():
    client.run(
        'MTA2MjQzMDQ5NDQ0NjMzMzk3Mg.GzURVp.jFw598GbOMyHUh5HWco7Xyar9HmzeyL_KxZ4Is')
else:
    print("Event loop already closed")

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Set up OpenAI
openai.api_key = os.getenv('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')

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    """Responds with a friendly hello message"""
    await ctx.send(f'Hello {ctx.author.name}! 👋')

@bot.command(name='ping')
async def ping(ctx):
    """Check the bot's latency"""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! 🏓 Latency: {latency}ms')

@bot.command(name='ask')
async def ask(ctx, *, question):
    """Ask ChatGPT a question"""
    try:
        # Send a "thinking" message
        async with ctx.typing():
            # Create the chat completion
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ],
                max_tokens=1000
            )
            
            # Get the response text
            answer = response.choices[0].message.content
            
            # Split the response if it's too long (Discord has a 2000 character limit)
            if len(answer) > 1900:
                chunks = [answer[i:i+1900] for i in range(0, len(answer), 1900)]
                for chunk in chunks:
                    await ctx.send(chunk)
            else:
                await ctx.send(answer)
                
    except Exception as e:
        await ctx.send(f"Sorry, I encountered an error: {str(e)}")

# Run the bot
if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN')) 

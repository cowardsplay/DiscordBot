# Discord Bot

A simple Discord bot built with discord.py that responds to basic commands.

## Setup

1. Create a new Discord application and bot at the [Discord Developer Portal](https://discord.com/developers/applications)
2. Get your bot token from the Developer Portal
3. Create a `.env` file in the project root and add your bot token:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Bot

To run the bot, simply execute:
```bash
python bot.py
```

## Available Commands

- `!hello` - Bot responds with a friendly greeting
- `!ping` - Check the bot's latency

## Features

- Basic command handling
- Latency checking
- Environment variable configuration
- Message content intent enabled for command processing

## Adding New Commands

To add new commands, you can create new functions in `bot.py` using the `@bot.command()` decorator. For example:

```python
@bot.command(name='command_name')
async def command_function(ctx):
    await ctx.send('Your response here')
``` 
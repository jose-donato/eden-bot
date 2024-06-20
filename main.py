import nextcord
from nextcord.ext import commands
from helpers.binance import calculate_fibonacci_levels
from helpers.markdown import print_to_table
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

bot = commands.Bot()

@bot.slash_command(description="Returns fibonacci levels for a given symbol and interval")
async def levels(interaction: nextcord.Interaction, symbol: str = nextcord.SlashOption(description="Chose a binance symbol. E.g., BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT"), interval: str = nextcord.SlashOption(choices=[
    "1m", "5m", "15m", "1h", "4h", "12h", "1d", "1w"
], description="Interval for fetching historical data")):
    data = calculate_fibonacci_levels(symbol, interval)
    await interaction.send(print_to_table(data, symbol, interval), ephemeral=True)

bot.run(os.getenv('DISCORD_TOKEN'))
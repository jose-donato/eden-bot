# Discord Fibonacci Bot

This project is a Discord bot built using the `nextcord` library, designed to provide Fibonacci retracement levels for cryptocurrency trading pairs on Binance. It responds to slash commands within Discord.

## Features

- **Slash Commands**: Users can interact with the bot using slash commands.
- **Cryptocurrency Support**: The bot supports multiple cryptocurrency symbols like BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT.
- **Multiple Time Intervals**: Users can request data for various time intervals ranging from 1 minute to 1 week.

## Requirements

- Docker

## Setup

1. Clone the repository: `git clone https://github.com/yourusername/discord-fibonacci-bot.git`
2. Navigate to the project directory: `cd discord-fibonacci-bot`
3. Create a `.env` file and add your Discord token: `DISCORD_TOKEN=your_discord_token`
4. Build docker image: `docker build -t discord-fibonacci-bot .`
5. Run the docker container: `docker run -d --env-file .env --name discord-fibonacci-bot discord-fibonacci-bot`
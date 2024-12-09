import asyncio
from gen import TelegramChannelReader
from eng import TradEngine

class TradingBot:
    def __init__(self, api_id, api_hash, channel_username, ssid):
        self.api_id = api_id
        self.api_hash = api_hash
        self.channel_username = channel_username
        self.ssid = ssid

    async def run(self):
        # Initialize the TelegramChannelReader
        telegram_reader = TelegramChannelReader(self.api_id, self.api_hash, self.channel_username)

        # Initialize the TradEngine
        trad_engine = TradEngine(telegram_reader, self.ssid)

        # Start the trading engine
        await trad_engine.start()

# Main entry point
if __name__ == "__main__":
    # Telegram API credentials and trading session details
    API_ID = '22613667'  # Your API ID
    API_HASH = '6bdf404500def42da3f836d76a36b68d'  # Your API Hash
    CHANNEL_USERNAME = 'ProvenSignals'  # Channel username (without '@')
    SSID = r'42["auth",{"session":"dihpme6fh6s30mhe5nd47snu1l","isDemo":1,"uid":79658638,"platform":2}]'

    # Create the TradingBot instance
    bot = TradingBot(API_ID, API_HASH, CHANNEL_USERNAME, SSID)

    # Run the bot
    asyncio.run(bot.run())

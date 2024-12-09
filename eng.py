from BinaryOptionsTools import pocketoption
class TradEngine:
    def __init__(self, telegram_reader, ssid, demo=True):
        self.telegram_reader = telegram_reader  # TelegramChannelReader instance
        self.api = pocketoption(ssid, demo)

    async def process_signal(self, signal):
        # Process the incoming signal and execute trades
        print(f"Processing signal: {signal}")
        
        if signal == "EUR/USD OTC 3-min HIGHER":
            print("Entering long position...")
            self.api.Call(10, "EURUSD_otc", 90, False)
        elif signal == "EUR/USD OTC 3-min LOWER":
            print("Entering short position...")
            self.api.Put(10, "EURUSD_otc", 90, False)

    async def start(self):
        # Start the Telegram reader and pass the signal processing method as a callback
        await self.telegram_reader.start(signal_callback=self.process_signal)
from telethon import TelegramClient, events

class TelegramChannelReader:
    def __init__(self, api_id, api_hash, channel_username, session_name='session_name'):
        self.api_id = api_id
        self.api_hash = api_hash
        self.channel_username = channel_username
        self.session_name = session_name
        self.client = TelegramClient(self.session_name, self.api_id, self.api_hash)
        self.signal_callback = None  # A callback function to process signals

    """
    async def get_last_2_messages(self):
        # Get the channel entity
        channel = await self.client.get_entity(self.channel_username)
        # Fetch the last 2 messages from the channel
        messages = await self.client.get_messages(channel, limit=2)
        for msg in messages:
            print(f"Last message in {self.channel_username}: {msg.text}")
    """        
    async def new_message_listener(self, event):
        # Extract and print the incoming message text
        message_text = event.message.text
        print(f"New message in {self.channel_username}: {message_text}")
        
        # Pass the message to the callback, if set
        if self.signal_callback:
            await self.signal_callback(message_text)

    async def start(self, signal_callback=None):
        # Set the callback function for signal processing
        self.signal_callback = signal_callback
        
        # Ensure the client is connected before fetching the messages
        await self.client.start()  # This ensures the client connects to Telegram
        print("Client started and connected.")
        
        # Fetch and print the last 2 messages when the script starts
        #await self.get_last_2_messages()

        # Start listening for new messages
        print("Listening for new messages...")
        self.client.add_event_handler(self.new_message_listener, events.NewMessage(chats=self.channel_username))

        # Run until manually disconnected
        await self.client.run_until_disconnected()


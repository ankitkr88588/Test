from telethon.sync import TelegramClient, events
import asyncio
import datetime
import random

# Your API credentials and bot token
api_id = 22877673
api_hash = 'fd368cc0762560833a22445063ce2c96'
bot_token = '6438317885:AAH06wuWeEZm62uFs62EudqW1sDMIwX9yM8'
group_id = -1001969570874  # Your group's ID

# Initialize the Telegram client
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# List of exit messages and emojis
exit_messages = [
    "Mission Accomplished 🚀",
    "Time's Up ⏰",
    # ... (add the rest of your exit messages)
]

emojis = ["🚀", "⏰", "⏳", "⌛", "🎉", "🥳", "✨", "👏", "👑", "🎯", "🎊"]

# Countdown function
async def countdown(event, target_datetime):
    user = await event.get_sender()  # Get the user who sent the command
    user_info = (
        f"👤 **User Name:** {user.first_name}\n"
        f"👤 **Username:** @{user.username}\n"
        f"🆔 **User ID:** {user.id}\n"
    )
    print(user_info)

    chat = await event.get_chat()
    message = await event.respond("🚀 Starting countdown...")

    while datetime.datetime.now() < target_datetime:
        now = datetime.datetime.now()
        time_difference = target_datetime - now

        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        countdown_format = (
            f"{' '.join(random.choices(emojis))} **TIME LEFT:** {hours:02d}:{minutes:02d}:{seconds:02d} {' '.join(random.choices(emojis))}\n\n\n\n"
            f"{' '.join(random.choices(emojis))} **HOURS LEFT:** {hours + (minutes / 60):.2f} HOURS {' '.join(random.choices(emojis))}\n\n\n\n"
            f"{' '.join(random.choices(emojis))} **MINUTES LEFT:** {minutes + (seconds / 60):.2f} MINUTES {' '.join(random.choices(emojis))}\n\n\n\n"
            f"{' '.join(random.choices(emojis))} **SECONDS LEFT:** {seconds} SECONDS {' '.join(random.choices(emojis))}\n\n\n\n\n"
            f"{random.choice(exit_messages)}"
        )

        await client.edit_message(chat, message, countdown_format)
        await asyncio.sleep(1)

    await client.edit_message(chat, message, "🎉 **Countdown Finished!**")

# Sending birthday wishes
birthday_wishes = [
    "🎂🎉 Happy Birthday, Aarohi! 🎉🎂 Wishing you a day filled with love and happiness! 🥳🎈",
    # ... (add the rest of your birthday wishes)
]

async def send_birthday_wishes():
    chat_entity = group_id
    
    for wish in birthday_wishes:
        await client.send_message(chat_entity, wish)
        await asyncio.sleep(2)  # To avoid hitting rate limits

# Sending enjoying emojis
async def send_enjoying_emojis():
    chat_entity = group_id
    
    for _ in range(100):
        await client.send_message(chat_entity, random.choice(emojis))
        await asyncio.sleep(1)  # To avoid hitting rate limits

# Event handler for the /start command
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    target_datetime = datetime.datetime(2024, 8, 10, 0, 0)  # August 10, 2023, 12:00 AM
    await countdown(event, target_datetime)
    await send_birthday_wishes()
    await send_enjoying_emojis()

# Start the client
print("Bot is running...")
client.run_until_disconnected()

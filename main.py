from telethon.sync import TelegramClient, events
import asyncio
import datetime
import random

# Your API credentials and bot token
api_id = 22877673
api_hash = 'fd368cc0762560833a22445063ce2c96'
bot_token = '6438317885:AAH06wuWeEZm62uFs62EudqW1sDMIwX9yM8'

# Initialize the Telegram client
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# List of exit messages and emojis
exit_messages = [
    "Mission Accomplished 🚀",
    "Time's Up ⏰",
    "It's a Wrap 🎉",
    "Countdown Concluded ✨",
    "Let the Celebrations Begin 🎊",
    "Hooray! 🎈",
    "Goal Achieved 🥳",
    "Party Time! 🥳",
    "Epic Countdown 🌟",
    "Success! 🌟",
    "We Made It! 🎉",
    "Great Job! 👍",
    "Cheers! 🥂",
    "Well Done! 👏",
    "Bravo! 👌",
    "Victory Lap! 🏆",
    "Goal Reached! 🎯",
    "Triumphant Finish! 🎉",
    "Time to Celebrate 🎊",
    "Unstoppable 🚀",
    "Fantastic Countdown! 🌟",
    "Legendary Finish! 🏆",
    "Onward to Victory! ⚔️",
    "Cheers to Success! 🥂",
    "Kudos to You! 🌟",
    "Superb Effort! 💪",
    "Magnificent! 💫",
    "Completion Achieved! 🎉",
    "Tremendous Countdown! 🚀",
    "Excellence Personified! 🌟",
    "Achievement Unlocked! 🏆",
    "Impressive Finish! 👏",
    "Brilliant Success! 🌟",
    "Crowning Glory! 👑",
    "Wondrous Achievement! 🌟",
    "Masterful Countdown! 🎉",
    "Glorious Victory! 🏆",
    "The Countdown Closes 🚀",
    "Exult in Success! 🌟",
    "Astounding Finish! 🎉",
    "Incredible Triumph! 🏆",
    "Celebrate the Win! 🥳",
    "Conquering Countdown! ⚔️",
    "Triumph Personified! 🏆",
    "Joyful Success! 🌟",
    "Phenomenal Countdown! 🚀",
    "Final Countdown Flourish! 🎉",
    "Marvelous Victory! 🏆",
    "Achievement Attained! 🌟",
    "Unbeatable Finish! 💥",
    "Culmination of Success! 🌟",
    "Epic Countdown Conclusion! 🚀",
    "Triumphant Glory! 🏆",
    "Cheers to the Win! 🥂",
    "Exemplary Finish! 👌",
    "Splendid Success! 🌟",
    "Finale of Triumph! 🎉",
    "Super Countdown! 🚀",
    "Victorious Conquest! 🏆",
    "The Finish Line Approaches! 🏁",
    "Jubilant Success! 🌟",
    "Stupendous Countdown! 🚀",
    "Ultimate Victory! 🏆",
    "Countdown Triumph! 🎉",
    "Success Beyond Compare! 🌟",
    "Wondrous Finish! ✨",
    "Countdown Glory! 🚀",
    "Glorious Triumph! 🏆",
    "Mission Success! ✅",
    "Triumphant Countdown! 🎉",
    "Magnificent Victory! 🏆",
    "Achievement Beyond Belief! 🌟",
    "Fantastic Finish! 🎉",
    "Countdown Champion! 🚀",
    "Joyous Triumph! 🏆",
    "Exquisite Success! 🌟",
    "Victory Cheers! 🥂",
    "Stellar Countdown! 🚀",
    "Countdown of Champions! 🏆",
    "Celebrating Success! 🌟",
    "Success on the Horizon! 🌅",
    "Countdown Victory! 🎉",
    "Triumphant Cheers! 🥂",
    "Countdown Excellence! 🚀",
    "Champion of Success! 🏆",
    "Success Awaits! 🌟",
    "Triumphant Fanfare! 🎉",
    "Countdown Glory Unleashed! 🚀",
    "Triumphantly Yours! 🏆",
    "Embrace the Success! 🌟",
    "Countdown Achieved! 🎉",
    "Triumph Celebrated! 🥳",
    "Success Beyond Measure! 🌟",
    "Triumphantly Concluded! 🏆",
    "Countdown Conqueror! 🚀",
    "Victorious Cheers! 🥂",
    "Success Sparkles! ✨",
    "Countdown Grandeur! 🚀",
    "Triumphant Parade! 🎉",
    "Glorious Success! 🌟",
    "Countdown Champion's Euphoria! 🏆",
    "Triumphant Fireworks! 🎆",
    "Triumphant Anthem! 🎶",
]

emojis = ["🚀", "⏰", "⏳", "⌛", "🎉", "🥳", "✨", "👏", "👑", "🎯", "🎊"]

# Countdown function
# ... (previous code)

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

    now = datetime.datetime.now()
    time_difference = target_datetime - now

    for remaining in range(time_difference.seconds, -1, -1):
        hours, remainder = divmod(remaining, 3600)
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

# ... (rest of the code)


# Sending birthday wishes
birthday_wishes = [
    "🎂🎉 Happy Birthday, Aarohi! 🎉🎂 Wishing you a day filled with love and happiness! 🥳🎈",
    "Warmest wishes on your special day, Aarohi! May your birthday be as wonderful as you are! 🎂🎈",
    "Sending you a big birthday hug, Aarohi! May your day be filled with laughter and joy! 🥳🎉",
    "Happy Birthday, Aarohi! May this year be filled with exciting adventures and beautiful moments! 🎂🎁",
    "Wishing you an amazing birthday, Aarohi! May all your dreams and wishes come true! 🥳🎂",
    "On your birthday, Aarohi, I hope you're surrounded by love, laughter, and all the things that make you happy! 🎈🎉",
    "Sending you lots of birthday love and good vibes, Aarohi! May your day be truly spectacular! 🥳🎂",
    "Happy Birthday, Aarohi! May your day be as bright and beautiful as your smile! 🎉🎂",
    "Another year older, wiser, and even more fabulous! Happy Birthday, Aarohi! 🥳🎈",
    "Wishing you a year ahead filled with love, laughter, and endless blessings, Aarohi! Happy Birthday! 🎂🎉",
    "May your birthday be filled with love, joy, and the company of those who cherish you, Aarohi! 🥳🎂",
    "Happy Birthday to an incredible person, Aarohi! May your day be as special as you are to everyone around you! 🎉🎂",
    "Here's to another year of laughter, adventure, and wonderful memories, Aarohi! Happy Birthday! 🥳🎈",
    "Wishing you a day that's just as sweet and wonderful as you are, Aarohi! Happy Birthday! 🎂🎉",
    "May your birthday be the start of an amazing year ahead, filled with happiness and success, Aarohi! 🥳🎂",
    "Sending you all the joy and happiness in the world on your special day, Aarohi! Happy Birthday! 🎈🎉",
    "Happy Birthday, Aarohi! May your day be filled with laughter, love, and lots of cake! 🎂🥳",
    "Here's to a year ahead full of exciting opportunities and beautiful moments, Aarohi! Happy Birthday! 🎉🎂",
    "Wishing you a birthday that's as wonderful and unique as you are, Aarohi! Enjoy your special day! 🥳🎈",
    "May your birthday be a reflection of all the happiness and positivity you bring to others, Aarohi! 🎂🎉",
    "On your special day, Aarohi, may you be surrounded by happiness, love, and all the things you hold dear! 🥳🎂"
]
async def send_birthday_wishes():
    chat_entity = await client.get_entity(-1001969570874)  # Replace with the group's username or ID
    
    for wish in birthday_wishes:
        await client.send_message(chat_entity,f"@Notfound989 {wish}")
        await asyncio.sleep(0.8)  # To avoid hitting rate limits

#imoji
async def send_enjoying_emojis():
    chat_entity = await client.get_entity(-1001969570874)  # Replace with the group's username or ID
    
    for k in range(100):
        await client.send_message(chat_entity, random.choice(emojis))
        await asyncio.sleep(1)  # To avoid hitting rate limits


# Event handler for the /start command
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    target_datetime = datetime.datetime(2023, 8 ,9,0, 2)  # 12 am on August 10th
    await countdown(event, target_datetime)
    await send_birthday_wishes()

# Start the client
print("Bot is running...")
client.run_until_disconnected()

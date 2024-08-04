from os import environ 

class Config:
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6970918221').split()]
    BOT_TOKEN = environ.get("BOT_TOKEN", "7360899365:AAG5PF3VpqCY5cOq6USO79AIUYgJYdD_VBA")
    # Insert your Telegram bot token here
    bot = telebot.TeleBot('7040771689:AAGqgdv8i66m-UJwCuNoKE1CLbkTdo9KBEg')

    # Admin user IDs
    admin_id = {"7462351545"}

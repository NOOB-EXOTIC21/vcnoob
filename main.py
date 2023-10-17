import os
import telebot
import requests

bot = telebot.TeleBot("6161615496:AAFtkF661taD-vRE3nAQ3UF5ggWMD68o2tg")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['vc'])
def tell_vehicle_info(message):
    try:
        # Extract the vehicleId from the command
        vehicle_id = message.text.split(' ')[1]

        # Make the API request
        response = requests.get(f"https://lol.game-quasar.com//?vehicleId={vehicle_id}")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            bot.reply_to(message, f"Response: {response.text}")
        else:
            bot.reply_to(message, f"Error: Unable to fetch information for vehicle {vehicle_id}")
    except IndexError:
        bot.reply_to(message, "Error: Please provide a vehicleId after /vc")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

bot.infinity_polling()

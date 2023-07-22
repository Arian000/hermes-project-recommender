# Import necessary libraries
import pandas as pd
import asyncio
from aiogram import Bot, Dispatcher, types
import openai

# Define Telegram bot token and OpenAI API key
telegram_token = '<TELEGRAM-BOT-TOKEN>'
openai.api_key = '<OPENAI-API-KEY>'

# Initialize a Bot and a Dispatcher for handling incoming messages
bot = Bot(token=telegram_token)
dp = Dispatcher(bot)

# Function to recommend projects based on user's resume
def recommend(projects, resume_text):
    # Prepare system message for GPT-3 with project descriptions
    system_text = f"You are a project recommender. User will give you a resume and you should sort the projects based on compatibility with the resume. These are description of projects: {str(projects)}"
    messages = [
        {"role": "system", "content": system_text},
        {"role": "user", "content": resume_text},
    ]
    
    # Send request to GPT-3 API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Return the response received from GPT-3
    return str(response["choices"][0]["message"]["content"])

# Asynchronous message handler
@dp.message_handler()
async def handle_message(message: types.Message):
    # Ignore messages that do not start with '/'
    if message.text[0] != '/':
        return
    # Prepare filename of CSV file containing project descriptions
    filename = f"csvs/{message.text[1:]}.csv"
    projects = pd.read_csv(filename)['Description']
    try:
        # Read user's resume text from file
        with open(f'resumes/{message.from_user.id}.txt', 'r') as file:
            resume_text = file.read().replace('\n', '')
        # Get recommended projects
        projects_sorted = recommend(projects, resume_text)
        print(projects_sorted)
        # Respond with the recommended projects
        await message.answer(projects_sorted)
    # Catch exceptions and respond with the error message
    except Exception as e:
        await message.answer(f"Error: {str(e)}")

# Function to send message when bot starts
async def on_startup(dp):
    await bot.send_message(119298397, 'Your bot started')

# Function to send message when bot stops
async def on_shutdown(dp):
    await bot.send_message(119298397, 'Your bot stopped')

# Main function
if __name__ == '__main__':
    from aiogram import executor

    # Start the bot and set up the startup and shutdown functions
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)

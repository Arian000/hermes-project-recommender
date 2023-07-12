import pandas as pd
import asyncio
from aiogram import Bot, Dispatcher, types
import openai

telegram_token = '6018456454:AAG0dvTHEWHudF2loaY2QKutRMlCnEbHKCk'
openai.api_key = ''
# Initialize bot and dispatcher
bot = Bot(token=telegram_token)
dp = Dispatcher(bot)

def recommend(projects, resume_text):
    system_text = f"You are a project recommender. User will give you a resume and you should sort the projects based on compatibality with the resume. These are description of projects: {str(projects)}"
    messages = [
            {"role": "system", "content": system_text},
            {"role": "user", "content": resume_text},
        ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return str(response["choices"][0]["message"]["content"])

@dp.message_handler()
async def handle_message(message: types.Message):
    if message.text[0] != '/':
        return
    filename = f"csvs/{message.text[1:]}.csv"
    projects = pd.read_csv(filename)['Description']
    try:
        with open(f'resumes/{message.from_user.id}.txt', 'r') as file:
            resume_text = file.read().replace('\n', '')
        projects_sorted = recommend(projects, resume_text)
        print(projects_sorted)
        # for project in projects:
        await message.answer(projects_sorted)
    except Exception as e:
        await message.answer(f"Error: {str(e)}")

async def on_startup(dp):
    await bot.send_message(119298397, 'Your bot started')

async def on_shutdown(dp):
    await bot.send_message(119298397, 'Your bot stopped')

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
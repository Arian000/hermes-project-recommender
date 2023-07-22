Hermes Project Recommender

Hermes Project Recommender is a Telegram bot that leverages OpenAI's powerful GPT-3 model to recommend projects to users based on their resume.

The user submits a command to the bot in the format '/filename' where 'filename' is the name of the CSV file containing project descriptions. The bot reads the project descriptions and the user's resume text, and then uses GPT-3 to recommend projects that best align with the user's resume.

Getting Started

Prerequisites

Python 3.7+

pandas

aiogram

openai

asyncio

Install the prerequisites with pip:

pip install pandas aiogram openai asyncio

Setting Up

Clone the repository to your local machine:

git clone https://github.com/Arian000/hermes-project-recommender.git

Navigate to the project directory:

cd hermes-project-recommender

Set up your Telegram bot and get your bot token.

Get your OpenAI API key.

Replace the placeholders <TELEGRAM-BOT-TOKEN> and <OPENAI-API-KEY> in the main.py file with your respective Telegram bot token and OpenAI API key.

Running the Bot

To start the bot, run the following command:

python main.py

Usage

Message the bot with a command in the format /filename where 'filename' is the name of the CSV file (without the .csv extension) containing project descriptions.

The bot will read the project descriptions and the user's resume text (which should be in a text file named with the user's ID under the 'resumes' directory), and respond with the projects that best align with the user's resume.

License

This project is licensed under the terms of the MIT license.

Contact

For any questions or concerns, please open an issue on this GitHub repository.

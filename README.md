Project Description
Telegram bot for ordering pizza built with Django and PostgreSQL. The project includes a pizza catalog, cart system, order management, Telegram bot interface, REST API and unit tests.

Tech Stack
• Python
• Django
• Django REST Framework
• PostgreSQL
• Telebot (pyTelegramBotAPI)

Requirements
• Python 3.10+
• PostgreSQL
• Git


Installation Steps
1. Clone the repository:
git clone https://github.com/vts-software/pizza-telegram-bot
cd pizza-telegram-bot

2. Create virtual environment:
python -m venv venv

3. Activate environment:
Windows:
venv\Scripts\activate

Linux / Mac:
source venv/bin/activate

4. Install dependencies:
pip install -r requirements.txt

5. Create PostgreSQL database:
CREATE DATABASE pizza_db;

6. Configure environment variables (.env file):
SECRET_KEY=django_secret_key
DEBUG=True
POSTGRES_DB=pizza_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
TELEGRAM_TOKEN=your_telegram_bot_token

7. Apply migrations:
python manage.py migrate

8. Create admin user:
python manage.py createsuperuser
Running the Project
Start Django server:
python manage.py runserver

Admin panel will be available at:
http://127.0.0.1:8000/admin/

Run Telegram bot:
python bot_runner.py

Running Tests
python manage.py test

Project Structure
pizza-telegram-bot
│
├── bot_runner.py
├── bot_app.py
│
├── tg_bot
│   ├── telegram_bot.py
│   ├── handlers.py
│   └── keyboards.py
│
├── users
├── menu
├── cart
├── orders
│
├── config
└── manage.py

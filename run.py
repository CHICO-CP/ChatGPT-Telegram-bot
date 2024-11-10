from bot.bot import main
from bot.database import create_table
from bot.config import TELEGRAM_TOKEN

create_table()

main()

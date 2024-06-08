import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext

# Вставьте ваш токен сюда
TOKEN = 'TOKEN'

# Идентификаторы групп
GROUP_IDS = [00000000000]

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Обработчик входящих сообщений
async def handle_message(update: Update, context: CallbackContext):
    message = update.message
    text = message.text

    # Пересылка сообщения в группы
    for group_id in GROUP_IDS:
        await context.bot.send_message(chat_id=group_id, message_thread_id = "0000" , text=text)

def main() -> None:
    # Настройка приложения
    application = Application.builder().token(TOKEN).build()

    # Добавление обработчика сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
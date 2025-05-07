from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from ConversationalShell import ConversationalShell

class TelegramBridge:
    def __init__(self):
        self.shell = ConversationalShell()
        self.allowed_user = "jsunheart"
        self.bot = Bot(token="8170948174:AAFM_RZNl4AcpyY0M3rQwsHDmjCY5_yfwyE")
        self.updater = Updater(bot=self.bot, use_context=True)
        dp = self.updater.dispatcher
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, self.handle_message))

    def handle_message(self, update: Update, context: CallbackContext):
        if str(update.message.chat.username) != self.allowed_user:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Access denied.")
            return
        user_input = update.message.text
        response = self.shell.receive_message(user_input)
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    def start(self):
        print("TelegramBridge is live.")
        self.updater.start_polling()
        self.updater.idle()
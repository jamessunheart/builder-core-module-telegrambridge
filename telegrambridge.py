from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
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
        try:
            username = str(update.message.chat.username)
            user_input = update.message.text
            print(f"[TRACE] From: {username} | Msg: {user_input}")
            if username != self.allowed_user:
                context.bot.send_message(chat_id=update.effective_chat.id, text="Access denied.")
                return
            # TEMPORARY RESPONSE OVERRIDE
            response = "Hello from Builder Core. This confirms connection."
            context.bot.send_message(chat_id=update.effective_chat.id, text=response)
        except Exception as e:
            print(f"[ERROR] Exception in TelegramBridge: {str(e)}")

    def start(self):
        print("[TRACE] TelegramBridge is now polling...")
        self.updater.start_polling()
        self.updater.idle()
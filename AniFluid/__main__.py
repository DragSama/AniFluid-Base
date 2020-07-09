import glob
import importlib
from AniFluid import dispatcher, updater

files = glob.glob('AniFluid/modules/*.py')

for file in file:
  importlib.import_module("AniFluid.modules." + file)

@run_async
def start(update: Update, context: CallbackContext):
    update.effective_message.reply_text("Hm?")


def main():
    start_handler = CommandHandler("start", start)
    dispatcher.add_hander(start_handler)

if __name__ == '__main__':
    LOGGER.info("Successfully loaded modules: " + str(files
    main()
    updater.start_polling()

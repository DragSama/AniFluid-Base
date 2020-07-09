import logging
import telegram.ext as tg

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

from AniFluid.config import TOKEN
updater = tg.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

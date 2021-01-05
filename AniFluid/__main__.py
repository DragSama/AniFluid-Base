# Copyright (C) 2020-2021 DragSama. All rights reserved. Source code available under the AGPL.
#
# This file is part of AniFluidBot.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import glob
import importlib
from AniFluid import dispatcher, updater, LOGGER

files = glob.glob('AniFluid/modules/*.py')

for file in file:
  importlib.import_module("AniFluid.modules." + file)

@run_async
def start(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text("Hm?")


def main():
    start_handler = CommandHandler("start", start)
    dispatcher.add_hander(start_handler)

if __name__ == '__main__':
    LOGGER.info("Successfully loaded modules: " + str(files
    main()
    updater.start_polling()

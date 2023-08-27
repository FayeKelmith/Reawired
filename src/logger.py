# NOTE: to log progress

import logging
import os
from datetime import datetime

# to get log information
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%M_%S')}.log"
# creating a logs path at the current working directory, start with logs then log information.
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# making a directory, the creating the file despite others existing there already

os.makedirs(logs_path, exist_ok=True)
# getting our newly created file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
# overring the logging file to suit our needs

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

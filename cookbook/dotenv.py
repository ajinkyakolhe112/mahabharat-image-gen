# INSTALL      : pip install python-dotenv
# WRONG INSTALL:  pip install dotenv
import dotenv, os
dotenv.load_dotenv ( dotenv.find_dotenv() )
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
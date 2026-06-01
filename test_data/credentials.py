import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME", "")
PASSWORD = os.getenv("PASSWORD", "")
BASE_URL = os.getenv("BASE_URL", "")
INVENTORY_URL = os.getenv("INVENTORY_URL", "")
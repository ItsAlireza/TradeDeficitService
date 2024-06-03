from dotenv import load_dotenv
import os


dotenv_path = '.env'
if not os.path.exists(dotenv_path):
    raise FileNotFoundError(f"The .env file does not exist at the specified path: {dotenv_path}\nfull path is: {os.path.abspath(dotenv_path)}")

load_dotenv(dotenv_path)

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from frontend.pages.home import HomePage

if __name__ == "__main__":
    page = HomePage()
    page.render()
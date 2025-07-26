import os
from pathlib import Path

from dotenv import load_dotenv

from src import SendRequest, TakeImage, logger


def main() -> None:
    """Load configuration and start the image capture process."""
    env_path = Path(__file__).parent / ".env"
    load_dotenv(dotenv_path=env_path)

    url = os.getenv("API_URL")
    api_key = os.getenv("API_KEY")
    interval = int(os.getenv("INTERVAL", 60))

    if not url:
        logger.error("API_URL is not set in the environment variables.")
        raise ValueError("API_URL is not set in the environment variables.")

    sender = SendRequest(url, api_key)
    take_image = TakeImage(sender, interval)
    take_image.run()


if __name__ == "__main__":
    main()

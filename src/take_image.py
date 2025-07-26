import io
import random
import time
from typing import Dict

import cv2
from picamera2 import Picamera2

from .logger import logger
from .send_request import SendRequest


class TakeImage:
    """Capture images periodically from a Pi Camera and send to a server."""

    def __init__(self, request_sender: SendRequest, interval: int = 60) -> None:
        """
        Initialize with a SendRequest instance and capture interval.

        Args:
            request_sender (SendRequest): Instance to handle HTTP requests.
            interval (int): Time between captures in seconds.
        """
        self.sender = request_sender
        self.interval = interval

        self.picam2 = Picamera2()
        config = self.picam2.create_still_configuration(
            main={"format": "RGB888", "size": (640, 480)}
        )
        self.picam2.configure(config)
        self.picam2.start()
        time.sleep(1)  # Optional: let camera settle

    def _generate_payload(self) -> Dict[str, str]:
        """Generate random payload data for each image."""
        return {
            "user_id": "1",
            "loc_id": "1",
            "is_trash": str(random.choice([0, 1])),
            "water_lvl": f"{random.uniform(1, 20):.2f}",
        }

    def take_and_send(self) -> None:
        """Capture an image, encode it, send with metadata, and log results."""
        frame = self.picam2.capture_array()

        success, encoded_image = cv2.imencode(".jpg", frame)
        if not success:
            logger.error("Failed to encode image.")
            return

        image_bytes = io.BytesIO(encoded_image.tobytes())
        payload = self._generate_payload()

        response = self.sender.send_image_post_request(
            image_bytes=image_bytes, data=payload
        )
        if response is None:
            logger.error("Request failed.")
        else:
            logger.info("Success request")

    def run(self) -> None:
        """Start the capture-send loop, until interrupted."""
        logger.info(
            f"Starting image capture every {self.interval} seconds. Press Ctrl+C to stop."
        )
        try:
            while True:
                self.take_and_send()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logger.info("Stopping image capture.")
        finally:
            self.picam2.stop()
            logger.info("Camera stopped.")

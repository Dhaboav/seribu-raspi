import io
from typing import Any, Dict, Optional, Union

import requests

from .logger import logger


class SendRequest:
    """Handles HTTP requests including sending images with authentication."""

    def __init__(self, url: str, api_key: Optional[str] = None) -> None:
        """
        Initialize with endpoint URL and optional Bearer API key.

        Args:
            url (str): The API endpoint URL.
            api_key (Optional[str]): Bearer token for authorization.
        """
        self.url = url
        self.api_key = api_key

    def send_get_request(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Send a GET request to the URL with optional query parameters.

        Args:
            params (Optional[Dict[str, Any]]): Query parameters.

        Returns:
            Optional[Dict[str, Any]]: Parsed JSON response or None on failure.
        """
        try:
            response = requests.get(self.url, params=params)
            response.raise_for_status()
            logger.info("Success request")
            return response.json()
        except requests.RequestException as e:
            status = e.response.status_code if e.response else "No Status"
            logger.error(f"Error {status}: {e.__class__.__name__}")
            return None

    def send_image_post_request(
        self,
        image_bytes: io.BytesIO,
        data: Optional[Dict[str, Any]] = None,
        field_name: str = "file",
        filename: str = "image.jpg",
    ) -> Union[Dict[str, Any], str, None]:
        """
        Send a POST request uploading an image with optional form data.

        Args:
            image_bytes (io.BytesIO): Image data in memory.
            data (Optional[Dict[str, Any]]): Additional form data.
            field_name (str): Form field name for the file.
            filename (str): Filename to send.

        Returns:
            Union[Dict[str, Any], str, None]: JSON response dict, raw text, or None on error.
        """
        headers = {"Accept": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        files = {field_name: (filename, image_bytes, "image/jpeg")}

        try:
            response = requests.post(
                self.url, headers=headers, files=files, data=data or {}
            )
            response.raise_for_status()
            try:
                return response.json()
            except ValueError:
                return response.text
        except requests.RequestException as e:
            status = e.response.status_code if e.response else "No Status"
            logger.error(f"Error {status}: {e.__class__.__name__}")
            return None

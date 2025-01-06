import requests
from typing import Optional
import dotenv
import os

# Load environment variables from a .env file
dotenv.load_dotenv()

class AI_MODEL:
    """
    A class to interact with an AI model via a REST API.
    """

    def ask_ai(self, prompt: str) -> str:
        """
        Sends a prompt to the AI model and retrieves the response.

        Args:
            prompt (str): The input message or question to be sent to the AI.

        Returns:
            str: The AI model's response.
        """
        return self.run_flow(
            message=prompt,
            application_token=os.getenv("APPLICATION_TOKEN")
        )

    def run_flow(
        self,
        message: str,
        output_type: str = "chat",
        input_type: str = "chat",
        tweaks: Optional[dict] = None,
        application_token: Optional[str] = None
    ) -> dict:
        """
        Executes a flow by sending a request to the AI model API.

        Args:
            message (str): The input message or question to be sent to the API.
            output_type (str): The expected format of the API's response (default is "chat").
            input_type (str): The format of the input sent to the API (default is "chat").
            tweaks (Optional[dict]): Optional dictionary of tweaks to customize the flow.
            application_token (Optional[str]): The token for API authentication.

        Returns:
            dict: The parsed response from the API.
        """
        # Construct the API URL using environment variables
        api_url = f"{os.getenv('BASE_API_URL')}/lf/{os.getenv('LANGFLOW_ID')}/api/v1/run/{os.getenv('ENDPOINT')}"

        # Prepare the payload for the POST request
        payload = {
            "input_value": message,
            "output_type": output_type,
            "input_type": input_type,
        }

        # Include tweaks in the payload if provided
        if tweaks:
            payload["tweaks"] = tweaks

        # Prepare the headers for the POST request
        headers = None
        if application_token:
            headers = {
                "Authorization": "Bearer " + application_token,
                "Content-Type": "application/json"
            }

        # Send the POST request to the API
        response = requests.post(api_url, json=payload, headers=headers)

        # Parse and return the relevant part of the response
        return response.json()["outputs"][0]["outputs"][0]["results"]["message"]["text"]

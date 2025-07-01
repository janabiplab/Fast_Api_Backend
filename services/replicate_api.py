import replicate
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")


def ask_replicate(prompt: str) -> str:
    try:

        # Defensively ensures the prompt is valid and avoids weird edge cases like None or numbers.

        if not prompt or not isinstance(prompt, str):
            raise ValueError("Prompt must be a non-empty string")
        
        # Sends the input prompt to the LLaMA 4 Maverick model.
        # get the response in chunks (events)
        output = replicate.stream(
            "meta/llama-4-maverick-instruct",
            input={
                "prompt": prompt,
                "max_tokens": 1024,
                "temperature": 0.6,
                "top_p": 1,
                "presence_penalty": 0,
                "frequency_penalty": 0
            }
        )

        full_response = ""
        
        # Collects all streamed fragments into one final string.

        for event in output:
            full_response += str(event)
        
        # Removes leading/trailing whitespace and returns the result.

        return full_response.strip()

    except Exception as e:
        raise Exception(f"Error processing prompt: {str(e)}")

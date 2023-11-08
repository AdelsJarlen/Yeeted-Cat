import requests
import io
from PIL import Image
import data.credentials

def sendPromptToClipdrop(prompt):
    r = requests.post(
        url = 'https://clipdrop-api.co/text-to-image/v1',
        files = {'prompt': (None, "Product design, "+ prompt, 'text/plain')},
        headers = { 'x-api-key': credentials.clipdrop_api_key}
    )

    if (r.ok):
    # r.content contains the bytes of the returned image
        image = Image.open(io.BytesIO(r.content))
        return [image]
    else:
        r.raise_for_status()
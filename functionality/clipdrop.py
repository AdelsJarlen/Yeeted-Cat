import requests
import io
from PIL import Image

def sendPromptToClipdrop(prompt):
    r = requests.post(
        url = 'https://clipdrop-api.co/text-to-image/v1',
        files = {'prompt': (None, "Product design, "+ prompt, 'text/plain')},
        headers = { 'x-api-key': "ac6d220774f556b180714170c5926a4e6b08589eb1cb27aa52d9afea740c4619c8207fb209a5cd4c8e87cb65c06d7709"}
    )

    if (r.ok):
    # r.content contains the bytes of the returned image
        image = Image.open(io.BytesIO(r.content))
        return [image]
    else:
        r.raise_for_status()
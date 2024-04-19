from fastapi import FastAPI, Response, Request
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get(
    "/ip.png",
    responses={
        200: {
            "content": {"image/png": {}},
            "description": "Returns an image with the client's IP address."
        }
    },
    response_class=Response
)
def get_image(request: Request):
    # Create an image with white background
    img = Image.new('RGB', (200, 100), color=(255, 255, 255))
    # Initialize the drawing context with the image as background
    d = ImageDraw.Draw(img)
    # Select a default font
    font = ImageFont.load_default()
    # Position of the text (x, y)
    position = (10, 10)
    # Get client IP to draw
    client_ip = request.client.host
    # Draw the text
    d.text(position, client_ip, fill=(0, 0, 0), font=font)

    # Save the image to a bytes buffer
    image_bytes = BytesIO()
    img.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()

    # Return the image as a response
    return Response(content=image_bytes, media_type="image/png")

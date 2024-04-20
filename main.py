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



@app.get("/big.png", responses={200: {"content": {"image/png": {}}}}, response_class=Response)
def get_image(request: Request):
    # Create an image with white background
    img = Image.new('RGB', (19200, 10800), color=(255, 255, 255))
    
    # Initialize the drawing context with the image as background
    d = ImageDraw.Draw(img)
    
    # Load a custom font (you can specify the path to a TTF or OTF font file)
    font_path = "Allura-Regular.ttf"  # Replace with the path to your font file
    font_size = 3000  # You can change the size here
    font = ImageFont.truetype(font_path, font_size)
    
    # Position of the text (x, y)
    position = (0, 0)
    
    # Get client IP to draw
    client_ip = "cool opinion Bro, \n counterpoint: \n" + str(request.client.host)
    
    # Draw the text
    d.text(position, client_ip, fill=(0, 0, 0), font=font)

    # Save the image to a bytes buffer
    image_bytes = BytesIO()
    img.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()

    # Return the image as a response
    return Response(content=image_bytes, media_type="image/png")



@app.get("/starwars.mp4", responses={200: {"content": {"video/mp4": {}}}}, response_class=Response)
def get_image(request: Request):
  client_ip = str(request.client.host)
  
  return Response(content=image_bytes, media_type="image/png")


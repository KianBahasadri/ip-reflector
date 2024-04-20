from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, AudioFileClip
from io import BytesIO


def make_credits_video(text, duration=15, text_color='yellow', font_size=24, fps=24):
    # Create a text clip
    text_clip = TextClip(text, fontsize=font_size, color=text_color, size=(640, None), method='caption')
    
    # Set the duration of the text clip
    text_clip = text_clip.set_duration(duration)
    
    # Calculate the height that the text will need to scroll from below the screen to above it
    text_height = text_clip.size[1]
    start_y = 640
    end_y = -text_height
    
    # Define a position function that explicitly returns integers
    def position(t):
        # Calculate y position at time t
        y_position = int(start_y + (end_y - start_y) * t / duration)
        return ('center', y_position)
    
    # Animate the text going from the bottom of the screen to the top
    moving_text = text_clip.set_position(position)
    
    # Create a blank color clip for background
    background = ColorClip(size=(640, 480), color=(0,0,0)).set_duration(duration)
    
    # Composite the text on the background
    video = CompositeVideoClip([background, moving_text], size=(640, 480))
    
    # Load the audio file
    audio = AudioFileClip("star_wars_theme.mp3").set_duration(duration)
    
    # Set the audio of the video
    video = video.set_audio(audio)

    # Set the frames per second
    video.fps = fps
    
    # Write the video to a BytesIO object
    video.write_videofile("temp.mp4", fps=fps, codec="libx264", audio_codec="aac", bitrate="5000k", threads=4, verbose=False, logger=None)
    video_bytes = BytesIO()
    with open('temp.mp4', 'rb') as f:
        video_bytes.write(f.read())
    video_bytes.seek(0)
    
    return video_bytes


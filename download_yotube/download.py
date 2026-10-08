import yt_dlp
from nicegui import ui

url = ui.input(label='Video URL').props('clearable')

ui.label('Choose video quality:')

ui.label('1. 144p')
ui.label('2. 240p')
ui.label('3. 360p')
ui.label('4. 480p')
ui.label('5. 720p')
ui.label('6. 1080p')
ui.label('7. 1440p (2K)')
ui.label('8. 2160p (4K)')

choice = ui.input(label='Enter your choice (1-8)').props('clearable')

qualities = {
    "1": 144,
    "2": 240,
    "3": 360,
    "4": 480,
    "5": 720,
    "6": 1080,
    "7": 1440,
    "8": 2160
}

status = ui.label('')


def download_video():
    selected = choice.value
    video_url = url.value

    if not video_url:
        status.text = 'Please enter a video URL.'
        return

    if selected not in qualities:
        status.text = 'Invalid choice! Please enter a number from 1 to 8.'
        return

    height = qualities[selected]

    status.text = f'Downloading in up to {height}p...'

    options = {
        'format': f'bestvideo[height<={height}]+bestaudio/best',
        'merge_output_format': 'mp4'
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([video_url])

        status.text = 'Download complete!'

    except Exception as e:
        status.text = f'Download failed: {e}'

ui.button('Download', on_click=download_video)

ui.run()
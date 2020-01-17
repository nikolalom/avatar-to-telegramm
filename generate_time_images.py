import time
from PIL import ImageDraw, Image, ImageFont
from datetime import datetime, timedelta

FONT_SIZE = 60
TEXT_Y_POSITION = 1
TEXT_X_POSITION = 1
SAM_UTC = 4 

def convert_time_to_string(dt):
    dt += timedelta(hours=SAM_UTC)
    return f"{dt.hour}:{dt.minute:02}"

def change_img():
    start_time = datetime.utcnow()
    text = convert_time_to_string(start_time)
    row = Image.new('RGBA', (200, 200), "white")
    parsed = ImageDraw.Draw(row)
    font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    font2 = ImageFont.truetype("arial.ttf", 18)
    parsed.text((int(row.size[0]*0.15), int(row.size[1]*0.35)), f'{text}', 
                 align="center", font=font, fill=(0,68,225))
    parsed.text((70, 125),'Самара', 
                 align="center", font=font2, fill=(0,68,225))
    row.save(f'time.png', "PNG")

if __name__ == '__main__':
    change_img()

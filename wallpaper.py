from datetime import datetime as dt

from screeninfo import get_monitors
from PIL import Image, ImageDraw, ImageFont

from utils import rgb_to_tuple, message_box


class Wallpaper:
    def __init__(
            self,
            date:str = '01.01.2000',
            raise_errors:bool = True,
            set_wallpaper:bool = False,
            width:int = None,
            height:int = None
        )->None:
        '''
        Loading the parameters you need to work.
        '''

        self.date = dt.strptime(date, '%d.%m.%Y')
        self.date_month =((dt.now().year - self.date.year)* 12
                           - dt.now().month - self.date.month)
        self.raise_errors = raise_errors
        self.set_wallpaper = set_wallpaper

        if width == None:
            self.width = get_monitors()[0].width
        if height == None:
            self.height = get_monitors()[0].height
         
    def set_theme(
            self,
            bg_color:tuple = (250, 240, 230),
            checkbox_px:int = 19,
            on_state:tuple = (195, 176, 145),
            off_state:tuple = (255, 255, 255),
            outline_color:tuple = (255, 253, 208),
            padding_percent:int = 5
        )->None:
        '''
        Loading theme options.
        '''

        self.bg_color = rgb_to_tuple(bg_color)
        self.checkbox_px = int(checkbox_px)
        self.on_state = rgb_to_tuple(on_state)
        self.off_state = rgb_to_tuple(off_state)
        self.outline_color = rgb_to_tuple(outline_color)
        self.padding_percent = int(padding_percent)
        self.space = int(self.width/100 * self.padding_percent)

    def set_font(
            self,
            font_path:str = None,
            text:str = 'Just do it',
            text_size:int = 100,
            text_color:tuple = (0, 0, 0)
        )->None:
        '''
        Loading text options.
        '''

        self.font_path = font_path
        self.text = text
        self.text_size = int(text_size)            
        self.text_color = rgb_to_tuple(text_color)

    def make_wallpaper(self)->None:
        '''
        Create image.
        '''

        self.image  = Image.new('RGB', (self.width, self.height), self.bg_color)
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype(self.font_path, self.text_size)
        month = 0

        for h in range(self.space, self.height-self.space, self.checkbox_px*2):
            for w in range(self.space, self.width-self.space, self.checkbox_px*2):
                draw.rectangle(
                    (w, h, w+self.checkbox_px, h+self.checkbox_px),
                    fill = (self.on_state if month<self.date_month else self.off_state),
                    outline = self.outline_color)
                month += 1
                if month == 1080:
                    break
            else:
                continue # only executed if the inner loop did NOT break
            break # only executed if the inner loop DID break

        if month != 1080 and self.raise_errors == True:
            message_box(
                title='make_wallpaper error',
                msg =
                '''
                The specified parameters do not allow displaying all
                the months on the screen.
                Try lowering CHECKBOX_PX or PADDING_PERCENT.
                '''
            )
        
        _, _, w, h = draw.textbbox((0, 0), self.text, font=font)
        draw.text(
            ((self.width-w)/2, (self.height-h)/2),
            self.text,
            font=font,
            fill = self.text_color
        )

    def save(self, path:str='pic.png')->None:
        '''
        Save image.
        '''

        self.path = path
        self.image.save(path)


# Life in month

![Platform](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Python Version](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MIT](https://img.shields.io/github/license/artur0527rg/life_in_months)

**Life in month** - this project visualizes 90 years of life in months.

The project can be easily added to Windows startup and does not burden the system like Wallpaper Engine does.

>![Mockup](/imgs/google-pixelbook-mockup.png)


___
## Installation
```bash
$ git clone https://github.com/artur0527rg/life_in_months.git
```
```bash
$ cd life_in_months
```
```bach
$ pip install -r requirements.txt
```

___
## Run on Windows startup
+ Open poject folder
+ Press the **Win + R**, type **shell:startup**
  
    The Windows startup folder will open.
+  Create a **shortcut** to the 'run.cmd' file and **move** it to the **startup folder**

![Autorun](https://im4.ezgif.com/tmp/ezgif-4-9700429ee7.gif)


___
## Configuration

### THEME 
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `BG_COLOR` | `[red, green, blue]` | The background of the final image |
| `CHECKBOX_PX` | `integer` | Cell size in pixels |
| `ON_STATE` | `[red, green, blue]` | Previous month's color |
| `OFF_STATE` | `[red, green, blue]` | Next month's color |
| `PADDING_PERCENT` | `integer` | Offset from display borders in percent |

### FONT
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `FONT_PATH` | `string` | Path to desired font |
| `TEXT` | `string` | Motivational text |
| `TEXT_SIZE` | `integer` | Text size |
| `TEXT_COLOR` | `[red, green, blue]` | The color of text |

### USER
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `BIRTHDAY` | `day.month.year` | Your birthday |

### SETTINGS
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `RAISE_ERRORS` | `bool` | Show render errors |
| `SET_DESKWALLPAPER` | `bool` | Automatically apply wallpaper |


___
## Contributing
Bug reports and/or pull requests are welcome


___
## License

The project is available as open source under the terms of the [MIT License](/LICENSE)
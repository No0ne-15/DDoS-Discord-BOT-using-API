# DDoS Discord BOT ☄️
Hi, 
I'm doing this project out of pure boredom. I plan to make a complete and easy-to-use DDoS bot.
Give a star it's free ⭐

## Features

```
✅ - Launch DDoS Attacks
✅ - Easy config
✅ - CFX Resolver
✅ - Console Attacks logging
✅ - Max attack time in config
❌ - Geo ip command (3 stars ⭐)
❌ - Channel Required to attack (5 stars ⭐)
❌ - Role Required to attack (10 stars ⭐)
❌ - Attacks Cooldown (15 stars ⭐)
❌ - Concurrents system (20 stars ⭐)
```

## Installation

Edit config.json, Change TOKEN, methods lists and api infos
```json
{
    "token": "TOKEN",
    "prefix": ".",
    "status": ".help",

    "l4methods": ["UDP", "OVH", "TCP", "SYN"],
    "l7methods": ["UAM", "BYPASS", "CAPTCHA", "TLS", "BROWSER"],
    
    "api_config": [
        {
            "api_url":"https://api.stresser1.xyz",
            "api_key":"APIKEY",
            "max_time":"1200"
        }
    ],

    "msgGIF": "https://media.discordapp.net/attachments/1252323671310336110/1252323999434805268/standard_1.gif",
    "attackGIF": "https://media.discordapp.net/attachments/1252323671310336110/1252323998436692038/giphy.gif",
    "errorGIF": "https://media.discordapp.net/attachments/1252323671310336110/1252323998948130827/T8kd.gif"
}
```
After that, open a terminal and type :
```bash
c:\No0ne> pip install -r requirements.txt
c:\No0ne> python3 main.py
```

## Preview
  ![alt text](https://media.discordapp.net/attachments/1252323671310336110/1252327935235461321/image.png?ex=6671d0c6&is=66707f46&hm=2ba0868736d5cb82386f14358391d6f8c025963808d3835b86b2972241fab7a0&=&format=webp&quality=lossless)

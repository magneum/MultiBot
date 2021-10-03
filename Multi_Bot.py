"""==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ==================================
ᴇᴠᴇʀʏᴏɴᴇ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 ᴠᴇʀʙᴀᴛɪᴍ ᴄᴏᴘɪᴇꜱ 
ᴏꜰ ᴛʜɪꜱ ʟɪᴄᴇɴꜱᴇ ᴅᴏᴄᴜᴍᴇɴᴛ, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
一デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ一
ʜᴀꜱ ʙᴇᴇɴ ʟɪᴄᴇɴꜱᴇᴅ ᴜɴᴅᴇʀ ɢɴᴜ ɢᴇɴᴇʀᴀʟ ᴘᴜʙʟɪᴄ ʟɪᴄᴇɴꜱᴇ
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯
==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ=================================="""
try:
    import os
    import sys
    import time
    import qrcode
    import pprint
    import random
    import logging
    import pyqrcode
    import platform
    from PIL import Image
    from termcolor import *
    from covid import Covid
    from playsound import *
    # from pygobject import*
    import youtube_dl as Krak
    from gtts import gTTS as speak
except ImportError:
    os.system("pip install -U pip")
    os.system("pip install qrcode")
    os.system("pip install pyqrcode")
    os.system("pip install termcolor")
    # os.system("install-pkg pygobject")
    os.system("pip install playsound")
    os.system("pip install youtube-dl")
    os.system("pip install termcolor")
    os.system("pip install pillow")
    os.system("pip install covid")
    os.system("pip install gtts")
    from gtts import gTTS as speak
    import youtube_dl as Krak
    # from pygobject import*
    from playsound import *
    from covid import Covid
    from termcolor import *
    from PIL import Image
    import platform
    import pyqrcode
    import logging
    import random
    import pprint
    import qrcode
    import time
    import sys
    import os
"""==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ==================================
ᴇᴠᴇʀʏᴏɴᴇ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 ᴠᴇʀʙᴀᴛɪᴍ ᴄᴏᴘɪᴇꜱ 
ᴏꜰ ᴛʜɪꜱ ʟɪᴄᴇɴꜱᴇ ᴅᴏᴄᴜᴍᴇɴᴛ, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
一デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ一
ʜᴀꜱ ʙᴇᴇɴ ʟɪᴄᴇɴꜱᴇᴅ ᴜɴᴅᴇʀ ɢɴᴜ ɢᴇɴᴇʀᴀʟ ᴘᴜʙʟɪᴄ ʟɪᴄᴇɴꜱᴇ
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯
==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ=================================="""


class InterceptHandler(logging.Handler):
    LEVELS_MAP = {
        logging.CRITICAL:
        "CRITICAL",
        logging.ERROR:
        "ERROR",
        logging.WARNING:
        "WARNING",
        logging.INFO:
        "INFO",
        logging.DEBUG:
        "DEBUG"}

    def _get_level(
            self,
            record):
        return self.LEVELS_MAP.get(
            record.levelno,
            record.levelno)

    def emit(self, record):
        logger_opt = logger.opt(
            depth=6,
            exception=record.exc_info,
            ansi=True,
            lazy=True)
        logger_opt.log(self._get_level(record),
                       record.getMessage())


logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)
KrakinzLog = logging.getLogger(__name__)
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    KrakinzLog.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. KRAK quitting.")
    quit(1)
ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ = cprint
"""==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ==================================
ᴇᴠᴇʀʏᴏɴᴇ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 ᴠᴇʀʙᴀᴛɪᴍ ᴄᴏᴘɪᴇꜱ 
ᴏꜰ ᴛʜɪꜱ ʟɪᴄᴇɴꜱᴇ ᴅᴏᴄᴜᴍᴇɴᴛ, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
一デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ一
ʜᴀꜱ ʙᴇᴇɴ ʟɪᴄᴇɴꜱᴇᴅ ᴜɴᴅᴇʀ ɢɴᴜ ɢᴇɴᴇʀᴀʟ ᴘᴜʙʟɪᴄ ʟɪᴄᴇɴꜱᴇ
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯
==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ=================================="""
ӄʀǟӄɨռʐ__զʊǟʟɨȶʏ__ʟɨֆȶ = []
_ӄʀǟӄɨռʐ_ = Krak.YoutubeDL()
ӄʀǟӄɨռʐ__օքȶɨօռֆ = {"format": "bestaudio", "outtmpl": "%(title)s - %(extractor)s-%(id)s.%(ext)s",
                    "no_warnings": True, "ignoreerrors": True, "writethumbnail": True}
ӄʀǟӄɨռʐ__ǟʊɖɨօ = Krak.YoutubeDL(ӄʀǟӄɨռʐ__օքȶɨօռֆ)
ӄʀǟӄɨռʐ__օքȶɨօռֆ = {"format": "best", "outtmpl": "%(title)s - %(extractor)s-%(id)s.%(ext)s",
                    "no_warnings": True, "ignoreerrors": True, "writethumbnail": True}
ӄʀǟӄɨռʐ__ʋɨɖɛօ = Krak.YoutubeDL(ӄʀǟӄɨռʐ__օքȶɨօռֆ)
"""==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ==================================
ᴇᴠᴇʀʏᴏɴᴇ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 ᴠᴇʀʙᴀᴛɪᴍ ᴄᴏᴘɪᴇꜱ 
ᴏꜰ ᴛʜɪꜱ ʟɪᴄᴇɴꜱᴇ ᴅᴏᴄᴜᴍᴇɴᴛ, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
一デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ一
ʜᴀꜱ ʙᴇᴇɴ ʟɪᴄᴇɴꜱᴇᴅ ᴜɴᴅᴇʀ ɢɴᴜ ɢᴇɴᴇʀᴀʟ ᴘᴜʙʟɪᴄ ʟɪᴄᴇɴꜱᴇ
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯
==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ=================================="""


def ӄʀǟӄɨռʐ__ʟɨռӄ__ɨռʄօ(yturl):
    with _ӄʀǟӄɨռʐ_:
        _ӄʀǟӄռʐ_ = _ӄʀǟӄɨռʐ_.extract_info(yturl, download=False)
        for format in _ӄʀǟӄռʐ_["formats"]:
            if not "dash" in str(format["format"]).lower():
                ӄʀǟӄɨռʐ__զʊǟʟɨȶʏ__ʟɨֆȶ.append({
                    "format": format["format"],
                    "filesize": format["filesize"],
                    "format_id": format["format_id"],
                    "yturl": yturl})
        return _ӄʀǟӄռʐ_["title"], _ӄʀǟӄռʐ_["thumbnail"], ӄʀǟӄɨռʐ__զʊǟʟɨȶʏ__ʟɨֆȶ


ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ = """
==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ==================================
ᴇᴠᴇʀʏᴏɴᴇ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 ᴠᴇʀʙᴀᴛɪᴍ ᴄᴏᴘɪᴇꜱ 
ᴏꜰ ᴛʜɪꜱ ʟɪᴄᴇɴꜱᴇ ᴅᴏᴄᴜᴍᴇɴᴛ, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
一デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ一
ʜᴀꜱ ʙᴇᴇɴ ʟɪᴄᴇɴꜱᴇᴅ ᴜɴᴅᴇʀ ɢɴᴜ ɢᴇɴᴇʀᴀʟ ᴘᴜʙʟɪᴄ ʟɪᴄᴇɴꜱᴇ
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯
==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ=================================="""
ӄʀǟӄɨռʐ__ɖօառʟօǟɖɛʀ = """
==================================デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ==================================
ɢɴᴜ ɢᴇɴᴇʀᴀʟ ᴘᴜʙʟɪᴄ ʟɪᴄᴇɴꜱᴇ   
Everyone is permitted to DISTRIBUTE verbatim copies     
of this license document, BUT CHANGING IS NOT ALLOWED  
_| 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 |_
ʜᴀꜱ ʙᴇᴇɴ ʟɪᴄᴇɴꜱᴇᴅ ᴜɴᴅᴇʀ ɢɴᴜ ɢᴇɴᴇʀᴀʟ ᴘᴜʙʟɪᴄ ʟɪᴄᴇɴꜱᴇ 
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 
==================================デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ==================================
"""


def ᴋʀᴀᴋ__ɢʀᴇᴇɴ(text):
    return ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(text, "green")


def ᴋʀᴀᴋ__ʀᴇᴅ(text):
    return ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(text, "red")


def ᴋʀᴀᴋ__ʏᴇʟʟᴏᴡ(text):
    return ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(text, "yellow")


def ᴋʀᴀᴋ__ʙʟᴜᴇ(text):
    return ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(text, "blue")


def ᴋʀᴀᴋ__ᴍᴀɢᴇɴᴛᴀ(text):
    return ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(text, "magenta")


def ᴋʀᴀᴋ__ɢʀᴇʏ(text):
    return ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(text, "grey")


def ᴋʀᴀᴋ__ᴄʏᴀɴ(text):
    return ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(text, "cyan")


"""==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ==================================
ᴇᴠᴇʀʏᴏɴᴇ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 ᴠᴇʀʙᴀᴛɪᴍ ᴄᴏᴘɪᴇꜱ 
ᴏꜰ ᴛʜɪꜱ ʟɪᴄᴇɴꜱᴇ ᴅᴏᴄᴜᴍᴇɴᴛ, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
一デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ一
ʜᴀꜱ ʙᴇᴇɴ ʟɪᴄᴇɴꜱᴇᴅ ᴜɴᴅᴇʀ ɢɴᴜ ɢᴇɴᴇʀᴀʟ ᴘᴜʙʟɪᴄ ʟɪᴄᴇɴꜱᴇ
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯
==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ=================================="""
p = "|--------------------一デ  " + platform.system() + "  デ一--------------------|\n"
ps = platform.system().lower()
pt = cprint(p.upper(), "green")
"""==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ==================================
ᴇᴠᴇʀʏᴏɴᴇ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 ᴠᴇʀʙᴀᴛɪᴍ ᴄᴏᴘɪᴇꜱ 
ᴏꜰ ᴛʜɪꜱ ʟɪᴄᴇɴꜱᴇ ᴅᴏᴄᴜᴍᴇɴᴛ, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
一デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ一
ʜᴀꜱ ʙᴇᴇɴ ʟɪᴄᴇɴꜱᴇᴅ ᴜɴᴅᴇʀ ɢɴᴜ ɢᴇɴᴇʀᴀʟ ᴘᴜʙʟɪᴄ ʟɪᴄᴇɴꜱᴇ
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯
==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ=================================="""
try:
    while True:
        if ps.startswith("wi"):
            os.system("cls")
        elif ps.startswith("li"):
            os.system("clear")
        else:
            os.system("clear")
        ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
        ᴋʀᴀᴋ__ʏᴇʟʟᴏᴡ("""
        =====|一デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ一|=====

                ᴛʏᴘᴇ 1 ꜰᴏʀ ɢᴛᴛꜱ
                ᴛʏᴘᴇ 2 ꜰᴏʀ Qʀᴄᴏᴅᴇʀ
                ᴛʏᴘᴇ 3 ꜰᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ
                ᴛʏᴘᴇ 4 ꜰᴏʀ ᴄᴏᴠɪᴅ ɪɴꜰᴏ ᴇxᴛʀᴀᴄᴛᴏʀ
                ᴛʏᴘᴇ 0 ᴛᴏ ᴇxɪᴛ


        =====|一デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ一|=====
        """)
        Run = int(input(">  "))
        if Run == 0:
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            ᴋʀᴀᴋ__ʀᴇᴅ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
            quit(1)
        elif Run == 1:
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
            ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ("===========================| 𝗚𝗼𝗼𝗴𝗹𝗲 𝗧𝗲𝘅𝘁 𝗧𝗼 𝗦𝗽𝗲𝗲𝗰𝗵 |===========================",
                             "green", attrs=["bold"])
            ᴋʀᴀᴋ__ɢʀᴇᴇɴ("ᴛʏᴘᴇ ᴛʜᴇ ᴛᴇxᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇᴛ ᴀꜱ ᴀ ꜱᴘᴇᴇᴄʜ")
            Tts = input(">   ")
            KRAK = speak(text=Tts, lang="en", slow=True)
            KRAK.save(f"{Tts}.mp3")
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
            ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ("===========================| 𝗚𝗼𝗼𝗴𝗹𝗲 𝗧𝗲𝘅𝘁 𝗧𝗼 𝗦𝗽𝗲𝗲𝗰𝗵 |===========================",
                             "green", attrs=["bold"])
            ᴋʀᴀᴋ__ɢʀᴇᴇɴ("ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʜᴇᴀʀ ᴛʜᴇ ᴀᴜᴅɪᴏ?")
            Listen = input("y/n >   ").lower()
            if Listen == "y":
                playsound(f"{Tts}.mp3")
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(
                    "===========================| 𝗚𝗼𝗼𝗴𝗹𝗲 𝗧𝗲𝘅𝘁 𝗧𝗼 𝗦𝗽𝗲𝗲𝗰𝗵 |===========================", "green", attrs=["bold"])
                ᴋʀᴀᴋ__ɢʀᴇᴇɴ("ʜᴏᴡ ᴍᴀɴʏ ᴛɪᴍᴇꜱ ꜱʜᴏᴜʟᴅ ɪ ᴘʟᴀʏ  [𝘓𝘦𝘴𝘴 𝘵𝘩𝘦𝘯 50 !]")
                Times = int(input(">   "))
                Count_Check = 0
                while Count_Check < Times and not Count_Check == 50:
                    print("ᴛʜᴇ ᴄᴏᴜɴᴛ_ᴄʜᴇᴄᴋ ɪꜱ:", Count_Check+1)
                    playsound(f"{Tts}.mp3")
                    Count_Check = Count_Check + 1
                    print("Done !!")
            elif Listen == "n":
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(
                    "===========================| 𝗚𝗼𝗼𝗴𝗹𝗲 𝗧𝗲𝘅𝘁 𝗧𝗼 𝗦𝗽𝗲𝗲𝗰𝗵 |===========================", "green", attrs=["bold"])
                ᴋʀᴀᴋ__ɢʀᴇᴇɴ("ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴋᴇᴇᴘ ᴛʜᴇ ᴀᴜᴅɪᴏ ᴏʀ ᴅᴇʟᴇᴛᴇ ɪᴛ?")
                Delete = input("y/n >   ").lower()
                if Delete == "y":
                    ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ("ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴀᴜᴛᴏᴄʟᴇᴀɴ ᴄᴏᴅᴇᴄ!", "cyan")
                else:
                    os.remove(f"{Tts}.mp3")
            else:
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(
                    "===========================| 𝗚𝗼𝗼𝗴𝗹𝗲 𝗧𝗲𝘅𝘁 𝗧𝗼 𝗦𝗽𝗲𝗲𝗰𝗵 |===========================", "green", attrs=["bold"])
                ᴋʀᴀᴋ__ɢʀᴇᴇɴ("ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴋᴇᴇᴘ ᴛʜᴇ ᴀᴜᴅɪᴏ ᴏʀ ᴅᴇʟᴇᴛᴇ ɪᴛ?")
                Delete = input("y/n >   ").lower()
                if Delete == "y":
                    ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ("ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴀᴜᴛᴏᴄʟᴇᴀɴ ᴄᴏᴅᴇᴄ!", "cyan")
                else:
                    os.remove(f"{Tts}.mp3")
        elif Run == 2:
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
            ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ("===========================| Qr Code generator |===========================",
                             "green", attrs=["bold"])
            ᴋʀᴀᴋ__ʏᴇʟʟᴏᴡ(
                "ᴘʟᴇᴀꜱᴇ ᴘᴜᴛ ᴛʜᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ʏᴏᴜ ᴡᴀɴᴛ ɪɴꜱɪᴅᴇ ᴛʜᴇ 𝗤𝗥𝗖𝗢𝗗𝗘")
            KB = input(">   ")
            Kustom_Bank = [
                "red", "black",
                "green", "yellow",
                "blue", "magenta",
                "cyan", "Brown",
                "white", "Teal",
                "Silver", "Purple",
                "Gray", "Orange",
                "Maroon", "Aquamarine",
                "Lime", "Crimson",
                "pink", "Golden",
                "Plum", "Olive"
            ]
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ("===========================| Qr Code generator |===========================",
                             "green", attrs=["bold"])
            ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(
                "ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴄᴏʟᴏʀ ᴏꜰ ᴛʜᴇ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ᴏꜰ ʏᴏᴜʀ 𝗤𝗥𝗖𝗢𝗗𝗘", "green")
            Kolor_1 = "1 - red"
            ᴋʀᴀᴋ__ʀᴇᴅ(Kolor_1)
            Kolor_2 = "2 - green"
            ᴋʀᴀᴋ__ɢʀᴇᴇɴ(Kolor_2,)
            Kolor_3 = "3 - yellow"
            ᴋʀᴀᴋ__ʏᴇʟʟᴏᴡ(Kolor_3)
            Kolor_4 = "4 - blue"
            ᴋʀᴀᴋ__ʙʟᴜᴇ(Kolor_4,)
            Kolor_5 = "5 - magenta"
            ᴋʀᴀᴋ__ᴍᴀɢᴇɴᴛᴀ(Kolor_5)
            Kolor_6 = "6 - cyan"
            ᴋʀᴀᴋ__ᴄʏᴀɴ(Kolor_6)
            Kolor_7 = "7 - default white"
            ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(Kolor_7)
            print("8 - for a different color")
            print("9 - for a random color")
            ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ("===========================| Qr Code generator |===========================",
                             "green", attrs=["bold"])
            ᴋʀᴀᴋ__ᴍᴀɢᴇɴᴛᴀ("ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴀ ᴠᴀʟɪᴅ ɴᴜᴍʙᴇʀ ꜰʀᴏᴍ 1-9")
            Kolor_Finally = input(">   ")
            if Kolor_Finally == "1":
                Back_Kolor = "red"
            elif Kolor_Finally == "2":
                Back_Kolor = "green"
            elif Kolor_Finally == "3":
                Back_Kolor = "yellow"
            elif Kolor_Finally == "4":
                Back_Kolor = "blue"
            elif Kolor_Finally == "5":
                Back_Kolor = "magenta"
            elif Kolor_Finally == "6":
                Back_Kolor = "cyan"
            elif Kolor_Finally == "7":
                Back_Kolor = "white"
            elif Kolor_Finally == "8":
                Other_Kustom_Kolor = """
red    green   yellow
blue   magenta   cyan
Brown   white  Teal
Silver Purple   Gray
Orange   Maroon   Aquamarine
Lime   Crimson   pink
Golden   Plum   Olive
"""
                ᴋʀᴀᴋ__ɢʀᴇᴇɴ("ᴄʜᴏᴏꜱᴇ ꜰʀᴏᴍ ᴛʜᴇꜱᴇ\n>  ")
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(Other_Kustom_Kolor)
                Kustom = input(">").lower()
                Back_Kolor = Kustom
            elif Kolor_Finally == "9":
                Back_Kolor = random.choice(Kustom_Bank)
                print(Back_Kolor)
            else:
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(
                    "===========================| Qr Code generator |===========================", "green", attrs=["bold"])
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ((colored("ɢɪᴠᴇɴ ᴡʀᴏɴɢ ɪɴᴘᴜᴛ ꜱᴏ ᴇxɪᴛɪɴɢ",
                                          "red", attrs=["bold"])))
                quit(1)
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
            ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ("===========================| Qr Code generator |===========================",
                             "green", attrs=["bold"])
            ᴋʀᴀᴋ__ᴄʏᴀɴ("""
            =====|一デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ一|=====

                    ᴘʟᴇᴀꜱᴇ ᴛʏᴘᴇ 1 ꜰᴏʀ ᴘɴɢ
                    ᴘʟᴇᴀꜱᴇ ᴛʏᴘᴇ 2 ꜰᴏʀ ꜱᴠɢ
                    ᴘʟᴇᴀꜱᴇ ᴛʏᴘᴇ 3 ꜰᴏʀ ᴊᴘɢ
                        
            =====|一デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ一|=====
            """)
            input_data = input(">  ")
            ᴋʀᴀᴋ__ʏᴇʟʟᴏᴡ("Name of the QRCode file")
            SAVE = input(">   ")
            if input_data == "1":
                QRC = qrcode.QRCode(
                    version=1,
                    box_size=10,
                    border=5)
                QRC.add_data(input_data)
                QRC.make(fit=True)
                QC_IMG = QRC.make_image(fill="black", back_color=Back_Kolor)
                QC_IMG.save(f"{SAVE}.png")
                "Get Desired output as a .png file"
                ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
            elif input_data == "2":
                QRC = qrcode.QRCode(
                    version=1,
                    box_size=10,
                    border=5)
                QRC.add_data(input_data)
                QRC.make(fit=True)
                QC_IMG = QRC.make_image(fill="black", back_color=Back_Kolor)
                QC_IMG.save(f"{SAVE}.svg")
                "Get Desired output as a .svg file"
                ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
            elif input_data == "3":
                QRC = qrcode.QRCode(
                    version=1,
                    box_size=10,
                    border=5)
                QRC.add_data(input_data)
                QRC.make(fit=True)
                QC_IMG = QRC.make_image(fill="black", back_color=Back_Kolor)
                QC_IMG.save(f"{SAVE}.jpg")
                "Get Desired output as a .jpg file"
                ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
            else:
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(
                    "===========================| Qr Code generator |===========================", "green", attrs=["bold"])
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(
                    "ᴛᴏᴏ ʙᴀᴅ ᴍʏ ᴄᴏᴅᴇʀ ᴋɴᴇᴡ ᴛʜᴀᴛ ʜᴜᴍᴀɴꜱ ᴡɪʟʟ ᴛʀʏ ᴀɴʏᴛʜɪɴɢ ʙᴜᴛ 1 ᴏʀ 2", "cyan")
                ᴋʀᴀᴋ__ʀᴇᴅ("𝗪𝗥𝗢𝗡𝗚 𝗜𝗡𝗣𝗨𝗧 \n 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗!! 𝙲𝚢𝚔𝚊 𝙱𝚕𝚢𝚊𝚝")
                ᴋʀᴀᴋ__ɢʀᴇᴇɴ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
                time.sleep(2)
        elif Run == 3:
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            ᴋʀᴀᴋ__ʏᴇʟʟᴏᴡ(ӄʀǟӄɨռʐ__ɖօառʟօǟɖɛʀ)
            ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ("===========================| 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 |===========================",
                             "green", attrs=["bold"])
            ᴋʀᴀᴋ__ɢʀᴇᴇɴ("⭕️ ᴘʟᴇᴀꜱᴇ ᴛʏᴘᴇ ᴀᴜᴅɪᴏ ᴏʀ ᴠɪᴅᴇᴏ")
            AudioVideoManager = input("       :").lower()
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            if AudioVideoManager == "audio":
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                ᴋʀᴀᴋ__ʏᴇʟʟᴏᴡ(ӄʀǟӄɨռʐ__ɖօառʟօǟɖɛʀ)
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(
                    "===========================| 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 |===========================", "green", attrs=["bold"])
                ᴋʀᴀᴋ__ʏᴇʟʟᴏᴡ(
                    "ᴄᴏᴘʏ & ᴘᴀꜱᴛᴇ ᴛʜᴇ ᴜʀʟ ᴏꜰ ᴛʜᴇ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ")
                Linked = input(":- ")
                title, thumbnail_url, formats = ӄʀǟӄɨռʐ__ʟɨռӄ__ɨռʄօ(Linked)
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(title, "yellow")
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(formats, "yellow")
                zxt = Linked.strip()
                ӄʀǟӄɨռʐ__ǟʊɖɨօ.download([zxt])
                ᴋʀᴀᴋ__ᴍᴀɢᴇɴᴛᴀ(
                    "ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ!\n\nᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʟᴏᴄᴀʟ ᴄᴏᴅᴇ ᴀʀᴇᴀ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇ....")
                time.sleep(8)
            elif AudioVideoManager == "video":
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                ᴋʀᴀᴋ__ʏᴇʟʟᴏᴡ(ӄʀǟӄɨռʐ__ɖօառʟօǟɖɛʀ)
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(
                    "===========================| 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 |===========================", "green", attrs=["bold"])
                ᴋʀᴀᴋ__ʏᴇʟʟᴏᴡ(
                    "ᴄᴏᴘʏ & ᴘᴀꜱᴛᴇ ᴛʜᴇ ᴜʀʟ ᴏꜰ ᴛʜᴇ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ")
                Linked = input(":- ")
                title, thumbnail_url, formats = ӄʀǟӄɨռʐ__ʟɨռӄ__ɨռʄօ(Linked)
                ᴋʀᴀᴋ__ʏᴇʟʟᴏᴡ(title)
                ᴋʀᴀᴋ__ᴄʏᴀɴ(formats)
                zxt = Linked.strip()
                ӄʀǟӄɨռʐ__ʋɨɖɛօ.download([zxt])
                ᴋʀᴀᴋ__ᴍᴀɢᴇɴᴛᴀ(
                    "ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ!\n\nᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʟᴏᴄᴀʟ ᴄᴏᴅᴇ ᴀʀᴇᴀ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇ....")
                time.sleep(8)
            else:
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ(
                    "===========================| 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 |===========================", "green", attrs=["bold"])
                ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ((colored("𝗚𝗶𝘃𝗲𝗻 𝗪𝗿𝗼𝗻𝗴 𝗶𝗻𝗽𝘂𝘁 𝘀𝗼 𝗲𝘅𝗶𝘁𝗶𝗻𝗴",
                                          "red", attrs=["bold"])))
                quit(1)
        elif Run == 4:
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            covid = Covid()
            ᴋʀᴀᴋ__ʏᴇʟʟᴏᴡ(ӄʀǟӄɨռʐ__ʟǟɮ__աօʀӄ)
            ӄʀǟӄɨռʐ__ʍɛֆֆǟɢɛ("===========================| Covid Info Extractor |===========================",
                             "green", attrs=["bold"])
            COUNT = ["US", "India", "Brazil", "United Kingdom", "Russia", "France", "Turkey", "Argentina", "Iran", "Colombia", "Spain",
                     "Italy", "Indonesia", "Germany", "Mexico", "Poland", "South Africa", "Ukraine", "Peru", "Philippines", "Netherlands", "Iraq", "Malaysia", "Czechia",
                     "Chile", "Japan", "Canada", "Bangladesh", "Thailand", "Belgium", "Pakistan", "Sweden", "Israel", "Romania", "Portugal", "Kazakhstan", "Morocco",
                     "Hungary", "Jordan", "Switzerland", "Serbia", "Nepal", "United Arab Emirates", "Cuba", "Austria", "Tunisia", "Lebanon", "Greece", "Georgia", "Vietnam",
                     "Saudi Arabia", "Ecuador", "Belarus", "Bolivia", "Guatemala", "Costa Rica", "Sri Lanka", "Bulgaria", "Panama", "Paraguay", "Azerbaijan", "Burma",
                     "Kuwait", "Slovakia", "Uruguay", "Croatia", "Ireland", "West Bank and Gaza", "Dominican Republic", "Denmark", "Honduras", "Venezuela", "Libya",
                     "Ethiopia", "Lithuania", "Oman", "Egypt", "Bahrain", "Moldova", "Slovenia", "Korea, South", "Armenia", "Mongolia", "Kenya", "Qatar", "Bosnia and Herzegovina",
                     "Zambia", "Algeria", "Nigeria", "North Macedonia", "Kyrgyzstan", "Norway", "Botswana", "Uzbekistan", "Afghanistan", "Kosovo", "Albania", "Mozambique",
                     "Latvia", "Estonia", "Finland", "Zimbabwe", "Namibia", "Ghana", "Uganda", "Montenegro", "Cyprus", "iChina", "Cambodia", "El Salvador", "Rwanda",
                     "Cameroon", "Maldives", "Luxembourg", "Senegal", "Jamaica", "Singapore", "Australia", "Malawi", "Cote d'Ivoire", "Congo (Kinshasa)", "Angola",
                     "Fiji", "Trinidad and Tobago", "Eswatini", "Madagascar", "Sudan", "Malta", "Cabo Verde", "Mauritania", "Suriname", "Guinea", "Syria", "Guyana",
                     "Gabon", "Togo", "Haiti", "Seychelles", "Bahamas", "Papua New Guinea", "Somalia", "Timor-Leste", "Tajikistan", "Belize", "Benin", "Laos", "Taiwan*",
                     "Andorra", "Mali", "Lesotho", "Burkina Faso", "Congo (Brazzaville)", "Mauritius", "Burundi", "Nicaragua", "Djibouti", "South Sudan", "Central African Republic",
                     "Iceland", "Equatorial Guinea", "Gambia", "Saint Lucia", "Yemen", "Eritrea", "Sierra Leone", "Guinea-Bissau", "Niger", "Liberia", "Barbados", "San Marino",
                     "Chad", "Comoros", "New Zealand", "Brunei", "Liechtenstein", "Monaco", "Sao Tome and Principe", "Bhutan", "Saint Vincent and the Grenadines", "Dominica",
                     "Antigua and Barbuda", "Grenada", "Tanzania", "Saint Kitts and Nevis", "Summer Olympics 2020", "Diamond Princess", "Holy See", "Solomon Islands",
                     "MS Zaandam", "Marshall Islands", "Vanuatu", "Samoa", "Kiribati", "Palau", "Micronesia"]
            ᴋʀᴀᴋ__ɢʀᴇᴇɴ("ᴘʟᴇᴀꜱᴇ ᴛʏᴘᴇ ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ/ᴄᴏᴅᴇ")
            Country = input(">  ").capitalize()
            if Country in COUNT:
                pass
            else:
                ᴋʀᴀᴋ__ʀᴇᴅ("ɪɴᴠᴀʟɪᴅ ɴᴀᴍᴇ ᴏʀ ɴᴏᴛ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ʏᴇᴛ")
            Cases = covid.get_status_by_country_name(Country)
            pprint.pprint(Cases)
            ᴋʀᴀᴋ__ᴍᴀɢᴇɴᴛᴀ("ᴀᴜᴛᴏ ᴄʟᴇᴀɴɪɴɢ ɪɴ 20 ꜱᴇᴄᴏɴᴅꜱ !")
            time.sleep(20)
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
        else:
            pass
except Exception as E:
    ᴋʀᴀᴋ__ʀᴇᴅ("ERROR      :" + str(E))
"""==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ==================================
ᴇᴠᴇʀʏᴏɴᴇ ɪꜱ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 ᴠᴇʀʙᴀᴛɪᴍ ᴄᴏᴘɪᴇꜱ 
ᴏꜰ ᴛʜɪꜱ ʟɪᴄᴇɴꜱᴇ ᴅᴏᴄᴜᴍᴇɴᴛ, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
一デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ一
ʜᴀꜱ ʙᴇᴇɴ ʟɪᴄᴇɴꜱᴇᴅ ᴜɴᴅᴇʀ ɢɴᴜ ɢᴇɴᴇʀᴀʟ ᴘᴜʙʟɪᴄ ʟɪᴄᴇɴꜱᴇ
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯
==================================デ 🚀🔥 KRAKINZ LΛB 🔥🚀 デ=================================="""

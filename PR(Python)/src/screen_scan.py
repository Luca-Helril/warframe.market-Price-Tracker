from pathlib import Path
import mss


# takes a scranshot of the first monitor
with mss.mss() as sct:
    filename = sct.shot(output="ScreenShot.png")
    print(filename)



# klasse aufrufen die das bild scannen wird
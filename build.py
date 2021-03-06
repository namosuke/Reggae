from fontTools.ttLib.ttFont import newTable
from fontmake import __main__
from fontTools.ttLib import TTFont, newTable
import os, shutil, subprocess

print ("[Reggae One] Generating TTF")
__main__.main(("-g","sources/ReggaeOne.glyphs", "-o","ttf",))

path = "master_ttf/ReggaeOne-Regular.ttf"
hinted = "master_ttf/ReggaeOne-Regular-hinted.ttf"


modifiedFont = TTFont(path)
print ("[Reggae One] Adding stub DSIG")
modifiedFont["DSIG"] = newTable("DSIG")     #need that stub dsig
modifiedFont["DSIG"].ulVersion = 1
modifiedFont["DSIG"].usFlag = 0
modifiedFont["DSIG"].usNumSigs = 0
modifiedFont["DSIG"].signatureRecords = []

print ("[Reggae One] Making other changes")
modifiedFont["name"].addMultilingualName({'ja':'レゲエ One'}, modifiedFont, nameID = 1, windows=True, mac=False)
modifiedFont["name"].addMultilingualName({'ja':'Regular'}, modifiedFont, nameID = 2, windows=True, mac=False)
modifiedFont["head"].flags |= 1 << 3        #sets flag to always round PPEM to integer

modifiedFont.save("fonts/ttf/ReggaeOne-Regular.ttf")

shutil.rmtree("instance_ufo")
shutil.rmtree("master_ufo")
shutil.rmtree("master_ttf")

subprocess.check_call(
    [
        "ttfautohint",
        "--stem-width",
        "nsn",
        "fonts/ttf/ReggaeOne-Regular.ttf",
        "fonts/ttf/ReggaeOne-Regular-hinted.ttf",
    ]
)

shutil.move("fonts/ttf/ReggaeOne-Regular-hinted.ttf", "fonts/ttf/ReggaeOne-Regular.ttf")

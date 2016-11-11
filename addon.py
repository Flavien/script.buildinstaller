import xbmcaddon
import xbmcgui

import os
import xml.etree.ElementTree

# Install all required addons
def execute():
    file_path = xbmc.translatePath(os.path.join("special://profile/", "build.xml"))

    root = xml.etree.ElementTree.parse(file_path).getroot()

    for addon in root.findall("./addons/addon"):
        xbmc.executebuiltin("InstallAddon({id})".format(id = addon.attrib["id"]), True)


# Main script
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo("name")

execute()

xbmcgui.Dialog().ok(addonname, "The build has been restored successfully.")
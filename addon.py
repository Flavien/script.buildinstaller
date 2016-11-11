# Copyright 2016 Flavien Charlon
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import xbmcaddon
import xbmcgui

import os
import xml.etree.ElementTree


# Install all required addons
def execute():
    file_path = xbmc.translatePath(os.path.join("special://profile/", "build.xml"))

    root = xml.etree.ElementTree.parse(file_path).getroot()

    for addon in root.findall("./addon"):
        xbmc.executebuiltin("InstallAddon({id})".format(id = addon.attrib["id"]), True)


# Main script
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo("name")

execute()

xbmcgui.Dialog().ok(addonname, "The build has been restored successfully.")
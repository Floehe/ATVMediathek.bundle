# PMS plugin framework
from datetime import datetime
import time
import re

####################################################################################################

VIDEO_PREFIX = "/video/ATVLibrary"

NAME = "ATVLibrary"

ART = 'terminator.png'
ICON = 'icon.png'

####################################################################################################

# This function is initially called by the PMS framework to initialize the plugin. This includes
# setting up the Plugin static instance along with the displayed artwork.
def Start():

    # Initialize the plugin
    Plugin.AddPrefixHandler(VIDEO_PREFIX, MainMenu, NAME, ICON, ART)
    Plugin.AddViewGroup('List', viewMode = 'List', mediaType = 'items')

    # Setup the artwork associated with the plugin
    MediaContainer.thumb = R(ICON)
    DirectoryItem.thumb = R(ICON)

# This main function will setup the displayed items.
def MainMenu():
    dir = MediaContainer(viewGroup="List")
    dir.Append(Function(DirectoryItem(LiveMenu, "Live")))
    return dir

def LiveMenu(sender):
    dir = MediaContainer(viewGroup = "List")
    
    dir.Append(Function(DirectoryItem(ChannelMenu, "Channel 1"), channel = 1))
    dir.Append(Function(DirectoryItem(ChannelMenu, "Channel 2"), channel = 2))
    dir.Append(Function(DirectoryItem(ChannelMenu, "Channel 3"), channel = 3))

    return dir

def ChannelMenu(sender, channel = None):
    return MessageContainer("test", "test" + str(channel))

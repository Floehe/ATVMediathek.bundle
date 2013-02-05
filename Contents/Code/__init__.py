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
    oc = ObjectContainer(
    	objects = [
	    DirectoryObject(
		key = Callback(EpisodeMenu),
		title = "24 Stunden - SOKO Ost",
		tagline = "Tagline",
		summary = "A summary....",
		thumb = "http://atv.at/static/assets/contentset/teaser_image/3125304.jpg",
	    )
	]
    )
    return oc

def EpisodeMenu():
    #dir = MediaContainer()
    #dir.Append(WebVideoItem("http://atv.at/binaries/asset/tvnext_clip/3161808/video", title = "Test"))

    #return dir
    oc = ObjectContainer()
    oc.add(
	MovieObject(
	    title = "Ein Movie",
	    key = "abacasdjaklsnföalsdgj",
	    rating_key = "lköasjdsdafklasdflö",
	    items = [
		MediaObject(
	            audio_channels = 2,
		    audio_codec = AudioCodec.AAC,
		    video_codec = VideoCodec.H264,
		    container = Container.MP4,
		    parts = [
			PartObject(key="http://atv.at/static/assets/tvnext_clip/video/3305150.mp4"),
			PartObject(key="http://atv.at/static/assets/video_file/video/3305163.mp4"),
			PartObject(key="http://atv.at/static/assets/video_file/video/3305140.mp4")
		    ]    
	    	)
	    ]
	)
    )
    oc.add(
	VideoClipObject(
	    url = "http://atv.at/contentset/3092839-24-stunden---soko-ost/3161808",
	    title = "Tet"
	    #duration = 2892,
	    #original_title = "24 Stunden - SOKO Ost",
	    #source_title = "ATV.at Mediathek",
	    #summary = "Die Soko OST wurde vom Bundesministerium f\u00fcr Inneres speziell zur Bek\u00e4mpfung von Einbr\u00fcchen eingesetzt, mit dem Ziel die Aufkl\u00e4rungsquote zu erh\u00f6hen. Von einer gemeinsamen Einsatzzentrale aus kann die Soko ein l\u00e4nder\u00fcbergreifendes Lagebild erstellen und entsprechende Schwerpunkte durchf\u00fchren. Die Arbeit der Einheit macht auch vor Staatsgrenzen nicht halt, weshalb eine gute Kooperation mit den Nachbarstaaten essentiell f\u00fcr den Erfolg ist. Die Soko geht auch gegen Autodiebe und Menschenschlepper vor. ATV begleitet die Beamten bei ihren t\u00e4glichen Eins\u00e4tzen im Kampf gegen das Verbrechen.",
	    #thumb = "http://devel52-ng.intranet.xoz/atv/uemit/trunk/site/ATV/pub/flash/playcenter/main/images/81x46.png",
	    #art = "http://atv.at/binaries/asset/tvnext_clip/3161808/player_image"
  	)
    )

    return oc 
		

def ChannelMenu(sender, channel = None):
    return MessageContainer("test", "test" + str(channel))

# PMS plugin framework
from datetime import datetime
import time
import re

####################################################################################################

VIDEO_PREFIX = "/video/ATVLibrary"

NAME = "ATVLibrary"

ART = 'terminator.png'
ICON = 'icon.png'

ROOT_URL = "http://atv.at/mediathek"

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

    oc = ObjectContainer()

    for item in HTML.ElementFromURL(ROOT_URL).xpath('//ul[@id="list_shows"]/li'):
    	Log("URL = http://atv.at" + item.xpath('./a[1]/@href')[0])
	#Log("THUMB = " + item.xpath('./a[1]/img[1]/@src')[0])
	#Log("TITLE = " + item.xpath('./a[2]/h3[1]/text()')[0])
	#Log("TAGLINE = " + item.xpath('./a[3]/em[1]/text()')[0])
	#Log("SUMMARY = " + item.xpath('./a[3]/text()[2]')[0].strip())

	oc.add(DirectoryObject(
		key = Callback(EpisodeMenu, url="http://atv.at" + item.xpath('./a[1]/@href')[0]),
		#url = "http://atv.at" + item.xpath('./a[1]/@href')[0],
		title =  item.xpath('./a[2]/h3[1]/text()')[0],
		tagline = item.xpath('./a[3]/em[1]/text()')[0],
		summary = item.xpath('./a[3]/text()[2]')[0].strip(),
		thumb = item.xpath('./a[1]/img[1]/@src')[0]
		)
	)

    return oc

def EpisodeMenu(url):

    oc = ObjectContainer()

    Log("Entering EpisodeMenu with URL: " + url)
    page = HTML.ElementFromURL(url).xpath('//ul[@id="player_playlist_items"]/li')
    Log (page)
#	Log(item.xpath('./div[@class="description]/p/text()')[0])


    oc.add(
	EpisodeObject(
	    title = "Soko OST",
	    key = url,
	    rating_key = url + "_rating_key"
	    #url = "http://atv.at/contentset/3092839-24-stunden---soko-ost/3161808"
	)
    )


    #oc.add(
#	VideoClipObject(
#	    url = "http://atv.at/contentset/3092839-24-stunden---soko-ost/3161808",
#	    title = "Tet"
	    #duration = 2892,
	    #original_title = "24 Stunden - SOKO Ost",
	    #source_title = "ATV.at Mediathek",
	    #summary = "Die Soko OST wurde vom Bundesministerium f\u00fcr Inneres speziell zur Bek\u00e4mpfung von Einbr\u00fcchen eingesetzt, mit dem Ziel die Aufkl\u00e4rungsquote zu erh\u00f6hen. Von einer gemeinsamen Einsatzzentrale aus kann die Soko ein l\u00e4nder\u00fcbergreifendes Lagebild erstellen und entsprechende Schwerpunkte durchf\u00fchren. Die Arbeit der Einheit macht auch vor Staatsgrenzen nicht halt, weshalb eine gute Kooperation mit den Nachbarstaaten essentiell f\u00fcr den Erfolg ist. Die Soko geht auch gegen Autodiebe und Menschenschlepper vor. ATV begleitet die Beamten bei ihren t\u00e4glichen Eins\u00e4tzen im Kampf gegen das Verbrechen.",
	    #thumb = "http://devel52-ng.intranet.xoz/atv/uemit/trunk/site/ATV/pub/flash/playcenter/main/images/81x46.png",
	    #art = "http://atv.at/binaries/asset/tvnext_clip/3161808/player_image"
 # 	)
  #  )

    return oc 
		

def ChannelMenu(sender, channel = None):
    return MessageContainer("test", "test" + str(channel))

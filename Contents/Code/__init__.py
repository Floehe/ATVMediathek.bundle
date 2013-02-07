# PMS plugin framework
from datetime import datetime
import time
import re
import urllib2

####################################################################################################

VIDEO_PREFIX = "/video/ATVMediathek"

NAME = "ATVMediathek"

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
	oc.add(DirectoryObject(
		key = Callback(EpisodeMenu, url="http://atv.at" + item.xpath('./a[1]/@href')[0]),
		title =  item.xpath('./a[2]/h3[1]/text()')[0],
		tagline = item.xpath('./a[3]/em[1]/text()')[0],
		summary = item.xpath('./a[3]/text()[2]')[0].strip(),
		thumb = item.xpath('./a[1]/img[1]/@src')[0]
		)
	)

    return oc

def EpisodeMenu(url):

    oc = ObjectContainer()

    #Log("Entering EpisodeMenu with URL: " + url)
    try:
    	page = getUrl(url)
    except:
	return MessageContainer("Fehler", "Fetching of Information failed, please try again")
    id1 = re.compile('contentset_id%22%3A(.+?)%', re.DOTALL).findall(page)
    id2 = re.compile('active_playlist_id%22%3A(.+?)%', re.DOTALL).findall(page)

    newurl = "http://atv.at/player_playlist_page_json/" + id1[0] + "/" + id2[0] + "/1"
    json = JSON.ObjectFromURL(newurl)
    numberofitems = json['items_count']
    total_page_count = int(json['total_page_count'])

    for index in range(1,total_page_count+1):
	if index == 1:
	    data = json #beacuse we've already fetched it before
	else:
	    newurl = "http://atv.at/player_playlist_page_json/" + id1[0] + "/" + id2[0] + "/" + str(index)
	    try:
	        data =  JSON.ObjectFromURL(newurl)
	    except:
		return MessageContainer("Fehler", "Fetching of Information failed, please try again")

        for idx, item in enumerate(data[str(index)]):
	    try:
	    	season_int = int(item['keyValueSeason'])
	    except:
		season_int = 0
	
	    try:
		absolute_index_int = int(item['keyValueEpisode'])
	    except:
		absolute_index_int = 0

	    try:
	        oc.add(EpisodeObject(
	            url = newurl + "/" + str(idx),
	    	    title = item['title'] + " | " + item['subtitle'],
	    	    summary = item['description'].replace("[br]", "\n"),
	    	    thumb = item['thumbnail_url'],
	    	    art = item['image_url'],
	    	    absolute_index = absolute_index_int,
	    	    season = season_int,
	    	    )
	        )
	    except:
		return MessageContainer("Fehler", "Fetching of Information failed, please try again")
	    
    return oc 
		
def getUrl(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:16.0) Gecko/20100101 Firefox/16.0')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

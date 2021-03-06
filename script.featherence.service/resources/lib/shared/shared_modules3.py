# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,random
import json
from random import shuffle

from variables import *
#from modules import *
from shared_modules import *
from shared_modules5 import *
'''
shared_modules3 is used for Kodi's plugins.
Import the module and input the addDir in your addon module.py file.
'''
def addDir(name, url, mode, iconimage, desc, num, viewtype, fanart=""):
	url2 = url ; printpoint = "" ; returned = "" ; extra = "" ; name2 = "" ; iconimage2 = "" ; desc2 = ""
	text = 'fanart' + space2 + str(fanart)
	printlog(title='addDir_test0', printpoint=printpoint, text=text, level=0, option="")
	name = str(to_utf8(name))
	desc = str(to_utf8(desc))
	fanart = str(to_utf8(fanart))
	
	if '$LOCALIZE' in name or '$ADDON' in name: name = xbmc.getInfoLabel(name)
	if 'www.sdarot.pm' in iconimage:
		iconimage = iconimage.replace('www.sdarot.pm','www.sdarot.wf',1)
	if num == None: num = ""
	if '&getAPIdata=' in str(num):
		finalurl_, id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L = apimaster(num, name, iconimage, desc, fanart, playlist=[], onlydata=True)
		
		if 'getAPIdata' in name and title_L != [] and not 'getAPIdata' in title_L: name = title_L[0]
		if 'getAPIdata' in iconimage:
			if 'getAPIdata' in thumb_L: iconimage = ""
			elif thumb_L != []: iconimage = thumb_L[0]
		if 'getAPIdata' in desc:
			if 'getAPIdata' in desc_L: desc = ""
			elif desc_L != []: desc = desc_L[0]
		if 'getAPIdata' in fanart:
			if 'getAPIdata' in fanart_L: fanart = ""
			elif fanart_L != []: fanart = fanart_L[0]
		
		text = "name" + space2 + str(name) + newline + \
		"title_L" + space2 + str(title_L) + newline + \
		"thumb_L " + space2 + str(thumb_L) + newline + \
		"desc_L" + space2 + str(desc_L) + newline + \
		"fanart_L" + space2 + str(fanart_L) + newline + \
		"fanart" + space2 + str(fanart)
		printlog(title='addDir_test-getAPIdata', printpoint=printpoint, text=text, level=0, option="")
		
	
		
	if iconimage == None or iconimage == "": iconimage = ""
	
	
	if url == None or url == "": url = "None"
	else:
		returned = get_types(url)
		url_ = []
		if 'list' in returned:
			printpoint = printpoint + '3'
			i = 0
			for x in url:
				x_ = "" ; q = ""
				if '&' in x and '=' in x:
					x_ = find_string(x, "&", '=')
					if x != x_:
						pass
					else:
						url_.append(x)
				else: q = 'skipped'
				#print 'i' + space2 + str(i) + space + 'x' + space2 + str(x) + space + 'x_' + space2 + str(x_) + space + 'q' + space2 + str(q) + space + 'url_' + space2 + str(url_)
				i += 1
			for x in url_:
				url.remove(x)
				#print 'x' + space2 + str(x) + space + 'x_' + space2 + str(x_) + space + 'url' + space2 + str(url) + space + 'url_' + space2 + str(url_)
		elif 'str' in returned:
			if '&' in url and '=' in url:
				url_ = find_string(url, "&", '=')
				if url == url_:
					printpoint = printpoint = '9s'
					
		if url == []: printpoint = printpoint + '9'
		else:
			printpoint = printpoint + '4'
			url = str(url)

	if '9' in printpoint: pass
	else:
		if mode >= 100 and 1 + 1 == 3:
			#if url == "": url = "1"
			u=sys.argv[0]+"?url="+str(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&desc="+urllib.quote_plus(desc)+"&num="+urllib.quote_plus(num)+"&viewtype="+str(viewtype)+"&fanart="+str(fanart)
		else:
			u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&desc="+urllib.quote_plus(desc)+"&num="+urllib.quote_plus(num)+"&viewtype="+str(viewtype)+"&fanart="+str(fanart)
		
		
		
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc} )
		try:
			if Fanart_Enable != "" and Fanart_EnableCustom != "": pass
		except:
			Fanart_Enable = "true"
			Fanart_EnableCustom = "false"
			
		fanart2 = setaddonFanart(fanart, Fanart_Enable, Fanart_EnableCustom)
		if fanart2 != "": liz.setProperty('Fanart_Image', fanart2)
			
		menu = []
		menu = menu_list(01, menu, addonID, name, url, mode, iconimage, desc, num, viewtype, fanart)
		
		isFolder = getisFolder(name, url, mode, iconimage, desc, num, viewtype, fanart)
		
		text = "addonID" + space2 + str(addonID) + newline + "name" + space2 + str(name) + newline + "url " + space2 + str(url) + newline + "url2" + space2 + str(url2) + newline + "mode" + space2 + str(mode) + newline + "iconimage" + space2 + str(iconimage) + newline + "desc" + space2 + str(desc) + newline + "num" + space2 + str(num)
		printlog(title='addDir_test1', printpoint=printpoint, text=text, level=0, option="")

		if mode == 41 or mode == 42 or mode == 44:
			liz.setProperty('IsPlayable', 'true')
			liz.setPath(url)

		
		liz.addContextMenuItems(items=menu, replaceItems=False)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
		returned = ok
		checkRandom(url)
		
	text = "name" + space2 + str(name) + newline + \
	"desc" + space2 + str(desc) + space + "addonID" + space2 + str(addonID) + newline + \
	"iconimage" + space2 + str(iconimage) + newline + \
	"num" + space2 + str(num) + newline + \
	"fanart" + space2 + str(fanart)
	printlog(title='addDir', printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''
	if not '9' in printpoint:
		return returned
	
def checkRandom(url):
	'''Check if random has been choosed then create a random playlist of the current view'''
	printpoint = "" ; i = "" ; returned = ""
	#extra = extra + newline + 'scriptfeatherenceservice_random' + space2 + str(xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random)'))
	if xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random)') != "":
		printpoint = printpoint + '0'
		url = CleanString2(url)
		if xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random)') == "true":
			printpoint = printpoint + '1'
			i = 1
			setProperty('script.featherence.service_random', str(i), type="home")
			setProperty('script.featherence.service_randomL', "", type="home")
			for x in range(1,6):
				setProperty('script.featherence.service_random'+str(x), "", type="home")
			
		else:
			printpoint = printpoint + '2'
			i = int(xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random)'))
		
		if i != "":
			if xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random'+str(i)+')') == "":
				printpoint = printpoint + '3'
				returned = str(url)
				setProperty('script.featherence.service_random'+str(i), returned, type="home")
			else:
				printpoint = printpoint + '4'
				returned = xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random'+str(i)+')') + '|' + str(url)
				setProperty('script.featherence.service_random'+str(i), returned, type="home")

			if i == 5: setProperty('script.featherence.service_random', '1', type="home")
			else: setProperty('script.featherence.service_random', str(i + 1), type="home")
				
				
		text = 'i' + space2 + str(i) + newline + \
		"url" + space2 + str(url) + newline + \
		'returned' + space2 + str(returned) + newline + \
		"scriptfeatherenceservice_randomL" + space2 + str(xbmc.getInfoLabel('Window(home).Property(script.featherence.service_randomL)'))
		printlog(title='checkRandom', printpoint=printpoint, text=text, level=0, option="")
		
def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
				params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
					param[splitparams[0]]=splitparams[1]
							
	return param
	
def clean_commonsearch(x, match=False):
	'''Used when searching in YouTube'''
	y = x ; printpoint = ""
	if "commonsearch" in y:
		printpoint = printpoint + '1'
		if addonID == 'plugin.video.featherence.music':
			y = y.replace("commonsearch101", space + commonsearch101)
			y = y.replace("commonsearch102", space + commonsearch102)
			y = y.replace("commonsearch104", space + commonsearch104)
			y = y.replace("commonsearch105", space + commonsearch105)
			y = y.replace("commonsearch106", space + commonsearch106)
			y = y.replace("commonsearch107", space + commonsearch107)
			y = y.replace("commonsearch108", space + commonsearch108)
			y = y.replace("commonsearch109", space + commonsearch109)
			
			y = y.replace("commonsearch111", space + commonsearch111)
			y = y.replace("commonsearch112", space + commonsearch112)
			y = y.replace("commonsearch114", space + commonsearch114)
			y = y.replace("commonsearch115", space + commonsearch115)
			y = y.replace("commonsearch118", space + commonsearch118)
			
		elif addonID == 'plugin.video.featherence.kids':
			y = y.replace("commonsearch101", space + commonsearch101)
		
		elif addonID == 'plugin.video.featherence.rofl':
			y = y.replace("commonsearch101", space + commonsearch101)
			y = y.replace("commonsearch102", space + commonsearch102)
			y = y.replace("commonsearch103", space + commonsearch103)
			y = y.replace("commonsearch104", space + commonsearch104)
		if 'commonsearch' in y:
			y = y.replace('commonsearch',"",1)
		
	count = 0
	while count < 10 and not xbmc.abortRequested:
		if count == 0:
			y = y.replace('[Search]',"")
			y = y.replace('[Video]',"")
			y = y.replace('[Playlist]',"")
			y = y.replace('[Channel]',"")
			y = y.replace('[Sdarot-TV]',"")
		elif '[COLOR=' in y:
			printpoint = printpoint + '4'
			y_ = regex_from_to(y, '[COLOR=', ']', excluding=False)
			y = y.replace(y_,"", 1)
			y = y.replace('[/COLOR]',"", 1)
			
		elif '[' in y and ']' in y:
			printpoint = printpoint + '5'
			y_ = regex_from_to(y, '[', ']', excluding=False)
			y = y.replace(y_,"", 1)
		
		elif y.count('&') > 1 and '=' in y:
			y_ = find_string(y, "&", '&')
			#print 'wwwww ' + str(y_)
			y = y.replace(y_,"",1)
			
		else: count = 40
		count += 1
	
	y = y.replace("  "," ")
	y = y.replace("[","")
	y = y.replace("]","")
	y = y.replace(" ","%20")
	y = y.replace("#","%23")
	if match == True:
		y = '"' + y + '"'
	text = "x" + space2 + str(x) + space + "y" + space2 + str(y)
	printlog(title='clean_commonsearch', printpoint=printpoint, text=text, level=0, option="")
	return y

def LocalSearch(mode, name, url, iconimage, desc, num, viewtype, fanart):
	'''Read lines of a file like .txt and use each line as a YouTube search.'''
	printpoint = "" ; admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)') ; value = "" ; url2 = ""
	url2 = read_from_file(url, silent=True, lines=True, retry=True, printpoint="", addlines='&custom_se=', createlist=False)
	text = 'url2' + space2 + str(url2)
	printlog(title='LocalSearch' + space + name, printpoint=printpoint, text=text, level=0, option="")
	mode = TvMode2(addonID, mode, name, url2, iconimage, desc, num, viewtype, fanart)
	
	return mode
	
def LocalSearch2(mode, name, url, iconimage, desc, num, viewtype, fanart):
	'''Read lines of a file like .txt and use each line to create a folder or play'''
	printpoint = "" ; admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)') ; value = "" ; url2 = ""
	url2 = read_from_file(url, silent=True, lines=True, retry=True, printpoint="", addlines="", createlist=False)
	
	text = 'url2' + space2 + str(url2)
	printlog(title='LocalSearch2' + space + name, printpoint=printpoint, text=text, level=0, option="")
	mode = TvMode2(addonID, mode, name, url2, iconimage, desc, num, viewtype, fanart)
	
	return mode
	
def YoutubeSearch(name, url, desc, num, viewtype):
	'''Search in YouTube command'''
	printpoint = "" ; value = ""
	#print 'blablabla ' + str(name)
	if url == None or url == 'None': url = ""
	name = clean_commonsearch(name)
	try: name = str(name).encode('utf-8')
	except: pass
	
	if name == localize(137) or name == '-' + localize(137):
		'''search'''
		printpoint = printpoint + "1"
		x = desc
		returned = dialogkeyboard("", x, 0, '1', "", "")
		if returned != 'skip':
			printpoint = printpoint + "2"
			value = returned + space + url
			if Search_History == 'true':
				if os.path.exists(Search_History_file): printpoint = printpoint + 'A' ; append = True ; value = '\n' + value
				else: printpoint = printpoint + 'B' ; append = False
				write_to_file(Search_History_file, value, append=append, silent=True , utf8=False)
				
					
		else:
			notification_common("8")
	elif 'commonsearch' in url:
		'''commonsearch'''
		printpoint = printpoint + "3"
		url = clean_commonsearch(url)
		value = name + space + url
	else:
		printpoint = printpoint + '4'
		value = url
	
	if value != "":
		printpoint = printpoint + "7"
		value = clean_commonsearch(value)
		try: value = str(value).encode('utf-8')
		except: pass
		update_view('plugin://plugin.video.youtube/search/?q=' + value, num, viewtype)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = 'name' + space2 + str(name) + newline + \
	"desc" + space2 + str(desc) + newline + \
	"value" + space2 + str(value) + newline + \
	"url" + space2 + str(url) + newline
	printlog(title='YoutubeSearch', printpoint=printpoint, text=text, level=1, option="")
	'''---------------------------'''
	
def ListPlaylist2(name, url, iconimage, desc, num, viewtype, fanart):
	'''View playlists'''
	printpoint = "" ; extra = "" ; TypeError = ""
	if '&dailymotion_pl=' in url:
		finalurl_, id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L = apimaster(url, name, iconimage, desc, fanart, playlist=[], onlydata=False)
		#except Exception, TypeError: extra = extra + newline + "apimaster_TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "6"
		x__count = 0
		for x__ in range(0,len(playlist_L)):
			x__ = '&dailymotion_id=' + str(playlist_L[x__count])
			x__ = x__.replace('plugin://plugin.video.dailymotion_com/?url=',"")
			x__ = x__.replace('&mode=playVideo',"")
			addDir(str(title_L[x__count]), str(x__), 4, str(thumb_L[x__count]), str(desc_L[x__count]), num, viewtype, fanart)
			
			x__count += 1
			extra = extra + newline + 'x__' + space2 + str(url)
		#update_view('plugin://plugin.video.dailymotion_com/?url='+url+'&mode=listVideos', num, viewtype)
	else:
		default = 'plugin://plugin.video.youtube/'
		update_view('plugin://plugin.video.youtube/playlist/' + url + '/', num, viewtype)
		'''---------------------------'''
	
	text = extra
	printlog(title='ListPlaylist2', printpoint=printpoint, text=text, level=0, option="")
	
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    '''---------------------------'''
    return link

def PlayVideos(name, mode, url, iconimage, desc, num, fanart):
	x = url
	playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
	if playerhasvideo: xbmc.executebuiltin('Action(Stop)')
	playlist = [] ; returned = ""
	pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	pl.clear()
	General_TVModeShuffle = getsetting('General_TVModeShuffle')
	
	url = url.replace("[","")
	url = url.replace("]","")
	url = url.replace("'","")
	
	printpoint = "" ; extra = "" ; TypeError = ""
	if 'plugin.' in num:
		if not xbmc.getCondVisibility('System.HasAddon('+ num +')') or not os.path.exists(os.path.join(addons_path, num)):
			notification_common("24")
			installaddon(num, update=True)
			xbmc.sleep(2000)
	
	if '&dailymotion_id=' in url:
		url = url.replace("&dailymotion_id=","")
		installaddonP('plugin.video.dailymotion_com', update=True)
		xbmc.executebuiltin('PlayMedia(plugin://plugin.video.dailymotion_com/?url='+url+'&mode=playVideo)')
				
	elif '&youtube_id=' in url:
		url = url.replace("&youtube_id=","")
		xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/play/?video_id='+ url +')')
		
	elif '&youtube_pl=' in url or '&dailymotion_pl=' in url:
		if '&dailymotion_pl=' in url: installaddonP('plugin.video.dailymotion_com', update=True)
		finalurl_, id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L = apimaster(x, name, iconimage, desc, fanart, playlist=playlist, onlydata=False)
		pl, playlist, printpoint = MultiVideos_play(playlist_L, pl, playlist, printpoint, General_TVModeShuffle, mode)
	
	elif '&googledrive=' in url:
		installaddonP('plugin.video.gdrive', update=True)
		url = url.replace("&googledrive=","")
		
	else: xbmc.executebuiltin('PlayMedia('+ url +')')
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "PlayVideos" + space + 'returned' + space2 + str(returned) + space + "url" + space2 + str(url)
	printlog(title='PlayVideos', printpoint="", text=text, level=0, option="")
	'''---------------------------'''
	return returned
	
def YOULink(mname, url, thumb, desc):
	if not "UKY3scPIMd8" in url or admin:
		ok=True
		url = "plugin://plugin.video.youtube/play/?video_id="+url
		#url='https://gdata.youtube.com/feeds/api/videos/'+url+'?alt=json&max-results=50' #TEST
		liz=xbmcgui.ListItem(mname, iconImage="DefaultVideo.png", thumbnailImage=thumb)
		liz.setInfo( type="Video", infoLabels={ "Title": mname, "Plot": desc } )
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
		text = "url" + space2 + str(url) + space + "mname" + space2 + mname
		printlog(title='YOULink', printpoint="", text=text, level=0, option="")
		return ok
		
def MultiVideos(addonID, mode, name, url, iconimage, desc, num, viewtype, fanart):
	'''read a list of urls, read thier API, put the required mode for each and play or view them'''
	printpoint = "" ; i = 0 ; i2 = 0 ; extra = "" ; desc = str(desc)
	#print 'testtt ' + fanart
	pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	playlist = []
	playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
	if mode == 5: #or mode == 2
		if playerhasvideo:
			xbmc.executebuiltin('Action(Stop)')
		pl.clear()
	
		if "&custom_se11=" in url:
			z = regex_from_to(url, "&custom_se11=", '.txt', excluding=False)
			z_ = z.replace('&custom_se11=',"")
			z__ = read_from_file(z_, silent=True, lines=True, retry=True, printpoint="", addlines="", createlist=False)
			url = url.replace(z, z__,1)
			#print 'testtt ' + 'z' + space2 + str(z) + newline + 'url' + space2 + str(url)
	
	else:
		if name == None: pass
		elif '.' in name:
			'''check if x contain previous positions'''
			name_ = find_string(name, name[:1], '. ')
			name__ = name_.replace('. ',"")
			#notification(name_,name__,"",4000)
			try:
				test = int(name__) + 1
				name = name.replace(name_,"",1)
			except: pass
			
	url2 = url.replace("['","")
	url2 = url2.replace("']","")
	url2 = url2.replace("'","")
	url2 = url2.replace("' ","'")
	url2 = url2.replace("'',","")
	
	url2 = url2.replace("&amp;", "&")
	
	url2 = url2.replace(" &custom_se=","&custom_se=")
	url2 = url2.replace(" &custom_se11=","&custom_se11=")
	url2 = url2.replace(" &custom4=","&custom4=")
	url2 = url2.replace(" &direct4=","&direct4=")
	url2 = url2.replace(" &custom8=","&custom8=")
	url2 = url2.replace(" &direct8=","&direct8=")
	url2 = url2.replace(" &googledrive=","&googledrive=")
	url2 = url2.replace(" &dailymotion_id=","&dailymotion_id=")
	url2 = url2.replace(" &dailymotion_pl=","&dailymotion_pl=")
	
	url2 = url2.replace(" &youtube_ch=","&youtube_ch=")
	url2 = url2.replace(" &youtube_pl=","&youtube_pl=")
	url2 = url2.replace(" &youtube_id=","&youtube_id=")
	url2 = url2.replace(" &youtube_se2=","&youtube_se2=")
	url2 = url2.replace(" &youtube_se=","&youtube_se=")
	
	url2a = url2
	url2 = url2.split(',')
	try: test = General_TVModeShuffle
	except: General_TVModeShuffle = 'true'
	if General_TVModeShuffle == "true" and mode == 5: random.shuffle(url2) ; printpoint = printpoint + "0"
	
	if '&custom_se=' in url2a:
		numTotal = int(len(url2))
		numEnd = int(num) * 20
		numStart = int(numEnd) - 20
		#notification('1',str(numStart),'',1000)
		if numStart < numTotal:
			if int(num) > 1:
				for i__ in range(1,numStart):
					text = 'i__' + space2 + str(i__) + space + str(url2)
					printlog(title="MultiVideos_numbering", printpoint=printpoint, text=text, level=0, option="")
					try: del url2[i__]
					except Exception, TypeError: break
				
				'''show the right number (line) in addDir'''
				i += i__
			if numEnd < numTotal: printpoint = printpoint + 'M'
					
	text = "url " + space2 + str(url) + newline + "url2a" + space2 + str(url2a) + newline + "url2" + space2 + str(url2)
	printlog(title='url_first_check', printpoint="", text=text, level=0, option="")
	#returned = get_types(url)
	counturl2 = 0
	for x in url2:
		x = str(x) ; finalurl = "" ; finalurlL = [] ; numOfItems2 = 0 ; name2 = ""
		x = url2[counturl2]
		if len(url2) < 2:
			'''check if list contain only one item'''
			printpoint = printpoint + 'O'
		counturl2 += 1
		text = "x" + space2 + str(x) + newline + "playlist" + space + str(playlist) + newline + "finalurl" + space2 + str(finalurl) + space + "finalurlL" + space2 + str(finalurlL)
		printlog(title='MultiVideos_test', printpoint=printpoint, text=text, level=0, option="")
		x = x.replace("[","")
		x = x.replace(",","")
		x = x.replace("'","")
		x = x.replace("]","")
		
		if '&' in x and '=' in x:
			'''check if x contain valid statement'''
			x_ = find_string(x, "&", '=')
			if x == x_:
				printpoint = printpoint = 's' ; continue
		
		if '&name_=' in x:
			name2 = find_string(x, '&name_=', '&')
			x = x.replace(name2,"",1)
			name2 = name2.replace('&name_=',"",1)
			name2 = name2.replace('&',"")
			if name2 != "":
				if name2 == 'default': name2 = name
				elif '<url="' in x and '/><title="' in x or "&custom_se11=" in x:
					name = name + space + name2
				else: name = name2
			
		if '<url="' in x and '/><title="' in x or "&custom_se11=" in x:
			'''check if mode == 11'''
			printpoint = printpoint + 'r'
			id_L, title_L, thumb_L, desc_L, fanart_L = checkMode11(mode, name, x, iconimage, desc, num, viewtype, fanart)
			x = id_L[0]
			finalurl_ = x
			
		if x not in playlist and x != "":
			i += 1
			if mode == 5:
				if "&custom4=" in x:
					x = x.replace("&custom4=","")
					finalurl=x
					'''---------------------------'''
				elif "&direct4=" in x:
					x2 = x.replace("&direct4=","")
					title2 = '['+str(x)+']'
					finalurl = listURL(42, name, x2, iconimage, desc, num, 50, fanart)
				elif "&direct8=" in x:
					x2 = x.replace("&direct8=","")
					title2 = '['+str(x)+']'
					id_L, title_L, thumb_L, desc_L = listURLS_(42, name, x2, iconimage, desc, num, 50, fanart)
					finalurl = id_L
					
				elif "&googledrive=" in x:
					x2 = x.replace("&googledrive=","")
					finalurl='plugin://plugin.video.gdrive?mode=streamURL&url=https://docs.google.com/file/d/'+x2+'/preview'
					'''---------------------------'''
					
				elif "&youtube_ch=" in x:
					#try:
					if 1 + 1 == 2:
						finalurl, id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L = apimaster(x, name, iconimage, desc, fanart, playlist=playlist, onlydata=False)
						finalurl = playlist_L
					#except Exception, TypeError: extra = extra + newline + "apimaster_TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "6"
					'''---------------------------'''
				elif "&youtube_pl=" in x:
					#x = x.replace("&youtube_pl=","")
					#try:
					if 1 + 1 == 2:
						finalurl_, id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L = apimaster(x, name, iconimage, desc, fanart, playlist=playlist, onlydata=False)
						finalurl = playlist_L
					#except Exception, TypeError: extra = extra + newline + "apimaster_TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "6"
					'''---------------------------'''
				elif "&youtube_id=" in x:
					x = x.replace("&youtube_id=","")
					finalurl="plugin://plugin.video.youtube/play/?video_id="+x+"&hd=1"
					'''---------------------------'''
				elif "&youtube_se2=" in x or "&youtube_se=" in x or "&custom_se=" in x:
					if 'commonsearch' in x: x = x + space + str(name)
					#try:
					if 1 + 1 == 2:
						finalurl_, id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L = apimaster(x, name, iconimage, desc, fanart, playlist=playlist, onlydata=False)
						finalurl = playlist_L
					#except Exception, TypeError: extra = extra + newline + "apimaster_TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "6"

				elif "&dailymotion_id=" in x:
					x = x.replace("&dailymotion_id=","")
					finalurl='plugin://plugin.video.dailymotion_com/?url='+x+'&mode=playVideo'
				elif "&dailymotion_pl=" in x:
					try:
						finalurl_, id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L = apimaster(x, playlist=playlist, onlydata=False)
						finalurl = playlist_L
					except Exception, TypeError: extra = extra + newline + "apimaster_TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "6"
				else: printpoint = printpoint + "Z"
				extra = extra + newline + str(i) + space2 + str(finalurl)
				'''---------------------------'''
				#title= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$title'][u'$t'].encode('utf-8')).decode('utf-8')
				#thumb =str(prms['feed'][u'entry'][i][ u'media$group'][u'media$thumbnail'][2][u'url'])
				#description = str(prms['feed'][u'entry'][i][ u'media$group'][u'media$description'][u'$t'].encode('utf-8')).decode('utf-8')
				
				#notification(str(int(len(playlist))),'','',5000)
				pl, playlist, printpoint = MultiVideos_play(finalurl, pl, playlist, printpoint, General_TVModeShuffle, mode)
				
				if 'x' in printpoint: break
				
			elif mode == 6:
				if not 'r' in printpoint: finalurl_, id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L = apimaster(x, name, iconimage, desc, fanart, playlist=playlist, onlydata=True)
				#except: pass
				for y in title_L:
					if name2 != "":
						if 'r' in printpoint:
							y = y.replace(y, name + space + name2)
						else:
							y = y.replace(y, name)
					y = y.replace(y,str(i) + '. ' + y, 1)
					
				if finalurl_ == "": pass
				elif "&custom_se11=" in x:
					title2 = '[Web]'
					x = x.replace("&custom_se11=","")
					addDir(str(i) + '.' + space + title_L[0] + space + title2, x, 11, thumb_L[0], desc_L[0], num, viewtype, fanart_L[0])
				elif "&custom4=" in x:
					title2 = gettitle2(x)
					x = x.replace("&custom4=","")
					addDir(str(i) + '.' + space + title_L[0] + title2, x, 4, thumb_L[0], desc_L[0], num, viewtype, fanart_L[0])
					'''---------------------------'''
				elif "&direct4=" in x:
					x = x.replace("&direct4=","")
					addDir(str(i) + '.' + space + title_L[0], x, 44, thumb_L[0], desc_L[0], num, viewtype, fanart_L[0])
					'''---------------------------'''
				elif "&custom8=" in x:
					title2 = gettitle2(x)
					x = x.replace("&custom8=","")
					addDir(str(i) + '.' + space + title_L[0] + title2, x, 8, thumb_L[0], desc_L[0], num, viewtype, fanart_L[0])
					'''---------------------------'''
				elif "&direct8=" in x:
					x = x.replace("&direct8=","")
					addDir(str(i) + '.' + space + title_L[0], x, 40, thumb_L[0], desc_L[0], num, viewtype, fanart_L[0])
					'''---------------------------'''
				elif "&googledrive=" in x:
					if 'O' in printpoint:
						PlayVideos(title_L[0], 4, x, thumb_L[0], desc_L[0], num, fanart_L[0])
						mode = 4
					else:
						title2 = '[googledrive]'
						addDir(str(i) + '.' + space + title_L[0] + space + title2, x, 4, thumb_L[0], desc_L[0], num, viewtype, fanart_L[0])
						'''---------------------------'''
				elif "&dailymotion_id=" in x:
					#x = x.replace("&dailymotion_id=","")
					if 'O' in printpoint:
						PlayVideos(title_L[0], 4, x, thumb_L[0], desc_L[0], num, fanart_L[0])
						mode = 4
					else:
						addDir(str(i) + '.' + space + title_L[0], x, 4, thumb_L[0], desc_L[0], num, viewtype, fanart_L[0])
						'''---------------------------'''
				elif "&dailymotion_pl=" in x:
					if 'O' in printpoint:
						ListPlaylist2(name, x, iconimage, desc, num, viewtype, fanart)
						#mode = 13
					else: addDir(str(i) + '.' + space + title_L[0], x, 17, thumb_L[0], desc_L[0], num, viewtype, fanart_L[0])
				elif "&youtube_ch=" in x:
					#x = x.replace("&youtube_ch=","")
					#if "/playlists" in x: x = x.replace("/playlists","")
					if 'O' in printpoint:
						YOUList2(name, url, iconimage, desc, num, viewtype)
						mode = 9
					else: mode_ = addDir(str(i) + '.' + space + title_L[0], x, 17, thumb_L[0], desc_L[0], num, viewtype, fanart_L[0]) #addonString(192).encode('utf-8')
					
					'''---------------------------'''
				elif "&youtube_pl=" in x:
					#x = x.replace("&youtube_pl=","")
					if 'O' in printpoint:
						ListPlaylist2(name, url, iconimage, desc, num, viewtype, fanart)
						mode = 13
					else: addDir(str(i) + '.' + space + title_L[0], x, 17, thumb_L[0], desc_L[0], num, viewtype, fanart_L[0]) #addonString(192).encode('utf-8')
					'''---------------------------'''
				elif "&youtube_id=" in x:
					#x = x.replace("&youtube_id=","")
					addDir(str(i) + '.' + space + title_L[0], x, 4, thumb_L[0], desc_L[0], num, viewtype, fanart_L[0])
					'''---------------------------'''
				elif "&youtube_se2" in x or "&youtube_se=" in x or "&custom_se=" in x:
					#try: str(name).encode('utf-8')
					#except: str(name)
					x = x.replace("&youtube_se2=","")
					x = x.replace("&youtube_se=","")
					x = x.replace("&custom_se=","")
					#x = x + space + str(name)
					#x = clean_commonsearch(x)
					#print 'testme ' + str(x)
					if 'O' in printpoint:
						YoutubeSearch(name, x, desc, num, viewtype)
						mode = 3
					else:
						addDir(str(i) + '.' + space + title_L[0], x, 3, thumb_L[0], desc_L[0], num, viewtype, fanart_L[0])
				
				if 1 + 1 == 2:
					if 'M' in printpoint:
						if i >= numEnd:
							addDir('Next Page', url, mode, iconimage, desc, str(int(num) + 1), viewtype, fanart)
							break
					
			else: printpoint = printpoint + 'y'
		else: extra = extra + newline + 'x' + space2 + str(x) + space + 'is in playlist or empty!'
		
		if 'r' in printpoint: printpoint = printpoint.replace('r',"")
	if mode == 5:
		playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
		if playlist == []: notification(addonString_servicefeatherence(32408).encode('utf-8'), addonString_servicefeatherence(32409).encode('utf-8'), "", 2000)
		#xbmc.executebuiltin('RunScript('+addonID+'/?mode=6&name='+name+'&url='+url+'&iconimage='+str(iconimage)+'&desc='+desc+'&num='+str(num)+'&viewtype='+str(viewtype)+')')
		#MultiVideos(6, name, url, iconimage, desc, num, viewtype, fanart)
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "mode" + space2 + str(mode) + space + "i" + space2 + str(i) + space + "num " + space2 + str(num) + newline + \
	"url " + space2 + str(url) + newline + \
	"url2" + space2 + str(url2) + newline + \
	"fanart" + space2 + str(fanart) + newline + \
	"pl" + space2 + str(pl) + space + "playlist" + space2 + str(len(playlist)) + space + str(playlist) + newline + \
	"finalurl" + space2 + str(finalurl) + space + "finalurlL" + space2 + str(finalurlL) + space + newline + extra
	printlog(title="MultiVideos", printpoint=printpoint, text=text, level=2, option="")
	'''---------------------------'''
	return mode

def MultiVideos_play(finalurl, pl, playlist, printpoint, General_TVModeShuffle, mode):
	'''Prepare the first available video in the playlist'''
	count = 0 ; finalurlN = 0 ; printpoint2 = ""
	playlistN = int(len(playlist))

	if finalurl != "" and finalurl != []:
		printpoint2 = printpoint2 + '0'
		returned = get_types(finalurl)
		if 'list' in returned:
			printpoint2 = printpoint2 + '1'
			finalurlN = int(len(finalurl))
			if General_TVModeShuffle == "true": random.shuffle(finalurl) ; printpoint = printpoint + "0"
			
		elif 'str' in returned:
			printpoint2 = printpoint2 + '2'
			finalurlN = 1
		else: printpoint2 = printpoint2 + '9'
		
		if finalurlN > 0:
			if '1' in printpoint2:
				for y in finalurl:
					pl, playlist, printpoint = MultiVideos_play2(y, pl, playlist, printpoint)
					count += 1
					playlistN = int(len(playlist))
					if count > finalurlN: break
					elif playlistN >= 40:
						printpoint = printpoint + 'x'
						break
					elif '3' in printpoint:
						playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
						playlistlength = xbmc.getInfoLabel('Playlist.Length(video)')
						if not playerhasvideo or int(playlistlength) >= 40:
							printpoint = printpoint + 'x_'
							#print 'playlistlength' + space2 + str(playlistlength)
							break
							
			elif '2' in printpoint2:
				pl, playlist, printpoint = MultiVideos_play2(finalurl, pl, playlist, printpoint)
	
	playlistN = int(len(playlist))
	if playlistN >= 40:
		printpoint = printpoint + 'x'
	text = 'finalurl' + space2 + str(finalurl) + newline + \
	'pl' + space2 + str(pl) + newline + \
	'playlist' + space2 + str(playlist) + newline + \
	'count' + space2 + str(count) + space + 'playlistN' + space2 + str(playlistN) + space + 'finalurlN' + space2 + str(finalurlN)
	printlog(title="MultiVideos_play", printpoint=printpoint + space + 'printpoint2' + space2 + str(printpoint2), text=text, level=0, option="")
	return pl, playlist, printpoint

def MultiVideos_play2(finalurl, pl, playlist, printpoint):
	'''Play the first available video in the playlist'''
	count = 0 ; printpoint2 = "" ; numOfItems2 = 0
	pl.add(finalurl)
	playlist.append(finalurl)
	if '606' in printpoint or '66' in printpoint:
		notification_common('8')
		sys.exit(0)
	elif not "3" in printpoint:
		'''play first video in the list'''
		if 'plugin://' in finalurl:
			printpoint = printpoint + '3'
			plugin = regex_from_to(finalurl, 'plugin://', '/', excluding=True)
			plugin = regex_from_to(plugin, 'plugin://', '?', excluding=True)
			if plugin != "": installaddon(plugin, update=True)
			
		xbmc.Player().play(pl) ; xbmc.sleep(2000)
		#xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl) ; xbmc.sleep(2000)
		
		playerhasvideo = xbmc.getCondVisibility('Player.HasVideo') ; dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOK.xml)') ; dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)') ; dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)') ; dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
		while count < 20 and not playerhasvideo and not dialogokW and not xbmc.abortRequested:
			xbmc.sleep(200)
			playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
			dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOK.xml)')
			dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
			dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
			dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
			if dialogselectW: xbmc.sleep(1000)
			elif not dialogbusyW and not dialogprogressW: count += 2
			else: count += 1
			
		if playerhasvideo and not dialogokW: printpoint = printpoint + "3"
		else:
			dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOK.xml)')
			if dialogokW or count >= 20:
				printpoint = printpoint + '6'
				xbmc.executebuiltin('Dialog.Close(okdialog)')
				#xbmc.executebuiltin('Action(Close)') ; xbmc.sleep(100)
				x = finalurl.replace('plugin://plugin.video.youtube/play/?video_id=',"")
				x = x.replace('&hd=1',"")
				notification('Video error: ' + str(x),'Trying to play next video','',2000)
				'''---------------------------'''
			
	text = 'finalurl' + space2 + str(finalurl) + newline + \
	'pl' + space2 + str(pl) + newline + \
	'playlist' + space2 + str(playlist) + newline + \
	'count' + space2 + str(count)
	printlog(title="MultiVideos_play2", printpoint=printpoint, text=text, level=0, option="")
	return pl, playlist, printpoint
		
def apimaster(x, title="", thumb="", desc="", fanart="", playlist=[], addonID=addonID, onlydata=True):
	'''return API information for YouTube and DailyMotion'''
	'''playlist_L = store new videos from x'''
	'''playlist = store up to date videos for comparision'''
	#addonID=addonID
	printpoint = "" ; TypeError = "" ; extra = "" ; page = 1 ; count = 0 ; count_ = 0 ; i = 0 ; totalResults = 0 ; pagesize = 40
	id_L = [] ; playlist_L = [] ; title_L = [] ; thumb_L = [] ; desc_L = [] ; fanart_L = [] ; nextpagetoken_L = [""]
	id_ = ""   ; finalurl_ = ""   ; title_ = "" ; thumb_ = ""  ; desc_ = ""  ; fanart_ = "" ; nextpagetoken = ""
	valid_ = "" ; invalid__ = "" ; duplicates__ = "" ; except__ = "" ; url = "" ; title2 = "" ; prms = "" ;  link = ""
	resultsPerPage = pagesize
	
	finalurl_ = x
	
	if onlydata == True:
		maxResults = '5'
		thumbnails = u'medium'
		if '&getAPIdata=' in x:
			printpoint = printpoint + 'A'
			if x[:1] == '[': x = x.replace('[',"",1)
			if x[-1:] == ']': x = x.replace(']',"")
			if x[:1] == "'": x = x.replace("'","",1)
			if x[-1:] == "'": x = x.replace("'","")
			#x = find_string(title, "getAPIdata=", "")
			x = x.replace('&getAPIdata=',"")
			#print 'blabla' + space2 + str(x)
	
	else:
		maxResults = '40'
		thumbnails = u'default'
		returned = get_types(playlist)
		if not 'list' in returned:
			printpoint = printpoint + '0'
			playlist = []
		try:
			count_ = int(len(playlist))
			#count = 0 + int(count_)
		except Exception, TypeError: extra = extra + newline + 'count_ TypeError: ' + str(TypeError)
	
	x2 = x
	videoDuration = 'any'
	videoDefinition = 'any'
	safeSearch = 'moderate'

	if '&videoDuration=' in x:
		videoDuration = regex_from_to(x, '&videoDuration=', '&', excluding=True)
		x = x.replace('&videoDuration='+videoDuration+'&',"")
		#notification(x,videoDuration,'',2000)
	
	if General_TVModeQuality == '1':
		videoDefinition = 'high'
		
	if '&videoDefinition=' in x:
		videoDefinition = regex_from_to(x, '&videoDefinition=', '&', excluding=True)
		x = x.replace('&videoDefinition='+videoDefinition+'&',"")
		#notification(x,videoDefinition,'',2000)
		
	if addonID == 'plugin.video.featherence.docu':
		pass
		#videoDefinition = 'high'
	
	if addonID == 'plugin.video.featherence.kids':
		safeSearch = 'strict'
	
	if "&youtube_pl=" in x:
		printpoint = printpoint + "1"
		title2 = '[Playlist]'
		x2 = x.replace("&youtube_pl=","")
		if onlydata == True:
			url = 'https://www.googleapis.com/youtube/v3/playlists?id='+x2+'&key='+api_youtube_featherence+'&part=snippet&maxResults=1&pageToken='
		else:
			url = 'https://www.googleapis.com/youtube/v3/playlistItems?playlistId='+x2+'&key='+api_youtube_featherence+'&part=snippet&maxResults='+maxResults+'&pageToken='
		
	elif '&youtube_id=' in x:
		title2 = '[Video]'
		x2 = x.replace('&youtube_id=',"")
		url = 'https://www.googleapis.com/youtube/v3/videos?id='+x2+'&key='+api_youtube_featherence+'&part=snippet'
	elif "&youtube_se=" in x:
		title2 = '[Search]'
		printpoint = printpoint + "2"
		x2 = x.replace("&youtube_se=","")
		if 'commonsearch' in x:
			printpoint = printpoint + 'c'
			x2 = to_utf8(title) + space + to_utf8(x2)
			x2 = clean_commonsearch(x2, match=False)
		url = 'https://www.googleapis.com/youtube/v3/search?q='+x2+'&key='+api_youtube_featherence+'&videoDuration='+videoDuration+'&videoDefinition='+videoDefinition+'&safeSearch='+safeSearch+'&type=video&part=snippet&maxResults='+maxResults+'&pageToken='
	elif "&youtube_se2=" in x:
		'''WIP'''
		printpoint = printpoint + "5"
		title2 = '[Search]'
		x2 = x.replace("&youtube_se2=","")
		#x = clean_commonsearch(x)
		#url = 'https://www.googleapis.com/youtube/v3/search?q='+x+'&key='+api_youtube_featherence+'&safeSearch='+safeSearch+'&type=channel&part=snippet&maxResults='+maxResults+'&pageToken='
		#url = 'https://www.googleapis.com/youtube/v3/search?channelId='+id+'&key='+api_youtube_featherence+'&videoDefinition='+videoDefinition+'&type=video&part=snippet&maxResults='+maxResults
		#url = 'https://www.googleapis.com/youtube/v3/search?q='+x2+'&key='+api_youtube_featherence+'&safeSearch=moderate&type=channel&part=snippet&maxResults=1&pageToken='
	elif "&custom_se=" in x:
		text = 'xxx' + space2 + str(x)
		title2 = '[Search2]'
		printlog(title='apimaster_test1', printpoint=printpoint, text=text, level=0, option="")
		printpoint = printpoint + "3"
		x2 = x.replace("&custom_se=","")
		x2 = clean_commonsearch(x2)
		url = 'https://www.googleapis.com/youtube/v3/search?q='+x2+'&key='+api_youtube_featherence+'&videoDuration='+videoDuration+'&videoDefinition='+videoDefinition+'&safeSearch='+safeSearch+'&type=video&part=snippet&maxResults=1&pageToken='
	elif "&youtube_ch=" in x:
		printpoint = printpoint + "4"
		title2 = '[Channel]'
		x2 = x2.replace('&youtube_ch=',"")
		if '/playlists' in x:
			x2 = x2.replace('/playlists',"")
		
		url = 'https://www.googleapis.com/youtube/v3/channels?forUsername='+x2+'&key='+api_youtube_featherence+'&part=snippet&maxResults='+maxResults
		link = OPEN_URL(url)
		#print 'link__' + space2 + str(link)
		if '"totalResults": 0' in link or '"items": []' in link:
			printpoint = printpoint + '2'
			url = 'https://www.googleapis.com/youtube/v3/channels?id='+x2+'&key='+api_youtube_featherence+'&part=snippet&maxResults='+maxResults
			
		if onlydata == True: pass
		else:
			link = OPEN_URL(url)
			prms=json.loads(link)
			try: id_ = str(prms['items'][i][u'id'])
			except: id_ = str(prms['items'][i][u'snippet'][u'channelId'])
			url = 'https://www.googleapis.com/youtube/v3/search?channelId='+id_+'&key='+api_youtube_featherence+'&part=snippet&maxResults='+maxResults

	elif '&dailymotion_id=' in x:
		title2 = '[Video]'
		x2 = x.replace('&dailymotion_id=',"")
		url = 'https://api.dailymotion.com/video/'+x2+'/?fields=description,duration,id,owner.username,taken_time,thumbnail_large_url,title,views_total&family_filter=1&localization=en'
		
	elif '&dailymotion_pl=' in x:
		printpoint = printpoint + '7'
		title2 = '[Playlist]'
		x2 = x.replace('&dailymotion_pl=',"")
		url = 'https://api.dailymotion.com/playlist/'+x2+'/videos?fields=description,duration,id,owner.username,taken_time,thumbnail_large_url,title,views_total&sort=recent&limit=40&family_filter=1&localization=en&page=1'
		#url = 'https://api.dailymotion.com/playlist/'+x2
	else: printpoint = printpoint + "8"
	
	text = 'x' + space2 + str(x) + newline + \
	'x2' + space2 + str(x2) +newline + \
	'url' + space2 + str(url) + newline + \
	'onlydata' + space2 + str(onlydata)
	printlog(title='apimaster_test2', printpoint=printpoint, text=text, level=0, option="")
	
	if url != "":
		if 'A' in printpoint: title2 = ""
		#if not 'c' in printpoint or 1 + 1 == 2:
		try: link = OPEN_URL(url)
		except Exception, TypeError:
			printpoint = printpoint + '9'
			extra = extra + newline + 'TypeError' + space2 + str(TypeError)
			text = '***The following video ID is broken!' + space + str(title) + space + str(x) + '***'
			printlog(title='apimaster_video error!', printpoint=printpoint, text=text, level=1, option="")
			title_L.append('[COLOR=red]' + title + space + '[Deleted!]' + '[/COLOR]')
		if not '9' in printpoint:
			
			prms=json.loads(link)
			text = "url" + space2 + str(url) + newline + \
			"link" + space2 + str(link) + newline + \
			"prms" + space2 + str(prms) + newline #+ \ + "totalResults" + space2 + str(totalResults)
			'''---------------------------'''
			printlog(title='apimaster_test2', printpoint=printpoint, text=text, level=0, option="")
		
			if '&dailymotion_pl=' in x:
				if prms[u'has_more']:
					totalResults = int(prms[u'limit'])
				else: totalResults = prms[u'total']
			elif '&dailymotion_id=' in x:
				if prms[u'id']:
					totalResults = len(prms[u'id'])
			else:
				totalResults=int(prms['pageInfo'][u'totalResults']) #if bigger than pagesize needs to add more result
				resultsPerPage = int(prms['pageInfo'][u'resultsPerPage'])
				try:
					nextpagetoken = str(prms['nextPageToken'])
					nextpagetoken_L.append(nextpagetoken)
				except:
					pass
					
				if '&youtube_pl=' in x:
					
					count__ = 0
					while count__ < 10 and not xbmc.abortRequested:
						url_ = url.replace('&pageToken=', '&pageToken=' + nextpagetoken)
						#try:
						if 1 + 1 == 2:
							if totalResults / resultsPerPage > 1: notification(str(len(nextpagetoken_L) - 1) + space + '/' + space + str(totalResults / resultsPerPage),"","",2000)
							link_ = OPEN_URL(url_)
							prms_=json.loads(link_)
							
							
							try:
								nextpagetoken = str(prms_['nextPageToken'])
								nextpagetoken_L.append(nextpagetoken)
							except: count__ = 10
							
						text = 'nextpagetoken_L' + space2 + str(nextpagetoken_L) + newline + \
						"url_" + space2 + str(url_) + newline + \
						"link_" + space2 + str(link_) + newline + \
						"prms_" + space2 + str(prms_)
						printlog(title='apimaster_playlisttoken', printpoint=printpoint, text=text, level=0, option="")

						count__ += 1
					
					
					max = len(nextpagetoken_L) - 1
					returned, value = getRandom(0, min=0, max=max, percent=50)
					if value == "": value = 0
					else:
						url = url.replace('&pageToken=', '&pageToken=' + nextpagetoken_L[int(value)])
						link = OPEN_URL(url)
						prms=json.loads(link)
					
			totalpagesN = (totalResults / pagesize) + 1
			'''---------------------------'''

		i = 0
		while i < pagesize and i < totalResults and i < resultsPerPage and not "8" in printpoint and ((count + count_) < pagesize) and not xbmc.abortRequested: #h<totalResults
			
			#try:
			if 1 + 1 == 2:
				id_ = "" ; id2_ = "" ; playlistid_ = ""
				finalurl_ = "" ; title_ = "" ; thumb_ = "" ; desc_ = "" ; fanart_ = ""
				
				if "&youtube_pl=" in x or "&youtube_ch=" in x or '&youtube_id=' in x:
					if onlydata == True:
						try: id_ = str(prms['items'][i][u'id'])
						except: pass
					else:
						try: id_ = str(prms['items'][i][u'snippet'][u'resourceId'][u'videoId']) #Video ID (Playlist)
						except:
							try: playlistid_ = str(prms['items'][i][u'id'][u'playlistId'])
							except:
								try: id_ = str(prms['items'][i][u'id'][u'videoId'])
								except:
									try: id_ = str(prms['items'][i][u'id'])
									except: id_ = ""
								
				elif "&youtube_se=" in x or '&custom_se=' in x:
					if onlydata == True:
						id_ = str(prms['items'][i][u'id'][u'videoId']) #Video ID (Search)
					else:
						#print str(i)
						id_ = str(prms['items'][i][u'id'][u'videoId']) #Video ID (Search)		
				elif '&youtube_se2=' in x:
					id_ = str(prms['items'][i][u'snippet'][u'channelId']) #Video ID (Search)
				elif '&dailymotion_id=' in x:
					id2_ = str(prms[u'id'])
				elif '&dailymotion_pl=' in x:
					#if onlydata == True:
					id2_ = str(prms[u'list'][i][u'id'])
						
				
				if id_ != "":
					#if '&youtube_pl=' in x: finalurl_ = "plugin://plugin.video.youtube/playlist/"+id_+"/"
					finalurl_ = "plugin://plugin.video.youtube/play/?video_id="+id_+"&hd=1"
					title_ = str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
					try:
						thumb_ = str(prms['items'][i][u'snippet'][u'thumbnails'][thumbnails][u'url'])
						fanart_ = str(prms['items'][i][u'snippet'][u'thumbnails'][u'high'][u'url'])
					except Exception, TypeError: extra = extra + newline + 'thumb TypeError: ' + str(TypeError) + space + 'i' + space2 + str(i) + space + 'id_' + space2 + str(id_)
					desc_ = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8'))
					
					
					id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L, count, invalid__, duplicates__ = apimaster2(playlist, id_, id_L, finalurl_, playlist_L, title_, title_L, title2, thumb_, thumb_L, desc_, desc_L, fanart, fanart_, fanart_L, count, invalid__, duplicates__, i, i_='i')
					
				elif playlistid_ != "":
					url2 = 'https://www.googleapis.com/youtube/v3/playlistItems?playlistId='+playlistid_+'&key='+api_youtube_featherence+'&part=snippet&maxResults=20&pageToken='
					link2 = OPEN_URL(url2)
					prms2 = json.loads(link2)
					totalResults2 = int(prms2['pageInfo'][u'totalResults']) #if bigger than pagesize needs to add more result
					totalpagesN = (totalResults2 / pagesize) + 1
					
					text = "url2" + space2 + str(url2) + newline + \
					"link2" + space2 + str(link2) + newline + \
					"prms2" + space2 + str(prms2) + newline + \
					"totalResults2" + space2 + str(totalResults2)
					printlog(title='apimaster_test3', printpoint=printpoint, text=text, level=0, option="")
					
					
					i2 = 0
					while i2 < pagesize and i2 < totalResults2 and i2 < 20 and not "8" in printpoint and ((count + count_) < pagesize) and not xbmc.abortRequested:
						id_ = "" ; finalurl_ = ""
						title_ = "" ; thumb_ = "" ; desc_ = "" ; fanart_ = ""
						try: id_ = str(prms2['items'][i2][u'snippet'][u'resourceId'][u'videoId']) #Video ID (Playlist)
						except Exception, TypeError:
							extra = extra + newline + 'TypeError' + space2 + str(TypeError)
						if id_ != "":
							finalurl_ = "plugin://plugin.video.youtube/play/?video_id="+id_+"&hd=1"
							title_ = str(prms2['items'][i2][u'snippet'][u'title'].encode('utf-8'))
							try:
								thumb_ = str(prms2['items'][i2][u'snippet'][u'thumbnails'][u'default'][u'url'])
								fanart_ = str(prms['items'][i2][u'snippet'][u'thumbnails'][u'high'][u'url'])
							except Exception, TypeError: extra = extra + newline + 'thumb TypeError: ' + str(TypeError) + space + 'i2' + space2 + str(i2) + space + 'id' + space2 + str(id_)
							desc_ = str(prms2['items'][i2][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
							
							id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L, count, invalid__, duplicates__ = apimaster2(playlist, id_, id_L, finalurl_, playlist_L, title_, title_L, title2, thumb_, thumb_L, desc_, desc_L, fanart, fanart_, fanart_L, count, invalid__, duplicates__, i2, i_='i2')
						
						#print 'i2' + space2 + str(i2) + space + 'id' + space2 + str(id)
						i2 += 1
				
				elif id2_ != "":
					id_ = id2_
					finalurl_ = 'plugin://plugin.video.dailymotion_com/?url='+id_+'&mode=playVideo'
					if '&dailymotion_id=' in x: #if onlydata == True:
						title_ = to_utf8(prms[u'title'])
						try: thumb_ = str(prms[u'thumbnail_large_url'])
						except Exception, TypeError: pass
						try: desc_ = str(prms[u'description']).encode('utf-8')
						except Exception, TypeError: pass
						try: fanart_ = str(prms[u'thumbnail_large_url'])
						except Exception, TypeError: pass
					elif '&dailymotion_pl=' in x:
						title_ = str(prms[u'list'][i][u'title'].encode('utf-8'))
						thumb_ = str(prms[u'list'][i][u'thumbnail_large_url'])
						desc_ = str(prms[u'list'][i][u'description'].encode('utf-8'))
						fanart_ = str(prms[u'list'][i][u'thumbnail_large_url'])
					
						
					id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L, count, invalid__, duplicates__ = apimaster2(playlist, id_, id_L, finalurl_, playlist_L, title_, title_L, title2, thumb_, thumb_L, desc_, desc_L, fanart, fanart_, fanart_L, count, invalid__, duplicates__, i, i_='i')
			
			#except Exception, TypeError:
				#except__ = except__ + newline + "i" + space2 + str(i) + space + "id" + space2 + str(id)
				#if not 'list index out of range' in TypeError: extra = extra + newline + "i" + space2 + str(i) + space + "TypeError" + space2 + str(TypeError)
				#else: printpoint = printpoint + "8"
				
			
			i += 1
			if "&custom_se=" in x2 and count > 0 and playlist_L != []: printpoint = printpoint + "8"
			elif onlydata == True and count > 0 and playlist_L != []: printpoint = printpoint + "8"
		
	#numOfItems2 = len(playlist_L)
	numOfItems2 = count
	#numOfItems2 = int(len(playlist_L)) / 2 #TEST THIS NEW !
	#numOfItems2 = totalResults - invalid_ - duplicates_ - except_
	#if numOfItems2 > pagesize: numOfItems2 = 40
	totalpages = (numOfItems2 / pagesize) + 1
	nextpage = page + 1
	
	if onlydata == True and not '9' in printpoint:
		if id_L == []:
			pass
			#id_L.append(id_)
		if playlist_L == []:
			pass
			#playlist_L.append(finalurl)
		if title_L == []:
			if title == None: title = ""
			if 'c' in printpoint: title_L.append(title + space + title2)
			else: title_L.append(title)
		if thumb_L == []:
			thumb_L.append(str(thumb))
		if desc_L == []:
			if desc == None: desc = ""
			desc_L.append(str(desc))
		if fanart_L == []:
			if fanart == None: fanart = ""
			fanart_L.append(str(fanart))
			
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if duplicates__ != "": extra = "duplicates__" + space2 + str(duplicates__) + "(" + str(len(duplicates__)) + ")" + newline + extra
	if invalid__ != "": extra = "invalid__" + space2 + str(invalid__) + "(" + str(len(invalid__)) + ")" + newline + extra
	if except__ != "": extra = "except__" + space2 + str(except__) + "(" + str(len(except__)) + ")" + newline + extra
	if playlist != []: extra = "playlist" + space2 + str(playlist) + newline + extra
	
	#'link' + space2 + str(link) + newline + \
	text = "i" + space2 + str(i) + space + "totalResults" + space2 + str(totalResults) + space + "numOfItems2" + space2 + str(numOfItems2) + newline + \
	'onlydata' + space2 + str(onlydata) + newline + \
	"x" + space2 + str(x) + newline + \
	'url' + space2 + str(url) + newline + \
	'prms' + space2 + str(prms) + newline + \
	'finalurl_' + space2 + str(finalurl_) + newline + \
	'id_L' + space2 + str(id_L) + newline + \
	'title' + space2 + str(title) + space + 'title2' + space2 + str(title2) + space + 'title_L' + space2 + str(title_L) + newline + \
	'thumb' + space2 + str(thumb) + space + 'thumb_L' + space2 + str(thumb_L) + newline + \
	'desc' + space2 + str(desc) + space + 'desc_L' + space2 + str(desc_L) + newline + \
	'fanart' + space2 + str(fanart) + space + 'fanart_L' + space2 + str(fanart_L) + newline + \
	"page" + space2 + str(page) + " / " + str(totalpages) + space + "pagesize" + space2 + str(pagesize) + newline + \
	'count' + space2 + str(count) + space + 'count_' + space2 + str(count_) + newline + \
	"playlist" + space2 + str(len(playlist)) + space + str(playlist) + newline + \
	"playlist_L" + space2 + str(len(playlist_L)) + space + str(playlist_L) + newline + \
	"extra" + space2 + str(extra)
	printlog(title='apimaster_id', printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''
	
	if '9' in printpoint:
		return "", [], [], [], [], [], []
	else:
		return finalurl_, id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L

def apimaster2(playlist, id_, id_L, finalurl_, playlist_L, title_, title_L, title2, thumb_, thumb_L, desc_, desc_L, fanart, fanart_, fanart_L, count, invalid__, duplicates__, i, i_='i'):
	if not finalurl_ in playlist and not "Deleted video" in title_ and not "Private video" in title_ and finalurl_ != "":
		#if onlydata == True:
		if title2 != "":
			title_ = title_ + space + title2
		id_L.append(id_)
		playlist_L.append(finalurl_)
		title_L.append(title_)
		if thumb_L != "": thumb_L.append(thumb_)
		if desc_ != "": desc_L.append(desc_)
		if fanart_ != "": fanart_L.append(fanart_)
		
		count += 1
	else:
		if "Deleted video" in title_ or "Private video" in title_:
			invalid__ = invalid__ + newline + i_ + space2 + str(i) + space + "id_" + space2 + str(id_)
		elif finalurl_ in playlist:
			duplicates__ = duplicates__ + newline + i_ + space2 + str(i) + space + "id_" + space2 + str(id_)
	
	text = "i" + space2 + str(i) + space + "count" + space2 + str(count) + newline + \
	'title_' + space2 + str(title_) + newline + \
	'fanart_' + space2 + str(fanart_) + newline + \
	'desc_' + space2 + str(desc_) + newline + \
	"id_" + space2 + str(id_)

	printlog(title='apimaster2', printpoint="", text=text, level=0, option="")
	
	return id_L, playlist_L, title_L, thumb_L, desc_L, fanart_L, count, invalid__, duplicates__

def getView(x, viewtype, containerfolderpath, containerfolderpath2):
	name = 'getView' ; printpoint = "" ; x = "" ; z = "" ; s = ""
	
	mainmenu = regex_from_to(containerfolderpath, 'plugin://' + addonID, '/', excluding=False)
	submenu = regex_from_to(containerfolderpath2, 'plugin://' + addonID, '/', excluding=False)
	if containerfolderpath2.replace(mainmenu,"") == "": x = General_AutoView0 ; printpoint = printpoint + "2" ; z = addonString_servicefeatherence(32151).encode('utf-8') ; s = 'General_AutoView0'
	elif containerfolderpath.replace(submenu,"") == "": x = General_AutoView1 ; printpoint = printpoint + "3" ; z = addonString_servicefeatherence(32153).encode('utf-8') ; s = 'General_AutoView1'
	else: x = General_AutoView9 ; printpoint = printpoint + "4" ; z = addonString_servicefeatherence(32152).encode('utf-8') ; s = 'General_AutoView9'
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "viewtype" + space2 + str(viewtype) + newline + \
	"containerfolderpath" + space2 + str(containerfolderpath) + newline + \
	"containerfolderpath2" + space2 + str(containerfolderpath2) + newline + \
	"x" + space2 + str(x) + newline + \
	"z" + space2 + str(z) + newline + \
	"mainmenu" + space2 + str(mainmenu) + newline + \
	"submenu" + space2 + str(submenu) + newline + \
	"General_AutoView0" + space2 + str(General_AutoView0) + newline + \
	"General_AutoView1" + space2 + str(General_AutoView1) + newline + \
	"General_AutoView9" + space2 + str(General_AutoView9)
	
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
	return x, z, s
	
def setView(viewtype, containerfolderpath, containerfolderpath2):
	'''set content type so library shows more views and info'''
	name = 'setView' ; printpoint = ""; x = "" ; z = ""
	
	if 1 + 1 == 3:
		printpoint = printpoint + "1"
		xbmcplugin.setContent(int(sys.argv[1]), content)
	
	x, z, s = getView(x, viewtype, containerfolderpath, containerfolderpath2)
	
	if x != "":
		printpoint = printpoint + "7"
		xbmc.executebuiltin("Container.SetViewMode(%s)" % str(x) )
		'''---------------------------'''
	else: printpoint = printpoint + "9"

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "viewtype" + space2 + str(viewtype) + newline + \
	"x" + space2 + str(x) + newline + \
	"z" + space2 + str(z)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''
			
def TVMode_check(admin, url, playlists):
	printpoint = ""
	returned = ""
	if General_TVModeDialog == "true":
		printpoint = printpoint + "1"
		printpoint = printpoint + "3"
		countl = 0
		for space in playlists:
			countl += 1
		countlS = str(countl)
		if playlists==[] or countl > 1:  #no playlists on  youtube channel
			'''------------------------------
			---PLAYLIST->-1------------------
			------------------------------'''
			printpoint = printpoint + "5"
			returned = dialogyesno(addonString_servicefeatherence(32412).encode('utf-8'), addonString_servicefeatherence(32413).encode('utf-8'))
			if returned == "ok": returned = TvMode(url)
			'''---------------------------'''
		else: printpoint = printpoint + "8"
				
	printlog(title='TVMode_check', printpoint=printpoint, text="", level=0, option="")
	'''---------------------------'''
	return returned

def TvMode2(addonID, mode, name, url, iconimage, desc, num, viewtype, fanart):
	returned = "" ; printpoint = ""
	scriptfeatherenceservice_random = xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random)')
	if url == "None":
		'''Empty button'''
		notification("no valid URL founds!", "...", "", 2000)
	else:
		if not '&youtube_' in url and not '&dailymotion_' in url and not '&custom4=' in url: pass
		elif General_TVModeDialog == "true" or mode == 2 or scriptfeatherenceservice_random != "":
			if General_TVModeShuffle == "true": extra = addonString_servicefeatherence(32413).encode('utf-8')
			else: extra = ""
			if scriptfeatherenceservice_random != "": returned = 'ok'
			else:
				#if (xbmc.getCondVisibility('Window.Previous(VideoFullScreen.xml)') or xbmc.getCondVisibility('Window.Previous(DialogBusy.xml)') or xbmc.getCondVisibility('Window.Previous(VideoOSD.xml)')) and xbmc.getCondVisibility('Player.HasVideo'):
				if General_TVModeForce == "true": returned = 'ok'
				else:
					returned = dialogyesno(addonString_servicefeatherence(32412).encode('utf-8'), extra)
			
		if returned == 'ok': mode = 5
		else: mode = 6
		
		mode = MultiVideos(addonID, mode, name, url, iconimage, desc, num, viewtype, fanart)
		
		text = 'General_TVModeShuffle' + space2 + str(General_TVModeShuffle) + newline + \
		'scriptfeatherenceservice_random' + space2 + str(scriptfeatherenceservice_random) + newline + \
		'General_TVModeDialog' + space2 + str(General_TVModeDialog) + newline + \
		'url' + space2 + str(url)
		printlog(title='TvMode2', printpoint=printpoint, text=text, level=1, option="")
		
		return mode

def getAddonInfo(addon):
	name = 'getAddonInfo' ; printpoint = ""
	thumb = "" ; fanart = "" ; summary = "" ; description = ""
	
	thumb = os.path.join(addons_path, addon, 'icon.png')
	fanart = os.path.join(addons_path, addon, 'fanart.jpg')
	addoninfo = os.path.join(addons_path, addon, 'addon.xml')
	addoninfo_ = read_from_file(addoninfo, silent=True, lines=False, retry=False, printpoint="", addlines="")
	systemlanguage = xbmc.getInfoLabel('System.Language')
	systemlanguage_ = systemlanguage[:2].lower()
	
	if addoninfo_ != "":
		i = 0
		for i in range(0,3):
			if i == 0: summary = regex_from_to(addoninfo_, '<summary lang="'+systemlanguage_+'">', '</summary>', excluding=True)
			elif i == 1: summary = regex_from_to(addoninfo_, '<summary>', '</summary>', excluding=True)
			elif i == 2: summary = regex_from_to(addoninfo_, '<summary lang="en">', '</summary>', excluding=True)
			if summary != "": break
		
		i = 0
		for i in range(0,3):
			if i == 0: description = regex_from_to(addoninfo_, '<description lang="'+systemlanguage_+'">', '</description>', excluding=True)
			elif i == 1: description = regex_from_to(addoninfo_, '<description>', '</description>', excluding=True)
			elif i == 2: description = regex_from_to(addoninfo_, '<description lang="en">', '</description>', excluding=True)
			if description != "": break
	
	text = 'systemlanguage' + space2 + str(systemlanguage) + space + 'systemlanguage[:2]' + space2 + str(systemlanguage_) + newline + \
	'thumb' + space2 + str(thumb) + newline + \
	'fanart' + space2 + str(fanart) + newline + \
	'summary' + space2 + str(summary) + newline + \
	'description' + space2 + str(description)
	
	try: summary = summary.encode('utf-8')
	except: pass
	try: description = description.encode('utf-8')
	except: pass
	plot = '[COLOR=yellow]'+summary+'[/COLOR]'+'[CR][CR]'+description
	
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	return thumb, fanart, summary, description, plot
	
def update_view(url, num, viewtype, ok=True, installaddon=True):
	printpoint = "" ; num_ = num
	if installaddon == True:
		printpoint = printpoint + '1'
		if 'plugin.' in num or 'plugin://plugin.' in url:
			printpoint = printpoint + 'a'
			if not 'plugin.' in num:
				printpoint = printpoint + 'b'
				num_ = find_string(url, "plugin://", '/')
				if num_ == "":
					printpoint = printpoint + 'c'
					num_ = url.replace('plugin://',"")
				else: printpoint = printpoint + 'd'
			else:
				printpoint = printpoint + 'e'
				num_ = num
				
			num_ = num_.replace("plugin://","")
			num_ = num_.replace("/","")
				
			if not xbmc.getCondVisibility('System.HasAddon('+ num_ +')') or not os.path.exists(os.path.join(addons_path, num_)) and num_ != "" and num_ != None:
				printpoint = printpoint + 'f'
				notification_common("24")
				#notification(num_,"","",4000)
				#installaddon(num_, update=True)
				xbmc.sleep(2000)
	
	if '&activatewindow=' in url:
		printpoint = printpoint + '2'
	if '&' in url and '=' in url:
		printpoint = printpoint + '3'
		url_ = find_string(url, "&", '=')
		list = ['&youtube_pl=', '&youtube_id=', '&youtube_ch=', '&youtube_se=', '&activatewindow=']
		if url_ in list:
			printpoint = printpoint + '4'
			url = url.replace(url_,"",1)
	
	url = url.replace('[',"",1)
	url = url.replace(']',"",1)
	url = url.replace("'","",1)
	url = url.replace("'","",1)
	
	if '2' in printpoint:
		#xbmc.sleep(500)
		xbmc.executebuiltin('ActivateWindow(10025,%s,return)' % url )
		#xbmc.executebuiltin('XBMC.Container.Update(%s)' % url )
	elif 'ActivateWindow(' in url:
		printpoint = printpoint + '5'
		xbmc.executebuiltin(url)
	else:
		printpoint = printpoint + '7'
		xbmc.executebuiltin('XBMC.Container.Update(%s)' % url )
		
	text = "url" + space2 + str(url) + space + 'viewtype' + space2 + str(viewtype) + newline + \
	'num_' + space2 + str(num_)
	printlog(title='update_view', printpoint=printpoint, text=text, level=0, option="")
	
	return ok

def play_view(url, num, viewtype):
	if 'plugin.' in num:
		if not xbmc.getCondVisibility('System.HasAddon('+ num +')') or not os.path.exists(os.path.join(addons_path, num)):
			notification_common("24")
			installaddon(num, update=True)
			xbmc.sleep(2000)
	ok = True
	xbmc.executebuiltin('PlayMedia(%s)' % url )
	text = "url" + space2 + str(url) + space + 'viewtype' + space2 + str(viewtype)
	printlog(title='update_view', printpoint="", text=text, level=0, option="")
	return ok	

def urlcheck(url, ping=False, timeout=1):
	import urllib2
	name = "urlcheck" ; printpoint = "" ; returned = "" ; extra = "" ; TypeError = "" ; response_ = ""
	
	if url == None or url == "":
		url = ""
		printpoint = printpoint + '9'
	else:
		try:
			#urllib2.urlopen(url)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request, timeout=timeout)
			response_ = response
			#content = response.read()
			#f = urllib2.urlopen(url)
			#f.fp._sock.recv=None # hacky avoidance
			response.close()
			del response
			printpoint = printpoint + "7"
			
		except urllib2.HTTPError, e: 
			extra = extra + newline + str(e.code) + space + str(e)
			printpoint = printpoint + "8"
		except urllib2.URLError, e:
			extra = extra + newline + str(e.args) + space + str(e)
			printpoint = printpoint + "9"
		except Exception, TypeError:
			printpoint = printpoint + "9"
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			if 'The read operation timed out' in TypeError: returned = 'timeout'
				
		if not "7" in printpoint:				
			if 'Forbidden' in extra:
				printpoint = printpoint + '7'
				
	if "UKY3scPIMd8" in url: printpoint = printpoint + "6"
	elif "7" in printpoint: returned = "ok" # or 'Forbidden' in extra
	else: returned = 'error'
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "url" + space2 + url + space + "ping" + space2 + str(ping) + space + 'returned' + space2 + str(returned) + newline + \
	'response_' + space2 + str(response_) + extra
	printlog(title='urlcheck', printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''
	return returned
	
def YOUList2(name, url, iconimage, desc, num, viewtype):
	returned = "" ; printpoint = "" ; i = 0 ; urlL = ['channel', 'user'] #, 'show'
	url = CleanString2(url)
	if '&youtube_ch=' in url or (not '&' in url and not '=' in url):
		printpoint = printpoint + '1'
		if '&youtube_ch=' in url:
			printpoint = printpoint + '2'
			url = url.replace("&youtube_ch=","")
		
		if "/playlists" in url:
			printpoint = printpoint + '3'
			url = url.replace("/playlists","")		
			
		default = 'http://www.youtube.com/'
		default2 = 'plugin://plugin.video.youtube/'
		
		for x in urlL:
			returned = urlcheck(default + urlL[i] + '/' + url + '/')
			if returned == "ok": break
			else:
				i += 1

		if returned == 'ok':
			printpoint = printpoint + '7'
			update_view(default2 + urlL[i] + '/' + url + '/', num, viewtype, ok=False)
	else:
		printpoint = printpoint + '9'
	text = "name" + space2 + str(name) + newline + \
	"url" + space2 + url + newline + \
	"i" + space2 + str(i) + space + "returned" + space2 + str(returned)
	printlog(title='YOUList2', printpoint=printpoint, text=text, level=0, option="")

def setCustomFanart(addon, mode, admin, name, printpoint):
	x = "" ; printpoint = ""
	if not '.' in addon: addon = ""
	try: test = int(mode) + 1
	except: mode = ""
	
	if mode != "" and addon != "":
		'''Add-Fanart'''
		name = localize(20441)
		x = 'background'
		nolabel=localize(20438)
		yeslabel=localize(20441)
	
	if x != "":
		returned = dialogyesno(str(name), addonString_servicefeatherence(32423).encode('utf-8'), nolabel=nolabel, yeslabel=yeslabel)
		if returned == 'ok':
			returned2, value = getRandom(0, min=0, max=100, percent=40)
			if returned2 == 'ok': notification('O_o???','Copy & Paste an image URL','',4000)
			'''remote'''
			value = dialogkeyboard("", yeslabel, 0, "1", "", "")
			if value != "skip":
				from shared_modules3 import urlcheck
				returned2 = urlcheck(value, ping=False)
				if returned2 != "ok":
					notification(localize(2102, s=[addonString_servicefeatherence(32436).encode('utf-8')]), addonString_servicefeatherence(32801).encode('utf-8') + space + '..', "", 2000)
					header = localize(2102, s=[addonString_servicefeatherence(32436).encode('utf-8')]) #"URL Error"
					message = addonString_servicefeatherence(32802).encode('utf-8') + space2 + newline + '[B]' + str(value) + '[/B]'
					diaogtextviewer(header,message)
				else:
					setsetting_custom1(addon, 'Fanart_Custom' + str(mode),str(value))
		else:
			'''local'''
			value = setPath(type=1,mask='pic', folderpath="")
			setsetting_custom1(addon, 'Fanart_Custom' + str(mode),str(value))
	
	text = 'addon' + space2 + str(addon) + space + 'mode' + space2 + str(mode) + space + 'x' + space2 + str(x) + newline
	printlog(title='setCustomFanart', printpoint=printpoint, text=text, level=0, option="")
	
def setaddonFanart(fanart, Fanart_Enable, Fanart_EnableCustom):
	returned = "" ; printpoint = "" ; TypeError = "" ; extra = ""
	try:
		Fanart_Enable = getsetting('Fanart_Enable')
		Fanart_EnableCustom = getsetting('Fanart_EnableCustom')
	except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
	
	if Fanart_Enable == "true" and extra == "":
		printpoint = printpoint + "1"
		if fanart != "":
			printpoint = printpoint + "2"
			try:
				if os.path.exists(fanart):
					printpoint = printpoint + "3"
					returned = fanart
				elif "http://" in fanart or "www." in fanart or "https://" in fanart:
					printpoint = printpoint + "4"
					returned = fanart
				else: pass
			except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
	
		else: printpoint = printpoint + "8"
	else: printpoint = printpoint + "9"
	
	text =  "Fanart_Enable" + space2 + str(Fanart_Enable) + space + "Fanart_EnableCustom" + space2 + str(Fanart_EnableCustom) + newline + \
	"fanart" + space2 + str(fanart) + extra
	printlog(title='setaddonFanart', printpoint=printpoint, text=text, level=0, option="")
	return returned

def getAddonFanart(category, custom="", default="", urlcheck_=False):
	#admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	#admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	#admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)')
	returned = "" ; category_path = "" ; printpoint = "" ; extra = "" ; 
	
	if custom != "":
		valid = ""
		if urlcheck_ == True: 
			valid = urlcheck(custom, ping=False, timeout=1)
		
		if 'ok' in valid or urlcheck_ != True:
			printpoint = printpoint + "7"
			returned = custom
			
	if returned == "" and not '7' in printpoint:
		printpoint = printpoint + '1'
		if Fanart_EnableCustom != "true" and default == "":
			returned = addonFanart
			printpoint = printpoint + "8"
		elif category == 100: category_path = Fanart_Custom100
		elif category == 101: category_path = Fanart_Custom101
		elif category == 102: category_path = Fanart_Custom102
		elif category == 103: category_path = Fanart_Custom103
		elif category == 104: category_path = Fanart_Custom104
		elif category == 105: category_path = Fanart_Custom105
		elif category == 106: category_path = Fanart_Custom106
		elif category == 107: category_path = Fanart_Custom107
		elif category == 108: category_path = Fanart_Custom108
		elif category == 109: category_path = Fanart_Custom109
		elif category == 110: category_path = Fanart_Custom110
		elif category == 111: category_path = Fanart_Custom111
		elif category == 112: category_path = Fanart_Custom112
		elif category == 113: category_path = Fanart_Custom113
		elif category == 114: category_path = Fanart_Custom114
		elif category == 115: category_path = Fanart_Custom115
		elif category == 116: category_path = Fanart_Custom116
		elif category == 117: category_path = Fanart_Custom117
		elif category == 118: category_path = Fanart_Custom118
		elif category == 119: category_path = Fanart_Custom119
		
		elif category == 10000: category_path = Fanart_Custom10000
		elif category == 10001: category_path = Fanart_Custom10001
		elif category == 10002: category_path = Fanart_Custom10002
		elif category == 10003: category_path = Fanart_Custom10003
		elif category == 10004: category_path = Fanart_Custom10004
		elif category == 10005: category_path = Fanart_Custom10005
		elif category == 10006: category_path = Fanart_Custom10006
		elif category == 10007: category_path = Fanart_Custom10007
		elif category == 10008: category_path = Fanart_Custom10008
		elif category == 10009: category_path = Fanart_Custom10009
		
		elif category == 10100: category_path = Fanart_Custom10100
		elif category == 10101: category_path = Fanart_Custom10101
		elif category == 10102: category_path = Fanart_Custom10102
		elif category == 10103: category_path = Fanart_Custom10103
		elif category == 10104: category_path = Fanart_Custom10104
		elif category == 10105: category_path = Fanart_Custom10105
		elif category == 10106: category_path = Fanart_Custom10106
		elif category == 10107: category_path = Fanart_Custom10107
		elif category == 10108: category_path = Fanart_Custom10108
		elif category == 10109: category_path = Fanart_Custom10109
		elif category == 10200: category_path = Fanart_Custom10200
		elif category == 10201: category_path = Fanart_Custom10201
		elif category == 10202: category_path = Fanart_Custom10202
		elif category == 10203: category_path = Fanart_Custom10203
		elif category == 10204: category_path = Fanart_Custom10204
		elif category == 10205: category_path = Fanart_Custom10205
		elif category == 10206: category_path = Fanart_Custom10206
		elif category == 10207: category_path = Fanart_Custom10207
		elif category == 10208: category_path = Fanart_Custom10208
		elif category == 10209: category_path = Fanart_Custom10209
		
		elif category == 11100: category_path = Fanart_Custom11100
		elif category == 11101: category_path = Fanart_Custom11101
		elif category == 11102: category_path = Fanart_Custom11102
		elif category == 11103: category_path = Fanart_Custom11103
		elif category == 11104: category_path = Fanart_Custom11104
		elif category == 11105: category_path = Fanart_Custom11105
		elif category == 11106: category_path = Fanart_Custom11106
		elif category == 11107: category_path = Fanart_Custom11107
		elif category == 11108: category_path = Fanart_Custom11108
		elif category == 11109: category_path = Fanart_Custom11109
		
		else:
			try:
				if "Custom_Playlist" in category:
					if category == "Custom_Playlist1": category_path = Custom_Playlist1_Fanart
					elif category == "Custom_Playlist2": category_path = Custom_Playlist2_Fanart
					elif category == "Custom_Playlist3": category_path = Custom_Playlist3_Fanart
					elif category == "Custom_Playlist4": category_path = Custom_Playlist4_Fanart
					elif category == "Custom_Playlist5": category_path = Custom_Playlist5_Fanart
					elif category == "Custom_Playlist6": category_path = Custom_Playlist6_Fanart
					elif category == "Custom_Playlist7": category_path = Custom_Playlist7_Fanart
					elif category == "Custom_Playlist8": category_path = Custom_Playlist8_Fanart
					elif category == "Custom_Playlist9": category_path = Custom_Playlist9_Fanart
					elif category == "Custom_Playlist10": category_path = Custom_Playlist10_Fanart
					else: printpoint = printpoint + "8"
			except Exception, TypeError:
				extra = extra + newline + "TypeError" + space2 + str(TypeError)
				printpoint = printpoint + "8"
	
	
		if category_path != "":
			if "http://" in category_path or "www." in category_path:
				printpoint = printpoint + "7a"
				returned = category_path
				#valid = urlcheck(value, ping=False)
			else:
				try:
					category_path = os.path.join(xbmc.translatePath(category_path).decode("utf-8"))
					category_path = category_path.encode('utf-8')
				except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError).encode('utf-8')
				if os.path.exists(category_path):
					printpoint = printpoint + "7b"
					
					if 1 + 1 == 3:
						category_path = os.path.join(xbmc.translatePath(category_path).decode("utf-8"))
						try: category_path = category_path.encode('utf-8')
						except: pass
					
				else:
					setsetting('Fanart_Custom'+str(category),"")
					printpoint = printpoint + "9d"
		
		elif default != "" and not '7' in printpoint: #default != 'getAPIdata'
			printpoint = printpoint + '5'
			returned, returned2 = TranslatePath(default, filename=True, urlcheck_=True, force=True)
			if default == 'getAPIdata':
				printpoint = printpoint + 'A'
				returned = default
			elif returned == "": printpoint = printpoint + "9"
		else:
			printpoint = printpoint + "9"
			
	if "9" in printpoint or "8" in printpoint:
		try:
			if os.path.exists(addonFanart): returned = addonFanart
		except Exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			returned = ""
	
	elif "7" in printpoint:
		if default == "" and custom == "" or '7b' in printpoint: returned = category_path
	
	text = "category" + space2 + str(category) + newline + \
	"custom" + space2 + str(custom) + newline + \
	"default" + space2 + str(default) + newline + \
	"returned" + space2 + str(returned) + newline + \
	"category_path" + space2 + str(category_path) + extra
	printlog(title='getAddonFanart', printpoint=printpoint, text=text, level=0, option="")
	return returned

def checkAddon_Update(admin, Addon_Update, Addon_Version, addonVersion, Addon_UpdateDate, Addon_UpdateLog, Addon_ShowLog, Addon_ShowLog2, VerReset=""):
	TypeError = "" ; extra = "" ; name = 'checkAddon_Update' ; printpoint = ""
	
	if Addon_Update != "true" or (Addon_Update == "true" and Addon_Version == addonVersion):
		'''------------------------------
		---Addon_Update-(NEW-ONLY)--------
		------------------------------'''
		Addon_Update = setAddon_Update(admin, addonVersion, Addon_Version, Addon_Update)
		'''---------------------------'''
	
	if Addon_Update == "true":
		'''------------------------------
		---setAddon_Version---------------
		------------------------------'''
		Addon_Version = setAddon_Version(admin, addonVersion, Addon_Version, VerReset)
		'''---------------------------'''
		
	if Addon_Update == "true" or Addon_UpdateDate == "":
		'''------------------------------
		---setAddon_UpdateDate-(NEW-ONLY)-
		------------------------------'''
		Addon_UpdateDate = setAddon_UpdateDate(admin, addonVersion, Addon_Version, Addon_Update, Addon_UpdateDate)
		'''---------------------------'''
	
	if Addon_Version == addonVersion and Addon_UpdateLog == "true" and Addon_UpdateDate != "":
		'''------------------------------
		---Addon_UpdateLog----------------
		------------------------------'''
		#dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOk.xml)')
		#dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
		#dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
		#dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
		#dialogtextviewerW = xbmc.getCondVisibility('Window.IsVisible(DialogTextViewer.xml)')
		#startupW = xbmc.getCondVisibility('Window.IsVisible(Startup.xml)')
		#custom1191W = xbmc.getCondVisibility('Window.IsVisible(Custom1191.xml)')
		#if not dialogokW and not dialogselectW and not dialogprogressW and not dialogbusyW and not startupW and not dialogtextviewerW and not custom1191W:
		#if datenowS != "":
		setAddon_UpdateLog(admin, Addon_Version, Addon_UpdateDate, Addon_ShowLog, Addon_ShowLog2, datenowS)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "checkAddon_Update" + space2 + "Addon_Update" + space2 + Addon_Update + space + "Addon_Version" + space2 + Addon_Version + space + "addonVersion" + space2 + addonVersion + space + "Addon_UpdateDate" + space2 + Addon_UpdateDate + space + "Addon_UpdateLog" + space2 + Addon_UpdateLog
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''
				
def setAddon_Update(admin, addonVersion, Addon_Version, Addon_Update):
	'''Compare addon version to check if it's been updated'''
	name = 'setAddon_Update' ; printpoint = ""
	Addon_Update2 = Addon_Update
	if Addon_Version != addonVersion and Addon_Update == "false":
		Addon_Update2 = "true"
		setsetting('Addon_UpdateLog',"true")
		'''---------------------------'''
	else:
		Addon_Update2 = "false"
		'''---------------------------'''
		
	if Addon_Update != Addon_Update2: setsetting('Addon_Update',Addon_Update2)
	'''---------------------------'''
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "setAddon_Update" + space2 + Addon_Update + " - " + Addon_Update2
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''	
	return Addon_Update2

def setAddon_Version(admin, addonVersion, Addon_Version, VerReset=""):
	'''set the new version in settings.xml'''
	name = 'setAddon_Version' ; printpoint = ""
	Addon_Version2 = Addon_Version
	'''---------------------------'''
	if Addon_Version != addonVersion:
		Addon_Version2 = addonVersion
		setsetting('Addon_Version',Addon_Version2)
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "setAddon_Version" + space2 + Addon_Version + " - " + Addon_Version2 + space + 'VerReset' + space2 + str(VerReset)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''
	return Addon_Version2
		
def setAddon_UpdateDate(admin, addonVersion, Addon_Version, Addon_Update, Addon_UpdateDate):
	'''set the current update date'''
	from variables import datenowS
	name = 'setAddon_UpdateDate' ; printpoint = ""
	Addon_UpdateDate2 = Addon_UpdateDate
	'''---------------------------'''
	if Addon_UpdateDate != datenowS:
		Addon_UpdateDate2 = datenowS
		setsetting('Addon_UpdateDate',Addon_UpdateDate2)
		'''---------------------------'''

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "setAddon_UpdateDate" + space2 + Addon_UpdateDate + " - " + Addon_UpdateDate2
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''
	return Addon_UpdateDate2
	
def setAddon_UpdateLog(admin, Addon_Version, Addon_UpdateDate, Addon_ShowLog, Addon_ShowLog2, datenowS):	
	'''show a changelog if that option enabled'''
	name = 'setAddon_UpdateLog' ; printpoint = "" ; TypeError = "" ; extra = ""
	from variables import addonID, addonName2
	number2S = ""
	datenowD = stringtodate(datenowS,'%Y-%m-%d')
	datedifferenceD = stringtodate(Addon_UpdateDate,'%Y-%m-%d')
	datedifferenceS = str(datedifferenceD)
	
	if Addon_ShowLog == "true":
		if "error" in [datenowD, datedifferenceD]: printpoint = printpoint + "9"
		try:
			number2 = datenowD - datedifferenceD
			number2S = str(number2)
			printpoint = printpoint + "2"
			'''---------------------------'''
		except Exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			printpoint = printpoint + "9"
			'''---------------------------'''
		try:
			Addon_ShowLog2 = int(Addon_ShowLog2)
			Addon_ShowLog2 = str(Addon_ShowLog2)
			printpoint = printpoint + "3"
			'''---------------------------'''
		except Exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			Addon_ShowLog2 = "1"
			printpoint = printpoint + "4"
			'''---------------------------'''
		if not "9" in printpoint:
			printpoint = printpoint + "5"
			if "day," in number2S: number2S = number2S.replace(" day, 0:00:00","",1)
			elif "days," in number2S: number2S = number2S.replace(" days, 0:00:00","",1)
			else: number2S = "0"
			number2N = int(number2S)
			'''---------------------------'''
			#header = '[COLOR=yellow]' + addonString(304).encode('utf-8') + " - " + addonVersion + '[/COLOR]'
			if number2N == 0: header = '[COLOR=yellow]' + localize(24065) + space + localize(33006) + space5 + Addon_Version + '[/COLOR]'
			elif number2N == 1: header = '[COLOR=green]' + localize(24065) + space + addonString_servicefeatherence(32410).encode('utf-8') + space5 + Addon_Version + '[/COLOR]'
			elif number2N <= 7: header = '[COLOR=purple]' + localize(24065) + space + addonString_servicefeatherence(32411).encode('utf-8') + space5 + Addon_Version + '[/COLOR]'
			else: header = ""
			'''---------------------------'''
			if number2N <= int(Addon_ShowLog2):
				printpoint = printpoint + "7"
				log = open(addonPath + "/" + 'changelog.txt', 'rb')
				message2 = log.read()
				log.close()
				message2S = str(message2)
				message3 = message2[0:8000]
				message3 = '"' + message3 + '"'
				message3S = str(message3)
				if header != "":
					w = TextViewer_Dialog('DialogTextViewer.xml', "", header=header, text=message2)
					w.doModal()
					'''---------------------------'''
			else: printpoint = printpoint + "8"

	try: setsetting_custom1(addonID, 'Addon_UpdateLog', "false")
	except: pass
		
	text = "Addon_UpdateDate" + space2 + str(Addon_UpdateDate) + newline + \
	"datenowS" + space2 + str(datenowS) + newline + \
	"number2S" + space2 + str(number2S) + newline + \
	"Addon_UpdateLog" + space2 + str(Addon_UpdateLog) + newline + \
	"Addon_ShowLog" + space2 + str(Addon_ShowLog) + newline + \
	"Addon_ShowLog2" + space2 + str(Addon_ShowLog2)
	'''---------------------------'''
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
def pluginend(admin):
	try: from modules import *
	except: pass
	try: from modulesp import *
	except: pass
	printpoint = "" ; TypeError = "" ; extra = ""
	
	'''------------------------------
	---params------------------------
	------------------------------'''
	params=get_params()
	url=None
	name=None
	mode=None
	iconimage=None
	desc=None
	num=None
	viewtype=None
	fanart=None
	#value=None
	'''---------------------------'''
	try: url=urllib.unquote_plus(params["url"])
	except: pass
	try: name=urllib.unquote_plus(params["name"])
	except: pass
	try: iconimage=urllib.unquote_plus(params["iconimage"])
	except: pass
	try: mode=int(params["mode"])
	except: pass
	try: desc=urllib.unquote_plus(params["desc"])
	except: pass
	
	try: num=urllib.unquote_plus(params["num"])
	except: pass
	try: viewtype=int(params["viewtype"])
	except: pass
	try: fanart=urllib.unquote_plus(params["fanart"])
	except: pass
	#try: value=urllib.unquote_plus(params["value"])
	#except: pass
	'''---------------------------'''

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	try: IconImageS = str(IconImage)
	except: IconImageS = "None"
	'''---------------------------'''
	text = "mode" + space2 + str(mode) + newline + \
	"url" + space2 + str(url) + newline + \
	"name" + space2 + str(name) + space + "IconImage" + space2 + IconImageS + newline + \
	"desc" + space2 + str(desc) + newline + \
	"viewtype" + space2 + str(viewtype) + space + "fanart" + space2 + str(fanart) + newline + \
	"params" + space2 + str(params)
	printlog(title='pluginend', printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''

	'''------------------------------
	---MODES-LIST--------------------
	------------------------------'''
	if mode == None or ((url == None or len(url)<1) and mode < 100) or 1 + 1 == 3:
		if addonID == 'plugin.video.featherence.kids':
			if General_Language == "":
				CATEGORIES200()
				xbmc.executebuiltin('AlarmClock(firstrun,RunScript(script.featherence.service,,?mode=32&value=40),00:01,silent)')
			else: CATEGORIES()
			
		
		else: CATEGORIES()
		
		systemlanguage = xbmc.getInfoLabel('System.Language')
		
		if 1 + 1 == 2:
			getsetting('Addon_Update')
			getsetting('Addon_Version')
			getsetting('Addon_UpdateDate')
			getsetting('Addon_UpdateLog')
			getsetting('Addon_ShowLog')
			getsetting('Addon_ShowLog2')
			
			VerReset = ""
			#if addonID == 'plugin.video.featherence.music' and Addon_Version == '0.0.17': VerReset = "true"
			checkAddon_Update(admin, Addon_Update, Addon_Version, addonVersion, Addon_UpdateDate, Addon_UpdateLog, Addon_ShowLog, Addon_ShowLog2, VerReset)
			if Addon_UpdateLog == "true" or 1 + 1 == 3:
				list = []
				list.append(addonString_servicefeatherence(32060).encode('utf-8')) #Would you like thanks us? Would love to hear you!
				list.append(addonString_servicefeatherence(32061).encode('utf-8')) #Do you want to contribute?
				list.append(addonString_servicefeatherence(32062).encode('utf-8')) #Have an idea for new addon?
				list.append(addonString_servicefeatherence(32063).encode('utf-8')) #Looking for support?
				list.append(addonString_servicefeatherence(32064).encode('utf-8')) #Having a question?
				returned, value = getRandom(0, min=0, max=len(list), percent=50)
				
				notification(list[int(value)],'www.featherence.com','',4000)
			
			if Addon_UpdateLog == "true":
				if addonID == 'plugin.video.featherence.kids':
					if 'Hebrew' in General_LanguageL:
						installaddonP('repository.xbmc-israel', update=True)
						#installaddonP('repository.kodil', update=True)
						installaddonP('repository.multidownrepo', update=True)
						installaddonP('repository.Jk$p', update=True)
				
					if 'English' in General_LanguageL:
						installaddonP('repository.metalkettle', update=True)
				
		#except Exception, TypeError:
			#extra = extra + newline + "TypeError" + space2 + str(TypeError)
			#printpoint = printpoint + "2"
			'''---------------------------'''
		
	#1-99 = COMMANDS
	elif mode == 1:
		getLists(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 2:
		mode = LocalSearch(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 3:
		YoutubeSearch(name, url, desc, num, viewtype)
	elif mode == 4:
		PlayVideos(name, mode, url, iconimage, desc, num, fanart)
	elif mode == 5:
		mode = MultiVideos(addonID, mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 6:
		mode = MultiVideos(addonID, mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 7:
		pass
	elif mode == 8:
		update_view(url, num, viewtype)
	elif mode == 9:
		YOUList2(name, url, iconimage, desc, num, viewtype)
	elif mode == 10:
		mode = 4
		PlayVideos(name, mode, url, iconimage, desc, num, fanart)
	elif mode == 11:
		mode = LocalSearch2(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 12:
		PlayVideos(name, mode, url, iconimage, desc, num, fanart)
	elif mode == 13:
		ListPlaylist2(name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 14:       
		pass
	elif mode == 15:
		pass
	elif mode == 16:       
		pass
	elif mode == 17:
		mode = TvMode2(addonID, mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 18:
		'''Custom Playlist'''
		mode = TvMode2(addonID, mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 20:
		AddCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 21:
		ManageCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 22:
		AdvancedCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 23:
		MoveCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 24:
		AddCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 25:
		RenameSubCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 30:
		CATEGORIES_SEARCH2(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 31:
		Search_Menu(mode, name, url, iconimage, desc, num, viewtype, fanart)
	
	elif mode == 40:
		listURLS(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 41:
		'''Play URL'''
		listURLS(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 42:
		listURL(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 44:
		'''Play URL'''
		playURL(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 50:
		'''Add View'''
		addView(viewtype)
	elif mode == 90:
		if General_Language != url and url != "":
			setsetting('General_Language',url)
			notification(addonString_servicefeatherence(32080).encode('utf-8'),str(url),'',2000)
			xbmc.sleep(500)
		CATEGORIES()
	elif mode == 100:
		CATEGORIES100(name, iconimage, desc, fanart)
	elif mode == 101:
		CATEGORIES101(name, iconimage, desc, fanart)
	elif mode == 102: 
		CATEGORIES102(name, iconimage, desc, fanart)
	elif mode == 103:       
		CATEGORIES103(name, iconimage, desc, fanart)
	elif mode == 104:       
		CATEGORIES104(name, iconimage, desc, fanart)
	elif mode == 105:    
		CATEGORIES105(name, iconimage, desc, fanart)
	elif mode == 106:       
		CATEGORIES106(name, iconimage, desc, fanart)
	elif mode == 107:       
		CATEGORIES107(name, iconimage, desc, fanart)
	elif mode == 108:       
		CATEGORIES108(name, iconimage, desc, fanart)
	elif mode == 109:
		CATEGORIES109(name, iconimage, desc, fanart)
	elif mode == 110:       
		CATEGORIES110(name, iconimage, desc, fanart)
	elif mode == 111:
		CATEGORIES111(name, iconimage, desc, fanart)
	elif mode == 112: 
		CATEGORIES112(name, iconimage, desc, fanart)
	elif mode == 113:       
		CATEGORIES113(name, iconimage, desc, fanart)
	elif mode == 114:       
		CATEGORIES114(name, iconimage, desc, fanart)
	elif mode == 115:    
		CATEGORIES115(name, iconimage, desc, fanart)
	elif mode == 116:       
		CATEGORIES116(name, iconimage, desc, fanart)
	elif mode == 117:       
		CATEGORIES117(name, iconimage, desc, fanart)
	elif mode == 118:       
		CATEGORIES118(name, iconimage, desc, fanart)
	elif mode == 119:       
		CATEGORIES119(name, iconimage, desc, fanart)
	
	elif mode == 120:       
		CATEGORIES120(name, iconimage, desc, fanart)	
	elif mode == 121:
		CATEGORIES121(name, iconimage, desc, fanart)
	elif mode == 122: 
		CATEGORIES122(name, iconimage, desc, fanart)
	elif mode == 123:       
		CATEGORIES123(name, iconimage, desc, fanart)
	elif mode == 124:       
		CATEGORIES124(name, iconimage, desc, fanart)
	elif mode == 125:    
		CATEGORIES125(name, iconimage, desc, fanart)
	elif mode == 126:       
		CATEGORIES126(name, iconimage, desc, fanart)
	elif mode == 127:       
		CATEGORIES127(name, iconimage, desc, fanart)
	elif mode == 128:       
		CATEGORIES128(name, iconimage, desc, fanart)
	elif mode == 129:       
		CATEGORIES129(name, iconimage, desc, fanart)
	
	elif mode == 130:
		CATEGORIES130(name, iconimage, desc, fanart)
	elif mode == 131:
		CATEGORIES131(name, iconimage, desc, fanart)
	elif mode == 132: 
		CATEGORIES132(name, iconimage, desc, fanart)
	elif mode == 133:       
		CATEGORIES133(name, iconimage, desc, fanart)
	elif mode == 134:       
		CATEGORIES134(name, iconimage, desc, fanart)
	elif mode == 135:    
		CATEGORIES135(name, iconimage, desc, fanart)
	elif mode == 136:       
		CATEGORIES136(name, iconimage, desc, fanart)
	elif mode == 137:       
		CATEGORIES137(name, iconimage, desc, fanart)
	elif mode == 138:       
		CATEGORIES138(name, iconimage, desc, fanart)
	elif mode == 139:       
		CATEGORIES139(name, iconimage, desc, fanart)
	elif mode == 200:
		CATEGORIES200()
	elif mode == 201:
		xbmc.executebuiltin(url)
		sys.exit(0)
	elif mode == 999:
		CATEGORIES999()
	
	#10101+ = SUB-CATEGORIES2
	elif mode == 10001:
		CATEGORIES10001(name, iconimage, desc, fanart)
	elif mode == 10002:
		CATEGORIES10002(name, iconimage, desc, fanart)
	elif mode == 10003:
		CATEGORIES10003(name, iconimage, desc, fanart)
	elif mode == 10004:
		CATEGORIES10004(name, iconimage, desc, fanart)
	elif mode == 10005:
		CATEGORIES10005(name, iconimage, desc, fanart)
	elif mode == 10006:
		CATEGORIES10006(name, iconimage, desc, fanart)
	elif mode == 10007:
		CATEGORIES10007(name, iconimage, desc, fanart)
	elif mode == 10008:
		CATEGORIES10008(name, iconimage, desc, fanart)
	elif mode == 10009:
		CATEGORIES10009(name, iconimage, desc, fanart)
		
	elif mode == 10101:
		CATEGORIES10101(name, iconimage, desc, fanart)
	elif mode == 10102:
		CATEGORIES10102(name, iconimage, desc, fanart)
	elif mode == 10103:
		CATEGORIES10103(name, iconimage, desc, fanart)
	elif mode == 10104:
		CATEGORIES10104(name, iconimage, desc, fanart)
	elif mode == 10105:
		CATEGORIES10105(name, iconimage, desc, fanart)
	elif mode == 10106:
		CATEGORIES10106(name, iconimage, desc, fanart)
	elif mode == 10107:
		CATEGORIES10107(name, iconimage, desc, fanart)
	elif mode == 10108:
		CATEGORIES10108(name, iconimage, desc, fanart)
	elif mode == 10109:
		CATEGORIES10109(name, iconimage, desc, fanart)
		
	elif mode == 10201:
		CATEGORIES10201(name, iconimage, desc, fanart)
	elif mode == 10202:
		CATEGORIES10202(name, iconimage, desc, fanart)
	elif mode == 10203:
		CATEGORIES10203(name, iconimage, desc, fanart)
	elif mode == 10204:
		CATEGORIES10204(name, iconimage, desc, fanart)
	elif mode == 10205:
		CATEGORIES10205(name, iconimage, desc, fanart)
	elif mode == 10206:
		CATEGORIES10206(name, iconimage, desc, fanart)
	elif mode == 10207:
		CATEGORIES10207(name, iconimage, desc, fanart)
	elif mode == 10208:
		CATEGORIES10208(name, iconimage, desc, fanart)
	elif mode == 10209:
		CATEGORIES10209(name, iconimage, desc, fanart)
	
	elif mode == 10301:
		CATEGORIES10301(name, iconimage, desc, fanart)
	elif mode == 10302:
		CATEGORIES10302(name, iconimage, desc, fanart)
	elif mode == 10303:
		CATEGORIES10303(name, iconimage, desc, fanart)
	elif mode == 10304:
		CATEGORIES10304(name, iconimage, desc, fanart)
	elif mode == 10305:
		CATEGORIES10305(name, iconimage, desc, fanart)
	elif mode == 10306:
		CATEGORIES10306(name, iconimage, desc, fanart)
	elif mode == 10307:
		CATEGORIES10307(name, iconimage, desc, fanart)
	elif mode == 10308:
		CATEGORIES10308(name, iconimage, desc, fanart)
	elif mode == 10309:
		CATEGORIES10309(name, iconimage, desc, fanart)
	
	elif mode == 10401:
		CATEGORIES10401(name, iconimage, desc, fanart)
	elif mode == 10402:
		CATEGORIES10402(name, iconimage, desc, fanart)
	elif mode == 10403:
		CATEGORIES10403(name, iconimage, desc, fanart)
	elif mode == 10404:
		CATEGORIES10405(name, iconimage, desc, fanart)
	elif mode == 10406:
		CATEGORIES10406(name, iconimage, desc, fanart)
	elif mode == 10407:
		CATEGORIES10407(name, iconimage, desc, fanart)
	elif mode == 10408:
		CATEGORIES10408(name, iconimage, desc, fanart)
	elif mode == 10409:
		CATEGORIES10409(name, iconimage, desc, fanart)
	elif mode == 10410:
		CATEGORIES10410(name, iconimage, desc, fanart)
	elif mode == 10411:
		CATEGORIES10411(name, iconimage, desc, fanart)
	elif mode == 10412:
		CATEGORIES10412(name, iconimage, desc, fanart)
	elif mode == 10413:
		CATEGORIES10413(name, iconimage, desc, fanart)
	elif mode == 10414:
		CATEGORIES10414(name, iconimage, desc, fanart)
	elif mode == 10415:
		CATEGORIES10415(name, iconimage, desc, fanart)
	elif mode == 10416:
		CATEGORIES10416(name, iconimage, desc, fanart)
	elif mode == 10417:
		CATEGORIES10417(name, iconimage, desc, fanart)
	elif mode == 10418:
		CATEGORIES10418(name, iconimage, desc, fanart)
	elif mode == 10419:
		CATEGORIES10419(name, iconimage, desc, fanart)
	elif mode == 10420:
		CATEGORIES10420(name, iconimage, desc, fanart)
	elif mode == 10421:
		CATEGORIES10421(name, iconimage, desc, fanart)
	elif mode == 10422:
		CATEGORIES10422(name, iconimage, desc, fanart)
	elif mode == 10423:
		CATEGORIES10423(name, iconimage, desc, fanart)
	elif mode == 10424:
		CATEGORIES10424(name, iconimage, desc, fanart)
	elif mode == 10425:
		CATEGORIES10425(name, iconimage, desc, fanart)
	elif mode == 10426:
		CATEGORIES10426(name, iconimage, desc, fanart)
	elif mode == 10427:
		CATEGORIES10427(name, iconimage, desc, fanart)
	elif mode == 10428:
		CATEGORIES10428(name, iconimage, desc, fanart)
	elif mode == 10429:
		CATEGORIES10429(name, iconimage, desc, fanart)
	elif mode == 10430:
		CATEGORIES10430(name, iconimage, desc, fanart)
	
	elif mode == 10501:
		CATEGORIES10501(name, iconimage, desc, fanart)
	elif mode == 10502:
		CATEGORIES10502(name, iconimage, desc, fanart)
	elif mode == 10503:
		CATEGORIES10503(name, iconimage, desc, fanart)
	elif mode == 10504:
		CATEGORIES10504(name, iconimage, desc, fanart)
	elif mode == 10505:
		CATEGORIES10505(name, iconimage, desc, fanart)
	elif mode == 10506:
		CATEGORIES10506(name, iconimage, desc, fanart)
	elif mode == 10507:
		CATEGORIES10507(name, iconimage, desc, fanart)
	elif mode == 10508:
		CATEGORIES10508(name, iconimage, desc, fanart)
	elif mode == 10509:
		CATEGORIES10509(name, iconimage, desc, fanart)
	
	elif mode == 10601:
		CATEGORIES10601(name, iconimage, desc, fanart)
	elif mode == 10602:
		CATEGORIES10602(name, iconimage, desc, fanart)
	elif mode == 10603:
		CATEGORIES10603(name, iconimage, desc, fanart)
	elif mode == 10604:
		CATEGORIES10604(name, iconimage, desc, fanart)
	elif mode == 10605:
		CATEGORIES10605(name, iconimage, desc, fanart)
	elif mode == 10606:
		CATEGORIES10606(name, iconimage, desc, fanart)
	elif mode == 10607:
		CATEGORIES10607(name, iconimage, desc, fanart)
	elif mode == 10608:
		CATEGORIES10608(name, iconimage, desc, fanart)
	elif mode == 10609:
		CATEGORIES10609(name, iconimage, desc, fanart)
	
	elif mode == 10701:
		CATEGORIES10701(name, iconimage, desc, fanart)
	elif mode == 10702:
		CATEGORIES10702(name, iconimage, desc, fanart)
	elif mode == 10703:
		CATEGORIES10703(name, iconimage, desc, fanart)
	elif mode == 10704:
		CATEGORIES10704(name, iconimage, desc, fanart)
	elif mode == 10705:
		CATEGORIES10705(name, iconimage, desc, fanart)
	elif mode == 10706:
		CATEGORIES10706(name, iconimage, desc, fanart)
	elif mode == 10707:
		CATEGORIES10707(name, iconimage, desc, fanart)
	elif mode == 10708:
		CATEGORIES10708(name, iconimage, desc, fanart)
	elif mode == 10709:
		CATEGORIES10709(name, iconimage, desc, fanart)
	
	elif mode == 10801:
		CATEGORIES10801(name, iconimage, desc, fanart)
	elif mode == 10802:
		CATEGORIES10802(name, iconimage, desc, fanart)
	elif mode == 10803:
		CATEGORIES10803(name, iconimage, desc, fanart)
	elif mode == 10804:
		CATEGORIES10804(name, iconimage, desc, fanart)
	elif mode == 10805:
		CATEGORIES10805(name, iconimage, desc, fanart)
	elif mode == 10806:
		CATEGORIES10806(name, iconimage, desc, fanart)
	elif mode == 10807:
		CATEGORIES10807(name, iconimage, desc, fanart)
	elif mode == 10808:
		CATEGORIES10808(name, iconimage, desc, fanart)
	elif mode == 10809:
		CATEGORIES10809(name, iconimage, desc, fanart)
		
	elif mode == 10901:
		CATEGORIES10901(name, iconimage, desc, fanart)
	elif mode == 10902:
		CATEGORIES10902(name, iconimage, desc, fanart)
	elif mode == 10903:
		CATEGORIES10903(name, iconimage, desc, fanart)
	elif mode == 10904:
		CATEGORIES10904(name, iconimage, desc, fanart)
	elif mode == 10905:
		CATEGORIES10905(name, iconimage, desc, fanart)
	elif mode == 1090504:
		CATEGORIES1090504(name, iconimage, desc, fanart)
	elif mode == 10906:
		CATEGORIES10906(name, iconimage, desc, fanart)
	elif mode == 10907:
		CATEGORIES10907(name, iconimage, desc, fanart)
	elif mode == 10908:
		CATEGORIES10908(name, iconimage, desc, fanart)
	elif mode == 10909:
		CATEGORIES10909(name, iconimage, desc, fanart)
	elif mode == 10910:
		CATEGORIES10910(name, iconimage, desc, fanart)
	elif mode == 10911:
		CATEGORIES10911(name, iconimage, desc, fanart)
	elif mode == 10912:
		CATEGORIES10912(name, iconimage, desc, fanart)
	elif mode == 10913:
		CATEGORIES10913(name, iconimage, desc, fanart)
	elif mode == 10914:
		CATEGORIES10914(name, iconimage, desc, fanart)
	elif mode == 10915:
		CATEGORIES10915(name, iconimage, desc, fanart)
	elif mode == 10916:
		CATEGORIES10916(name, iconimage, desc, fanart)
	elif mode == 10917:
		CATEGORIES10917(name, iconimage, desc, fanart)
	elif mode == 10918:
		CATEGORIES10918(name, iconimage, desc, fanart)
	elif mode == 10919:
		CATEGORIES10919(name, iconimage, desc, fanart)
	elif mode == 10920:
		CATEGORIES10920(name, iconimage, desc, fanart)
	elif mode == 10921:
		CATEGORIES10921(name, iconimage, desc, fanart)
	elif mode == 10922:
		CATEGORIES10922(name, iconimage, desc, fanart)
	elif mode == 10923:
		CATEGORIES10923(name, iconimage, desc, fanart)
	elif mode == 10924:
		CATEGORIES10924(name, iconimage, desc, fanart)
	elif mode == 10925:
		CATEGORIES10925(name, iconimage, desc, fanart)
	elif mode == 10926:
		CATEGORIES10926(name, iconimage, desc, fanart)
	elif mode == 10927:
		CATEGORIES10927(name, iconimage, desc, fanart)
	elif mode == 10928:
		CATEGORIES10928(name, iconimage, desc, fanart)
	elif mode == 10929:
		CATEGORIES10929(name, iconimage, desc, fanart)
	elif mode == 10930:
		CATEGORIES10930(name, iconimage, desc, fanart)
	
	elif mode == 11101:
		CATEGORIES11101(name, iconimage, desc, fanart)
	elif mode == 11102:
		CATEGORIES11102(name, iconimage, desc, fanart)
	elif mode == 11103:
		CATEGORIES11103(name, iconimage, desc, fanart)
	elif mode == 11104:
		CATEGORIES11104(name, iconimage, desc, fanart)
	elif mode == 11105:
		CATEGORIES11105(name, iconimage, desc, fanart)
	elif mode == 11106:
		CATEGORIES11106(name, iconimage, desc, fanart)
	elif mode == 11107:
		CATEGORIES11107(name, iconimage, desc, fanart)
	elif mode == 11108:
		CATEGORIES11108(name, iconimage, desc, fanart)
	elif mode == 11109:
		CATEGORIES11109(name, iconimage, desc, fanart)
		
	else: notification("?","","",1000)
	
	if mode != "" and mode != None and mode != 100:
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_DURATION)
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
		#xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL, name)
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_NONE)
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_RATING)
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_YEAR)
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_DATE)
		xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED)
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
		xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE, name)
		
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE, name)
		printpoint = printpoint + "S"
	if mode != 17 and mode != 5 and mode != 21 and mode != 4 and mode != 9 and mode != 13 and mode != 3:
		printpoint = printpoint + "7"		
		xbmcplugin.endOfDirectory(int(sys.argv[1]))
		
		
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	printlog(title='pluginend', printpoint=printpoint, text=extra, level=0, option="")
	'''---------------------------'''
	return url, name, mode, iconimage, desc, num, viewtype, fanart
		
def pluginend2(admin, url, containerfolderpath, viewtype):
	printpoint = "" ; count = 0 ; countmax = 50 ; url = str(url) ; containerfolderpath2 = ""
	
	setProperty('script.featherence.service_resolved', '', type="home")
	dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
	dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
	while count < countmax and (dialogbusyW or dialogprogressW or count < 2) and not xbmc.abortRequested:
		count += 1
		if count == 1: printpoint = printpoint + "1"
		xbmc.sleep(100)
		dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
		dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
		'''---------------------------'''
		
	if count < countmax:
		printpoint = printpoint + "2"
		if count == 0: xbmc.sleep(1000)
		else: xbmc.sleep(500)
		containerfolderpath2 = xbmc.getInfoLabel('Container.FolderPath')

		if containerfolderpath != containerfolderpath2 and General_AutoView == "true":
			printpoint = printpoint + "5"
			setView(viewtype, containerfolderpath, containerfolderpath2)
			'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "count" + space2 + str(count) + space + "containerfolderpath/2" + newline + \
	str(containerfolderpath) + newline + \
	str(containerfolderpath2) + newline + \
	'viewtype' + space2 + str(viewtype) + newline + \
	"url" + space2 + str(url)
	printlog(title='pluginend2', printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''

def addView(viewtype):
	name = 'addView' ; printpoint = "" ; TypeError = "" ; extra = "" ; x = ""
	
	containerfolderpath2 = containerfolderpath
	x, z, s = getView(x, viewtype, containerfolderpath, containerfolderpath2)
	
	'''Get Viewmode number'''
	import xbmcvfs
	
	skin = xbmc.getSkinDir()
	skinPath = xbmc.translatePath('special://skin/')
	xml = os.path.join(skinPath,'addon.xml')
	file = xbmcvfs.File(xml)
	read = file.read().replace('\n','')
	file.close()
	try: src = re.compile('defaultresolution="(.+?)"').findall(read)[0]
	except: src = re.compile('<res.+?folder="(.+?)"').findall(read)[0]
	src = os.path.join(skinPath, src)
	src = os.path.join(src, 'MyVideoNav.xml')
	file = xbmcvfs.File(src)
	read = file.read().replace('\n','')
	file.close()
	views = re.compile('<views>(.+?)</views>').findall(read)[0]
	views = [int(x) for x in views.split(',')]
	for view in views:
		label = xbmc.getInfoLabel('Control.GetLabel(%s)' % (view))
		if not (label == '' or label == None): break
	x = str(view)
	
	y = xbmc.getInfoLabel('Container.Viewmode')
	if addonID != "" and addonID != 'script.featherence.service' and s != "":
		setsetting_custom1(addonID, s, str(x))
		notification('View Mode: ' + str(to_utf8(y)) + space + '(' + str(to_utf8(x)) + ')',str(to_utf8(z)),'',4000)
	else:
		notification_common('17')
	
def addView_(viewtype):
    name = 'addView' ; printpoint = "" ; TypeError = "" ; extra = "" ; content = ""
    import xbmcvfs
    try:
		from sqlite3 import dbapi2 as database
    except:
		from pysqlite2 import dbapi2 as database
    
    try:
        skin = xbmc.getSkinDir()
        skinPath = xbmc.translatePath('special://skin/')
        xml = os.path.join(skinPath,'addon.xml')
        file = xbmcvfs.File(xml)
        read = file.read().replace('\n','')
        file.close()
        try: src = re.compile('defaultresolution="(.+?)"').findall(read)[0]
        except: src = re.compile('<res.+?folder="(.+?)"').findall(read)[0]
        src = os.path.join(skinPath, src)
        src = os.path.join(src, 'MyVideoNav.xml')
        file = xbmcvfs.File(src)
        read = file.read().replace('\n','')
        file.close()
        views = re.compile('<views>(.+?)</views>').findall(read)[0]
        views = [int(x) for x in views.split(',')]
        for view in views:
            label = xbmc.getInfoLabel('Control.GetLabel(%s)' % (view))
            if not (label == '' or label == None): break
        record = (skin, viewtype, str(view))
        xbmcvfs.mkdir(addonProfile)
        dbcon = database.connect(os.path.join(addonProfile, 'views.db'))
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS views (""skin TEXT, ""view_type TEXT, ""view_id TEXT, ""UNIQUE(skin, view_type)"");")
        dbcur.execute("DELETE FROM views WHERE skin = '%s' AND view_type = '%s'" % (record[0], record[1]))
        dbcur.execute("INSERT INTO views Values (?, ?, ?)", record)
        dbcon.commit()
        viewName = xbmc.getInfoLabel('Container.Viewmode')

        notification(addonString_servicefeatherence(32398).encode('utf-8'), viewName + str(view) , '', 2000)
    except Exception, TypeError:
        extra = 'TypeError' + space2 + str(TypeError)
        #return
	
	text = "content" + space2 + str(content) + space + newline + \
	'view' + space2 + str(view) + newline + \
	extra
	printlog(title=name, printpoint=printpoint, text=text, level=7, option="")
	
def getCustom_Playlist(admin):
	'''Get the next new Item ID of a user favourite'''
	returned = "" ; printpoint = ""
	if Custom_Playlist1_ID  == "": returned = 'Custom_Playlist1_ID'
	elif Custom_Playlist2_ID  == "": returned = 'Custom_Playlist2_ID'
	elif Custom_Playlist3_ID  == "": returned = 'Custom_Playlist3_ID'
	elif Custom_Playlist4_ID  == "": returned = 'Custom_Playlist4_ID'
	elif Custom_Playlist5_ID  == "": returned = 'Custom_Playlist5_ID'
	elif Custom_Playlist6_ID  == "": returned = 'Custom_Playlist6_ID'
	elif Custom_Playlist7_ID  == "": returned = 'Custom_Playlist7_ID'
	elif Custom_Playlist8_ID  == "": returned = 'Custom_Playlist8_ID'
	elif Custom_Playlist9_ID  == "": returned = 'Custom_Playlist9_ID'
	elif Custom_Playlist10_ID  == "": returned = 'Custom_Playlist10_ID'
	'''---------------------------'''
	text = "returned" + space2 + str(returned) + space + "Custom_Playlist1_ID" + space2 + str(Custom_Playlist1_ID)
	printlog(title="getCustom_Playlist", printpoint=printpoint, text=text, level=2, option="")
	return returned

def getCustom_Playlist2(value):
	'''Get the current item ID'''
	returned = "" ; printpoint = "" ; TypeError = "" ; extra = ""
	
	if Custom_Playlist1_ID  == "": returned = 'Custom_Playlist1_ID'
	
	try:
		returned = Custom_PlaylistL.index(value)
		returned += 1
		returned = 'Custom_Playlist' + str(returned) + '_ID'
	except Exception, TypeError: extra = extra + newline + 'TypeError' + space2 + str(TypeError)
	
	text = "returned" + space2 + str(returned) + newline + \
	"value" + space2 + str(value)
	printlog(title="getCustom_Playlist2", printpoint=printpoint, text=text, level=2, option="")
	return returned

def setCustom_Playlist_ID(Custom_Playlist_ID, New_ID, mode, url, name, num, viewtype):
	'''Revise user input url'''
	printpoint = "" ; extra = "" ; extra2 = "" ; New_Type = "" ; New_ID_ = "" ; New_IDL = "" ; DuplicatedL = [] ; IgnoredL = []
	Custom_Playlist_ID_ = getsetting(Custom_Playlist_ID)
	Custom_Playlist_ID_L = Custom_Playlist_ID_.split(',')
	
		
	if mode == 24:
		if New_ID == 'Custom':
			New_Type = 'New Custom'
		else:
			New_Type = 'Custom'
		New_ID = url
		New_ID_ = url
		extra = addonString_servicefeatherence(32439).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(32440).encode('utf-8') #New %s, Update Succesfully!
	
	elif "list=" in New_ID or len(New_ID) == 10 or '&youtube_pl=' in New_ID:
		'''Playlist'''
		New_Type = localize(559) #Playlist
		extra = addonString_servicefeatherence(32439).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(32440).encode('utf-8') #New %s, Update Succesfully!
		if "list=" in New_ID:
			New_ID = find_string(New_ID, "list=", "")
			New_ID = New_ID.replace("list=","&youtube_pl=")
		elif "&youtube_ch" in New_ID:
			New_ID = find_string(New_ID, "&youtube_ch=", "")
		New_ID_ = New_ID.replace("&youtube_pl=","")
		'''---------------------------'''
	elif "/user/" in New_ID or "/channel/" in New_ID or '&youtube_ch=' in New_ID:
		'''Channel'''
		New_Type = localize(19029) #Channel
		extra = addonString_servicefeatherence(32438).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(32421).encode('utf-8') #New %s, Update Succesfully!
		if "/channel/" in New_ID:
			New_ID = find_string(New_ID, "/channel/", "")
			New_ID = New_ID.replace("/channel/", "&youtube_ch=")
		elif "/user/"    in New_ID:
			New_ID = find_string(New_ID, "/user/", "")
			New_ID = New_ID.replace("/user/", "&youtube_ch=")
		elif "&youtube_ch" in New_ID:
			New_ID = find_string(New_ID, "&youtube_ch=", "")
			
		New_ID_ = New_ID.replace("&youtube_ch=","")
		'''---------------------------'''
	elif "watch?v=" in New_ID or '&youtube_id=' in New_ID:
		'''Single Video'''
		New_Type = localize(157) #Video
		extra = addonString_servicefeatherence(32438).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(32421).encode('utf-8') #New %s, Update Succesfully!
		if "watch?v=" in New_ID: New_ID = find_string(New_ID, "watch?v=", "")
		else: New_ID = find_string(New_ID, "&youtube_id", "")
		
		New_ID = New_ID.replace("watch?v=", "&youtube_id=")
		New_ID_ = New_ID.replace("&youtube_id=","")
		'''---------------------------'''
	elif "results?search_query=" in New_ID or '&youtube_se=' in New_ID:
		'''Search Video'''
		New_Type = localize(137) #Search
		extra = addonString_servicefeatherence(32438).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(32421).encode('utf-8') #New %s, Update Succesfully!
		if "results?search_query=" in New_ID: New_ID = find_string(New_ID, "results?search_query=", "")
		else: New_ID = find_string(New_ID, "&youtube_se=", "")
		New_ID = New_ID.replace("results?search_query=", "&youtube_se=")
		New_ID_ = New_ID.replace("&youtube_se=","")
		'''---------------------------'''
	
	elif "&custom4=" in New_ID:
		'''Direct Video'''
		New_Type = 'Direct Video' #Direct Video
		extra = addonString_servicefeatherence(32439).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(32440).encode('utf-8') #New %s, Update Succesfully!
		'''---------------------------'''	
		
	elif "&custom8=" in New_ID:
		'''Add-on'''
		New_Type = localize(24000) #Add-on
		extra = addonString_servicefeatherence(32439).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(32440).encode('utf-8') #New %s, Update Succesfully!
		'''---------------------------'''	
		
	elif New_ID == "None":
		New_Type = localize(2080) #Empty list
		extra = addonString_servicefeatherence(32439).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(32440).encode('utf-8') #New %s, Update Succesfully!
		New_ID_ = ""
		
	if New_Type != "":
		printpoint = printpoint + "1"
		New_IDL = CleanString2(New_ID, comma=True)
		New_IDL = New_IDL.split(',')
		for x in New_IDL:
			
			if 'commonsearch' in x:
				IgnoredL.append(x)
			elif x in Custom_Playlist_ID_L and x != "":
				DuplicatedL.append(x)
				if mode == 20 or mode == 21:
					check = dialogyesno(addonString_servicefeatherence(32457).encode('utf-8'), localize(19194)) # Duplicated URL found!, Continue?
					if check == "ok": pass				
					else: notification_common("9") ; printpoint = printpoint + "8"
					break
				else:
					pass
					
			
		
		if mode == 24 or mode == 21:
			for x in IgnoredL:
				New_IDL.remove(x)
			for x in DuplicatedL:
				New_IDL.remove(x)
			
				
			New_ID = CleanString2(New_IDL, comma=True)
			New_ID_ = New_ID
		
		if not "8" in printpoint and New_ID != "":
			printpoint = printpoint + "2"
			if mode == 20 or mode == 24 and New_Type == 'New Custom':
				setsetting(Custom_Playlist_ID, New_ID)
			elif mode == 21:
				setsetting(Custom_Playlist_ID, str(url) + "," + New_ID)
				#extra = "Previous ID: " + str(url)
			elif mode == 24:
				setsetting(Custom_Playlist_ID, Custom_Playlist_ID_ + "," + New_ID)
				
			else: notification_common("17") ; printpoint = printpoint + "9"
			#extra = addonString_servicefeatherence(32438).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(32421).encode('utf-8')
			if 'Custom' in New_Type: ID_Info = "" #'Source: ' + name
			else: ID_Info = "ID: " + str(New_ID_)
			
			if DuplicatedL != []:
				extra2 = 'Duplicated ID Ignored:[CR]' + str(DuplicatedL)
			dialogok(extra, str(name), ID_Info, extra2, line1c="yellow", line2c="yellow") ; xbmc.sleep(100)
			update_view(url, num, viewtype)
			'''---------------------------'''
		elif DuplicatedL != []: notification('Already exists in favourites!','','',2000)
		elif New_ID == "": notification('NO valid url has been detected!','','',2000)
		
	else: notification_common("17") ; printpoint = printpoint + "9"
	
	text = "name" + space2 + str(name) + space + 'mode' + space2 + str(mode) + newline + \
	"New_Type" + space2 + str(New_Type) + newline + \
	"New_ID" + space2 + str(New_ID) + newline + \
	"New_ID_" + space2 + str(New_ID_) + newline + \
	"New_IDL" + space2 + str(New_IDL) + newline + \
	"DuplicatedL" + space2 + str(DuplicatedL) + newline + \
	"IgnoredL" + space2 + str(IgnoredL) + newline + \
	"Custom_Playlist_ID_L" + space2 + str(Custom_Playlist_ID_L) + newline + \
	"Custom_Playlist_ID" + space2 + str(Custom_Playlist_ID) + newline
	printlog(title="setCustom_Playlist_ID", printpoint=printpoint, text=text, level=2, option="")
	'''---------------------------'''

def AdvancedCustom(mode, name, url, thumb, desc, num, viewtype, fanart):
	'''------------------------------
	---Backup/Restore-My-Addon-------
	------------------------------'''
	printpoint = "" ; extra = "" ; formula = "" ; formula_ = "" ; path = "" ; file = "" ; returned = "" ; returned2 = ""; returned3 = "" ; y = "s" ; custommediaL = [] ; list2_ = [] ; list2 = [] ; filesT_ = []
	
	if num == 's':
		list = ['-> (Exit)']
		list.append(localize(190) + space + localize(593)) #Save All
		list.append(addonString_servicefeatherence(32442).encode('utf-8') + space + localize(593) + space + "[LOCAL]") #Load All [LOCAL]
		list.append(addonString_servicefeatherence(32442).encode('utf-8') + space + localize(593) + space + "[REMOTE]") #Load All [REMOTE] 
		list.append('Remove all buttons') #Remove-All-Buttons
		
		y = "s"
		'''---------------------------'''
	else:
		list = ['-> (Exit)']
		list.append(localize(190) + space + addonString_servicefeatherence(32443).encode('utf-8')) #Save One
		list.append(addonString_servicefeatherence(32442).encode('utf-8') + space + addonString_servicefeatherence(32443).encode('utf-8') + space + "[LOCAL]") #Load One [LOCAL]
		list.append(addonString_servicefeatherence(32442).encode('utf-8') + space + addonString_servicefeatherence(32443).encode('utf-8') + space + "[REMOTE]") #Load One [REMOTE]
		y = ""
		
		Custom_Playlist_ID = "Custom_Playlist" + num + "_ID"
		if Custom_Playlist_ID == "": notification(addonString_servicefeatherence(32145).encode('utf-8'), addonString_servicefeatherence(32101).encode('utf-8'), "", 2000) ; printpoint = printpoint + "9"
		Custom_Playlist_Name = "Custom_Playlist" + num + "_Name"
		Custom_Playlist_Thumb = "Custom_Playlist" + num + "_Thumb"
		Custom_Playlist_Description = "Custom_Playlist" + num + "_Description"
		Custom_Playlist_Fanart = "Custom_Playlist" + num + "_Fanart"
		'''---------------------------'''
	returned, value = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list,0)
	
	if returned == -1: printpoint = printpoint + "9"
	elif returned == 0: printpoint = printpoint + "8"
	else: printpoint = printpoint + "7"
		
	if ("7" in printpoint or value != "") and not "8" in printpoint and not "9" in printpoint:
		
		if returned == 1 or returned == 2: path = os.path.join(addondata_path, addonID, '') #SAVE /LOAD [LOCAL]
		elif returned == 3: path = os.path.join(addonPath, 'resources', 'templates', '') #LOAD [REMOTE]
		elif returned == 4: pass #REMOVE ALL
		else: path = ""
		
		list2 = ['-> (Exit)'] ; list2_ = ['-> (Exit)']
		if returned == 1:
			list2.append('New')
			list2_.append('New')
		elif returned == 3:
			check = dialogyesno(addonString_servicefeatherence(32459).encode('utf-8') % addonString(30000).encode('utf-8'), addonString_servicefeatherence(32458).encode('utf-8')) #Share My button, Choose YES to learn how to share Your Music button
			if check == 'ok':
				header = addonString_servicefeatherence(32459).encode('utf-8') % addonString(30000).encode('utf-8')
				msg1 = localize(190) + space + localize(592) ; msg1.decode('utf-8').encode('utf-8')
				msg2 = os.path.join(addondata_path, addonID) ; msg2 = msg2.decode('utf-8').encode('utf-8')
				message = addonString_servicefeatherence(32143).encode('utf-8')
				diaogtextviewer(header,message)
				
		if path != "":
			'''read existing files'''
			filesT = {}
			AddonName = addonID.replace('plugin.video.', "", 1)
			AddonName = AddonName + str(y) + '_'
			for files in os.listdir(path):
				filesname = ""
				if '.zip' in files and not '.txt' in files:
					if AddonName in files:
						filesname = regex_from_to(files, AddonName, ".zip", excluding=True)
						if filesname != "" and filesname != None:
							filesT_ = { filesname: files }
							filesT.update(filesT_)
							filedate = getFileAttribute(1, path + files, option="1")
							list2_.append(filesname + space + '-(' + str(filedate) + ')')
							list2.append(filesname)
							extra = 'files' + space2 + to_utf8(files) + newline + 'filesname' + space2 + to_utf8(filesname)
							#print extra 
							'''---------------------------'''
			
			returned2, value2 = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list2_,0)
			
			if returned2 == -1: printpoint = printpoint + "9"
			elif returned2 == 0: printpoint = printpoint + "8"
			else: printpoint = printpoint + "7"
				
			if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
				if returned == 1: printpoint = printpoint + "A" #SAVE
				elif returned == 2: printpoint = printpoint + "B" #LOAD
				elif returned == 3: printpoint = printpoint + "C" #TEMPLATES
		
				if "A" in printpoint:
					if returned2 > 1:
						yesno = dialogyesno(localize(13206) + space + str(list2[returned2]) + '?',localize(19194))
						if yesno == 'skip': printpoint = printpoint + '9'
					if not '9' in printpoint:
						formula = ""
						if y == "s":
							'''save all'''
							min = 1
							max = 11
						else:
							'''save one'''
							min = int(num)
							max = int(num) + 1
							
						for i in range(min,max):

							Custom_Playlist_ID_ = "Custom_Playlist" + str(i) + "_ID"
							Custom_Playlist_Name_ = "Custom_Playlist" + str(i) + "_Name"
							Custom_Playlist_Thumb_ = "Custom_Playlist" + str(i) + "_Thumb"
							Custom_Playlist_Description_ = "Custom_Playlist" + str(i) + "_Description"
							Custom_Playlist_Fanart_ = "Custom_Playlist" + str(i) + "_Fanart"
							
							Custom_Playlist_ID__ = getsetting(Custom_Playlist_ID_)
							Custom_Playlist_Name__ = getsetting(Custom_Playlist_Name_)
							Custom_Playlist_Thumb__ = getsetting(Custom_Playlist_Thumb_)
							Custom_Playlist_Description__ = getsetting(Custom_Playlist_Description_)
							Custom_Playlist_Fanart__ = getsetting(Custom_Playlist_Fanart_)
							
							if Custom_Playlist_ID__ == "":
								
								formula = formula + newline + Custom_Playlist_ID_ + "=5" + ""
								formula = formula + newline + Custom_Playlist_Name_ + "=5" + ""
								formula = formula + newline + Custom_Playlist_Thumb_ + "=5" + ""
								formula = formula + newline + Custom_Playlist_Description_ + "=5" + ""
								formula = formula + newline + Custom_Playlist_Fanart_ + "=5" + ""
							
							else:
								formula = formula + newline + Custom_Playlist_ID_ + "=5" + Custom_Playlist_ID__
								formula = formula + newline + Custom_Playlist_Name_ + "=5" + Custom_Playlist_Name__
								x2, x2_ = TranslatePath(Custom_Playlist_Thumb__)
								formula, custommediaL, = GeneratePath(Custom_Playlist_Thumb_ + "=5", formula, custommediaL, x2, x2_, ignoreL=[])
										
								formula = formula + newline + Custom_Playlist_Description_ + "=5" + Custom_Playlist_Description__
								x2, x2_ = TranslatePath(Custom_Playlist_Fanart__)
								formula, custommediaL, = GeneratePath(Custom_Playlist_Fanart_ + "=5", formula, custommediaL, x2, x2_, ignoreL=[])
							
							extra = extra + newline + 'i' + space2 + str(i) + space + 'Custom_Playlist_ID_' + space2 + str(Custom_Playlist_ID_) + space + 'Custom_Playlist_ID__' + space2 + str(Custom_Playlist_ID__)
							
						if returned2 == 1: filename = ""
						else: filename = str(list2[returned2])
						
						filename = dialogkeyboard(filename, localize(21821), 0, "", "", "") #Description
						if filename != 'skip' and filename != "":
							formula = to_utf8(formula)
						
							write_to_file(featherenceserviceaddondata_media_path + AddonName + ".txt", str(formula), append=False, silent=True, utf8=False) ; xbmc.sleep(200)
							if not os.path.exists(featherenceserviceaddondata_media_path + AddonName + ".txt"):
								notification_common('17')
								extra = extra + newline + featherenceserviceaddondata_media_path + AddonName + ".txt" + space + 'Is not found!'
							else:
								removefiles(path + AddonName + to_unicode(list2[returned2]) + '.zip')
								zipname = path + AddonName + str(filename).decode('utf-8')
								if custommediaL == []:
									CreateZip(featherenceserviceaddondata_media_path, zipname, filteron=[AddonName + '.txt'], filteroff=[], level=10000, append=False, ZipFullPath=False, temp=False)
								else:
									CreateZip(featherenceserviceaddondata_media_path, zipname, filteron=[AddonName + '.txt'], filteroff=[], level=10000, append=False, ZipFullPath=False, temp=True)
									CreateZip(featherenceserviceaddondata_media_path, zipname, filteron=custommediaL, filteroff=[], level=10000, append='End', ZipFullPath=False, temp=True)
								notification(addonString_servicefeatherence(32444).encode('utf-8'), str(filename), "", 4000) #Saved Succesfully!, 
								'''---------------------------'''
						else: notification_common('9') ; extra = extra + newline + 'filename is empty!'
						
				elif "B" in printpoint or "C" in printpoint:
					'''------------------------------
					---Load/Templates----------------
					------------------------------'''
					filename = str(list2[returned2])
					file = filesT.get(filename)
					
					if file == "" or file == None:
						notification(addonString_servicefeatherence(32144).encode('utf-8'), "", "", 4000) #Invalid File!
					elif not os.path.exists(path + file):
						'''nothing to load'''
						notification(localize(33077), addonString_servicefeatherence(32127).encode('utf-8'), "", 4000)
					else:
						if os.path.exists(featherenceserviceaddondata_media_path + AddonName + '.txt'):
							removefiles(featherenceserviceaddondata_media_path + AddonName + '.txt')
							
						ExtractAll(path + file, featherenceserviceaddondata_media_path) ; xbmc.sleep(200)
						
						if not os.path.exists(featherenceserviceaddondata_media_path + AddonName + '.txt'):
							notification(addonString_servicefeatherence(32128).encode('utf-8') % (AddonName), addonString_servicefeatherence(32129).encode('utf-8'), "", 4000) #AddonName is missing! , Check your zip file!
						else:
							if y == 's':
								yesno = dialogyesno(addonString_servicefeatherence(32122).encode('utf-8') + '?',localize(19194)) #Overwrite
								if yesno == 'skip': printpoint = printpoint + '9'
							else:
								yesno = dialogyesno(addonString_servicefeatherence(32122).encode('utf-8') + space + xbmc.getInfoLabel('ListItem.Label') + '?',localize(19194)) #Overwrite
								if yesno == 'skip': printpoint = printpoint + '9'
								
							if not '9' in printpoint:
								printpoint = printpoint + "V"
								#print file
								import fileinput
								for line in fileinput.input(featherenceserviceaddondata_media_path + AddonName + '.txt'):
									x = "" ; x1 = "" ; x2 = "" ; x3 = ""
									if "=5" in line:
										'''setsetting'''
										x1 = regex_from_to(line, 'Custom_Playlist', '=5', excluding=False)
										x2 = line.replace(x1,"")
										x2 = x2.replace('\n', '')
										x1 = x1.replace('=5',"")
										
										
										if y == "":
											x1_ = regex_from_to(x1, 'Custom_Playlist', '_', excluding=True) #count
											x1__ = x1.replace('Custom_Playlist' + x1_ + '_','Custom_Playlist' + str(num) + '_')
											setsetting(str(x1__), str(x2))
										else:
											setsetting(str(x1), str(x2))
										
									extra = extra + newline + space + "line" + space2 + str(line) + space + "x " + space2 + str(x) + space + "x1" + space2 + str(x1) + space + "x2" + space2 + str(x2) + space + "x3" + space2 + str(x3)
									'''---------------------------'''	
		elif returned == 4:
			'''------------------------------
			---Remove-All-Buttons------------
			------------------------------'''
			Custom_Playlist_NameL = [Custom_Playlist1_Name, Custom_Playlist2_Name, Custom_Playlist3_Name, Custom_Playlist4_Name, Custom_Playlist5_Name, Custom_Playlist6_Name, Custom_Playlist7_Name, Custom_Playlist8_Name, Custom_Playlist9_Name, Custom_Playlist10_Name]
			returned = dialogyesno(addonString_servicefeatherence(32123).encode('utf-8') + '[CR]' + str(Custom_Playlist_NameL),localize(19194)) #Remove All Buttons?
			if returned == "ok":
				for x in range(1,11):
					setsetting('Custom_Playlist' + str(x) + '_ID', "")
					setsetting('Custom_Playlist' + str(x) + '_Name', "")
					setsetting('Custom_Playlist' + str(x) + '_Thumb', "")
					setsetting('Custom_Playlist' + str(x) + '_Description', "")
					setsetting('Custom_Playlist' + str(x) + '_Fanart', "")
					'''---------------------------'''
				if desc != "": extra1 = localize(21821) + space2 + str(desc)
				else: extra1 = ""
				dialogok(localize(50) + space + addonString_servicefeatherence(32435).encode('utf-8') + '[CR]' + str(name), "ID" + space2 + str(url), "", extra1)
				'''---------------------------'''
		else: printpoint = printpoint + '9'	
				
	if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
		if not "Q" in printpoint and not "A" in printpoint:
			notification(".","","",1000)
			xbmc.sleep(500)
			notification("..","","",1000)
			update_view(url, num, viewtype)
			'''---------------------------'''
	
	text = 'name_' + space2 + name + "_LV" + printpoint + space + newline + \
	"path" + space2 + str(path) + newline + \
	"list" + space2 + str(list) + space + 'returned' + space2 + str(returned) + newline + \
	"list2" + space2 + str(list2) + space + 'returned2' + space2 + str(returned2) + newline + \
	"list2_" + space2 + str(list2) + space + 'returned2_' + newline + \
	"file" + space2 + str(file) + newline + \
	"filesT_" + space2 + str(filesT_) + newline + \
	"formula" + space2 + str(formula) + space + "formula_" + space2 + str(formula_) + newline + \
	"extra" + space2 + str(extra)
	printlog(title="AdvancedCustom", printpoint=printpoint, text=text, level=2, option="")
		
def AddCustom(mode, name, url, iconimage, desc, num, viewtype, fanart):
	'''------------------------------
	---New-Button--------------------
	------------------------------'''
	printpoint = "" ; New_Type = "" ; New_ID = "" ; New_Name = "" ; value = "" ; value2 = ""
	Custom_Playlist_ID = getCustom_Playlist(admin)
	Custom_Playlist_Name = Custom_Playlist_ID.replace("_ID","_Name")
	if Custom_Playlist_ID == "": notification(addonString_servicefeatherence(32132).encode('utf-8'), addonString_servicefeatherence(32133).encode('utf-8'), "", 4000)
	elif mode == 24:
		'''from Menu'''
		list = ['-> (Exit)', 'New']
		for x in Custom_PlaylistL:
			if x != "":
				x2 = Custom_Playlist_NameT.get(x)
				x2 = to_utf8(x2)
				list.append(x2) #NAME
		returned, value = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list,0)
		
		if returned == -1: pass
		elif returned == 0: pass
		elif returned == 1:
			printpoint = printpoint + "1"
			New_Name = dialogkeyboard(addonString_servicefeatherence(32124).encode('utf-8'), addonString_servicefeatherence(32110).encode('utf-8'), 0, "",Custom_Playlist_Name, "0")
			setCustom_Playlist_ID(Custom_Playlist_ID, 'New Custom', mode, url, New_Name, num, viewtype)
		else:
			printpoint = printpoint + "2"
			New_Name = value
			value2 = Custom_Playlist_NameT2.get(value) #ID
			Custom_Playlist_ID = getCustom_Playlist2(value2)
			setCustom_Playlist_ID(Custom_Playlist_ID, url, mode, url, New_Name, num, viewtype)
			
	else:
		num = Custom_Playlist_ID.replace('Custom_Playlist',"")
		num = num.replace('_ID',"")
		ManageCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
		if 1 + 1 == 3:
			New_ID = dialogkeyboard("", addonString_servicefeatherence(32125).encode('utf-8'), 0, "5", "" , "")
			if New_ID != "skip":
				New_Name = dialogkeyboard(addonString_servicefeatherence(32124).encode('utf-8'), addonString_servicefeatherence(32110).encode('utf-8'), 0, "",Custom_Playlist_Name, "0")
				if New_Name != "skip":
					setCustom_Playlist_ID(Custom_Playlist_ID, New_ID, mode, url, New_Name, num, viewtype)
				
	text = "mode" + space2 + str(mode) + space + "name" + space2 + str(name) + newline + \
	"New_Type" + space2 + str(New_Type) + newline + \
	"New_ID" + space2 + str(New_ID) + newline + \
	"New_Name" + space2 + str(New_Name) + newline + \
	"value" + space2 + str(value) + newline + \
	"value2" + space2 + str(value2) + newline + \
	"url" + space2 + str(url) + newline + \
	"num" + space2 + str(num) + newline + \
	"iconimage" + space2 + str(iconimage) + newline
	printlog(title="AddCustom", printpoint=printpoint, text=text, level=2, option="")
	'''---------------------------'''

def cleanfanartCustom(fanart):
	printpoint = ""
	fanart2 = fanart.replace("/","")
	fanart2 = fanart2.replace("\\","")
	addonFanart2 = addonFanart.replace("/","")
	addonFanart2 = addonFanart2.replace("\\","")
	if fanart2 == addonFanart2:
		printpoint = printpoint + "7"
		fanart = "" # or not os.path.exists(fanart)
	
	text = "fanart" + space2 + str(fanart) + newline + \
	"fanart2" + space2 + str(fanart2) + newline + \
	"addonFanart" + space2 + str(addonFanart) + newline + \
	"addonFanart2" + space2 + str(addonFanart2)
	printlog(title="cleanfanartCustom", printpoint=printpoint, text=text, level=2, option="")
	return fanart
	
def MoveCustom(mode, name, url, iconimage, desc, num, viewtype, fanart):
	'''Reposition customized buttons'''
	printpoint = ""
	'''---------------------------'''
	if not "__" in num: printpoint = printpoint + "9"
	else:
		printpoint = printpoint + "1"
		num = num.split("__")
		num1 = num[0]
		num2 = num[1]
	try:
		test = int(num1) + 1
		test = int(num2) + 1
	except Exception, TypeError: printpoint = printpoint + "9"
	
	fanart = cleanfanartCustom(fanart)
	
	if not "9" in printpoint:
		printpoint = printpoint + "3"
		Custom_Playlist_ID = "Custom_Playlist" + num1 + "_ID"
		if Custom_Playlist_ID == "": notification(addonString_servicefeatherence(32145).encode('utf-8'), addonString_servicefeatherence(32101).encode('utf-8'), "", 2000) ; printpoint = printpoint + "9"
		Custom_Playlist_Name = "Custom_Playlist" + num1 + "_Name"
		Custom_Playlist_Thumb = "Custom_Playlist" + num1 + "_Thumb"
		Custom_Playlist_Description = "Custom_Playlist" + num1 + "_Description"
		Custom_Playlist_Fanart = "Custom_Playlist" + num1 + "_Fanart"
		'''---------------------------'''
		Custom_Playlist_ID2 = "Custom_Playlist" + str(num2) + "_ID"
		if Custom_Playlist_ID2 == "": notification(addonString_servicefeatherence(32145).encode('utf-8'), addonString_servicefeatherence(32101).encode('utf-8'), "", 2000) ; printpoint = printpoint + "9"
		Custom_Playlist_Name2 = "Custom_Playlist" + str(num2) + "_Name"
		Custom_Playlist_Thumb2 = "Custom_Playlist" + str(num2) + "_Thumb"
		Custom_Playlist_Description2 = "Custom_Playlist" + str(num2) + "_Description"
		Custom_Playlist_Fanart2 = "Custom_Playlist" + str(num2) + "_Fanart"
		'''---------------------------'''
	
	if not "9" in printpoint:
		printpoint = printpoint + "7"
		'''---------------------------'''
		setsetting(Custom_Playlist_ID, getsetting(Custom_Playlist_ID2))
		setsetting(Custom_Playlist_Name, getsetting(Custom_Playlist_Name2))
		setsetting(Custom_Playlist_Thumb, getsetting(Custom_Playlist_Thumb2))
		setsetting(Custom_Playlist_Description, getsetting(Custom_Playlist_Description2))
		setsetting(Custom_Playlist_Fanart, getsetting(Custom_Playlist_Fanart2))
		'''---------------------------'''
		setsetting(Custom_Playlist_ID2, url)
		setsetting(Custom_Playlist_Name2, name)
		setsetting(Custom_Playlist_Thumb2, iconimage)
		setsetting(Custom_Playlist_Description2, desc)
		setsetting(Custom_Playlist_Fanart2, fanart)
		'''---------------------------'''
		update_view(url, num, viewtype)
	
	text = "url" + space2 + str(url) + space + "num" + space2 + str(num)
	printlog(title="MoveCustom", printpoint=printpoint, text=text, level=2, option="")
		
def ManageCustom(mode, name, url, thumb, desc, num, viewtype, fanart):
	extra = "" ; printpoint = "" ; New_ID = ""
	
	Custom_Playlist_ID = "Custom_Playlist" + num + "_ID"
	if Custom_Playlist_ID == "": notification(addonString_servicefeatherence(32145).encode('utf-8'), addonString_servicefeatherence(32101).encode('utf-8'), "", 2000) ; printpoint = printpoint + "9"
	Custom_Playlist_Name = "Custom_Playlist" + num + "_Name"
	Custom_Playlist_Thumb = "Custom_Playlist" + num + "_Thumb"
	Custom_Playlist_Description = "Custom_Playlist" + num + "_Description"
	Custom_Playlist_Fanart = "Custom_Playlist" + num + "_Fanart"
	
	if printpoint != "9" and not url == 'New':
		list = ['-> (Exit)']
		list.append(addonString_servicefeatherence(32430).encode('utf-8')) #Edit URL
		list.append(addonString_servicefeatherence(32433).encode('utf-8')) #Rename Button
		if thumb == "": list.append(addonString_servicefeatherence(32428).encode('utf-8')) #Add Thumb
		else: list.append(addonString_servicefeatherence(32429).encode('utf-8')) #Remove Thumb
		if desc == "": list.append(addonString_servicefeatherence(32424).encode('utf-8')) #Add Description
		else: list.append(addonString_servicefeatherence(32425).encode('utf-8')) #Edit Description
		fanart = cleanfanartCustom(getsetting(Custom_Playlist_Fanart))
		if fanart == "": list.append(addonString_servicefeatherence(32426).encode('utf-8')) #Add Fanart
		else: list.append(addonString_servicefeatherence(32427).encode('utf-8')) #Remove Fanart
		list.append(localize(13336)) #Remove Button

		returned, value = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list,0)
			
		if returned == -1: printpoint = printpoint + "9"
		elif returned == 0: printpoint = printpoint + "8"
		else: printpoint = printpoint + "7"
	
	if "7" in printpoint and not "8" in printpoint and not "9" in printpoint and not url == 'New':
		if returned == 1: printpoint = printpoint + "A" #Edit URL
		elif returned == 2: printpoint = printpoint + "B" #Rename
		elif returned == 3: printpoint = printpoint + "C" #Add/Remove Thumb
		elif returned == 4: printpoint = printpoint + "D" #Add/Edit Description
		elif returned == 5: printpoint = printpoint + "E" #Add/Remove Fanart
		elif returned == 6: printpoint = printpoint + "F" #Remove Button
		'''---------------------------'''
	if "A" in printpoint or url == 'New':
		'''------------------------------
		---Edit-URL----------------------
		------------------------------'''
		list = ['-> (Exit)']
		list.append(addonString_servicefeatherence(32434).encode('utf-8')) #View URL
		list.append(addonString_servicefeatherence(32432).encode('utf-8')) #Add URL
		list.append(addonString_servicefeatherence(32431).encode('utf-8')) #Remove URL
		
		if not url == 'New':
			returned2, value = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list,0)
			
			if returned2 == -1: printpoint = printpoint + "9"
			elif returned2 == 0: printpoint = printpoint + "8"
			else: printpoint = printpoint + "7"
		
			if returned2 == 1: printpoint = printpoint + "1" #View URL
			elif returned2 == 2: printpoint = printpoint + "2" #Add URL
			elif returned2 == 3: printpoint = printpoint + "3" #Remove URL
		
		if "1" in printpoint:
			'''------------------------------
			---View-URL----------------------
			------------------------------'''
			message2 = "" ; i = 0
			url2 = url.split(",")
			for x in url2:
				i += 1
				x2 = ""
				if "&youtube_ch=" in x:
					x = x.replace("&youtube_ch=","")
					x2 = space + "[" + "YouTube Channel" + "]"
					'''---------------------------'''
				elif "&youtube_pl=" in x:
					x = x.replace("&youtube_pl=","")
					x2 = space + "[" + "YouTube Playlist" + "]"
					'''---------------------------'''
				elif "&youtube_id=" in x:
					x = x.replace("&youtube_id=","")
					x2 = space + "[" + "YouTube Video" + "]"
					'''---------------------------'''
				elif "&youtube_se=" in x:
					x = x.replace("&youtube_se=","")
					x2 = space + "[" + "YouTube Search" + "]"
					'''---------------------------'''
				elif "&custom8=" in x:
					x = x.replace("&custom8=","")
					x2 = space + "[" + "Add-on" + "]"
					'''---------------------------'''
				elif "&custom4=" in x:
					x = x.replace("&custom4=","")
					x2 = space + "[" + "Direct Video" + "]"
					'''---------------------------'''
				if x2 != "": message2 = message2 + '[CR]' + str(i) + space2 + str(x) + str(x2)
				'''---------------------------'''
			header = addonString_servicefeatherence(32434).encode('utf-8') + space2 + str(name)
			if message2 != "": message = message2 + '[CR][CR]' + addonString_servicefeatherence(32453).encode('utf-8')
			else: message = addonString_servicefeatherence(32454).encode('utf-8') #URL Error occured.
			diaogtextviewer(header,message)
			'''---------------------------'''
			
		elif "2" in printpoint or url == 'New':
			'''------------------------------
			---Add-URL-----------------------
			------------------------------'''
			list3 = ['-> (Exit)']
			list3.append(localize(413)) #Manual
			list3.append(localize(24000)) #Add-on
			list3.append('YouTube Video ID') #
			list3.append('YouTube Playlist ID') #
			list3.append('YouTube Channel ID') #
			list3.append('YouTube Search') #
			
			returned3, value = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list3,0)
			if returned3 == -1: printpoint = printpoint + "9"
			elif returned3 == 0: printpoint = printpoint + "8"
			else:
				printpoint = printpoint + "7" ; x = ""			
				if returned3 == 1: x = ""
				elif returned3 == 2: x = "&custom8="
				elif returned3 == 3: x = "&youtube_id="
				elif returned3 == 4: x = "&youtube_pl="
				elif returned3 == 5: x = "&youtube_ch="
				elif returned3 == 6: x = "&youtube_se="
				
				if returned3 == 1:
					New_ID = dialogkeyboard(x, value, 0, "1", "" , "")
				elif returned3 == 2:
					from modules import *
					setSkinSetting('0','actionTEMP',"",force=True)
					setSkinSetting('0','labelTEMP',"",force=True)
					setSkinSetting('0','iconTEMP',"",force=True)
					xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=232&value=TEMP)') ; xbmc.sleep(1000) ; mode232 = xbmc.getInfoLabel('Window(home).Property(mode232)')
					
					count = 0
					while count < 200 and mode232 != "" and not xbmc.abortRequested:
						xbmc.sleep(1000)
						mode232 = xbmc.getInfoLabel('Window(home).Property(mode232)')
						count += 1
					
					y = xbmc.getInfoLabel('Skin.String(actionTEMP)')
					y = y.replace(',returned',"")
					New_ID = x + y
				else:
					New_ID = dialogkeyboard(x, value, 0, "5", "" , "")
					
				if New_ID != 'skip' and New_ID != "":
					if url == 'New':
						labelTEMP = xbmc.getInfoLabel('Skin.String(labelTEMP)')
						if labelTEMP != "": labelx = labelTEMP
						else: labelx = addonString_servicefeatherence(32124).encode('utf-8')
						New_Name = dialogkeyboard(labelx, addonString_servicefeatherence(32110).encode('utf-8'), 0, "",Custom_Playlist_Name, "0")
						name = New_Name
						
						iconTEMP = xbmc.getInfoLabel('Skin.String(iconTEMP)')
						if iconTEMP != "":
							New_Thumb = iconTEMP
							setsetting(Custom_Playlist_Thumb, New_Thumb)
							
					setCustom_Playlist_ID(Custom_Playlist_ID, New_ID, mode, url, name, num, viewtype)
			
				
		elif "3" in printpoint:
			'''------------------------------
			---Remove-URL--------------------
			------------------------------'''
			list = ['-> (Exit)']
			url2 = url.split(',')
			i = 0
			for x in url2:
				i += 1
				if x == "" and ',,' in url:
					setsetting(Custom_Playlist_ID, url.replace(',,',""))
				else:
					list.append(x)

			returned2, value = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list,0)
				
			if returned2 == -1: printpoint = printpoint + "9"
			elif returned2 == 0: printpoint = printpoint + "8"
			else: printpoint = printpoint + "7"
			
			if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
				
				if i == 1:
					'''Warning 1 URL found!'''
					check = dialogyesno(localize(13336), addonString_servicefeatherence(32456).encode('utf-8') + '[CR]' + addonString_servicefeatherence(32455).encode('utf-8'))
					if check == "ok":
						'''Remove Button'''
						printpoint = printpoint + "F"
					else:
						'''Skip'''
				else:
					if value + "," in url:
						'''multi links'''
						value2 = url.replace(value + ",","",1)
					elif value in url:
						'''single link'''
						value2 = url.replace(value,"",1)
					else: value2 = ""
					if value2 == "": notification_common("17")
					else:
						setsetting(Custom_Playlist_ID, value2)
						notification(addonString_servicefeatherence(32436).encode('utf-8') + space + addonString_servicefeatherence(32435).encode('utf-8'),str(name), "", 4000) #URL Removed Succesfully!
						'''---------------------------'''
				
	elif "B" in printpoint:
		'''------------------------------
		---Rename-Button-----------------
		------------------------------'''
		New_Name = dialogkeyboard(name, addonString_servicefeatherence(32437).encode('utf-8'), 0, "", Custom_Playlist_Name, "0")
		if New_Name != "skip" and New_Name != name:
			notification(addonString_servicefeatherence(32110).encode('utf-8') + space + addonString_servicefeatherence(32421).encode('utf-8'), str(name), "", 4000) #Button Name Update Succesfully!
			'''---------------------------'''
		
	elif "C" in printpoint:
		if thumb == "":
			'''------------------------------
			---Add-Thumb---------------------
			------------------------------'''
			New_Thumb = ""
			returned = dialogyesno(str(name), addonString_servicefeatherence(32423).encode('utf-8'), nolabel=localize(20017), yeslabel=localize(20015))
			if returned == 'ok':
				'''remote'''
				x = localize(20015) #Remote thumb
				value = dialogkeyboard("", x + space + "URL", 0, "1", "", "")
				if value != "skip":
					returned = urlcheck(value, ping=False)
					if returned != "ok":
						notification(localize(2102, s=[addonString_servicefeatherence(32436).encode('utf-8')]), addonString_servicefeatherence(32801).encode('utf-8') + space + '..', "", 2000)
						header = localize(2102, s=[addonString_servicefeatherence(32436).encode('utf-8')]) #"URL Error"
						message = addonString_servicefeatherence(32802).encode('utf-8') + space2 + newline + '[B]' + str(value) + '[/B]'
						diaogtextviewer(header,message)
					else:
						New_Thumb = value
			else:
				'''local'''
				x = localize(20017) #Local thumb
				xbmc.executebuiltin('Skin.SetString('+addonID+'_Temp,)')
				xbmc.executebuiltin('Skin.SetImage('+addonID+'_Temp,)') ; xbmc.sleep(4000)
				dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
				while dialogfilebrowserW and not xbmc.abortRequested:
					xbmc.sleep(500)
					dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
					xbmc.sleep(500)
				xbmc.sleep(500)
				New_Thumb = xbmc.getInfoLabel('Skin.String('+addonID+'_Temp)')
			
			if New_Thumb != "":
				setsetting(Custom_Playlist_Thumb, New_Thumb)
				notification(str(x) + space + addonString_servicefeatherence(32421).encode('utf-8'), str(name), "", 4000) #Thumb* Update Succesfully!
				'''---------------------------'''
		else:
			'''------------------------------
			---Remove-Thumb------------------
			------------------------------'''
			if os.path.exists(thumb): x = localize(20017) #Local thumb
			else: x = localize(20015)
			setsetting(Custom_Playlist_Thumb, "")
			notification(str(x) + space + addonString_servicefeatherence(32435).encode('utf-8'), str(name), "", 2000) #Thumb* Removed Succesfully!
			'''---------------------------'''
			
	elif "D" in printpoint:
		'''------------------------------
		---Add-Description---------------
		------------------------------'''
		returned, value = getRandom("0", min=0, max=100, percent=50)
		if int(value) <= 10: notification("Tip New Line:", "[CR]", "", 4000)
		elif int(value) <= 20: notification("Tip Bold:", "[B]text[/B]", "", 4000)
		elif int(value) <= 30: notification("Tip Color:", "[COLOR=X]text[/COLOR]", "", 4000)
		elif int(value) <= 40: notification("Tip Italic:", "[I]text[/I]", "", 4000)
		
		if Custom_Playlist_Description == "": extra1 = addonString_servicefeatherence(32424).encode('utf-8') #Add Description
		else: extra1 = addonString_servicefeatherence(32425).encode('utf-8') #Edit Description
		
		returned = dialogkeyboard(desc, extra1, 0, "", Custom_Playlist_Description, "0")
		if returned != "skip":
			if returned == "": extra2 = addonString_servicefeatherence(32435).encode('utf-8') #Removed Succesfully!
			else: extra2 = addonString_servicefeatherence(32421).encode('utf-8') #Update Succesfully!
			if returned != desc: notification(localize(21821) + space + extra2, str(name), "", 4000) #Description Update/Removed Succesfully!
			'''---------------------------'''
	
	elif "E" in printpoint:
		
		if fanart == "":
			'''------------------------------
			---Add-Fanart----------------
			------------------------------'''
			New_Fanart = ""
			returned = dialogyesno(str(name), addonString_servicefeatherence(32423).encode('utf-8'), nolabel=localize(20438), yeslabel=localize(20441))
			if returned == 'ok':
				'''remote'''
				x = localize(20441) #Remote fanart
				value = dialogkeyboard("", localize(20441), 0, "1", "", "")
				if value != "skip":
					returned2 = urlcheck(value, ping=False)
					if returned2 != "ok":
						notification(localize(2102, s=[addonString_servicefeatherence(32436).encode('utf-8')]), addonString_servicefeatherence(32801).encode('utf-8') + space + '..', "", 2000)
						header = localize(2102, s=[addonString_servicefeatherence(32436).encode('utf-8')]) #"URL Error"
						message = addonString_servicefeatherence(32802).encode('utf-8') + space2 + newline + '[B]' + str(value) + '[/B]'
						diaogtextviewer(header,message)
					else:
						New_Fanart = value
			else:
				'''local'''
				x = localize(20438) #Local fanart
				xbmc.executebuiltin('Skin.SetString('+addonID+'_Temp,)')
				xbmc.executebuiltin('Skin.SetImage('+addonID+'_Temp,)') ; xbmc.sleep(4000)
				dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
				while dialogfilebrowserW and not xbmc.abortRequested:
					xbmc.sleep(500)
					dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
					xbmc.sleep(500)
				xbmc.sleep(500)
				New_Fanart = xbmc.getInfoLabel('Skin.String('+addonID+'_Temp)')
			
			if New_Fanart != "":
				setsetting(Custom_Playlist_Fanart, New_Fanart)
				 
				notification(str(x) + space + addonString_servicefeatherence(32421).encode('utf-8'), str(New_Fanart), "", 2000) #Fanart* Update Succesfully!
				xbmc.sleep(2000)
				if Fanart_Enable != "true": notification(addonString_servicefeatherence(32422).encode('utf-8') + space + localize(24023) + "!", "->" + localize(1045), "", 4000) # Allow Backgrounds disabled, ->Add-on settings
				elif Fanart_EnableCustom != "true": notification(localize(21389) + space + localize(24023) + "!", "->" + localize(1045), "", 4000) # Enable custom background disabled, ->Add-on settings
				'''---------------------------'''
		else:
			'''------------------------------
			---Remove-Fanart------------
			------------------------------'''
			setsetting(Custom_Playlist_Fanart, "")
			notification(localize(33068) + space + localize(19179) + "!", str(name), "", 4000) #Background Deleted!
			'''---------------------------'''
			
	if "F" in printpoint:
		if Custom_Playlist_Description != "":
			'''------------------------------
			---Remove-Button-----------------
			------------------------------'''
			returned = dialogyesno(localize(13336) + '[CR]' + str(name),localize(19194)) #Remove Button, Continue?
			if returned == "ok":
				setsetting(Custom_Playlist_ID, "")
				setsetting(Custom_Playlist_Name, "")
				setsetting(Custom_Playlist_Thumb, "")
				setsetting(Custom_Playlist_Description, "")
				setsetting(Custom_Playlist_Fanart, "")
				'''---------------------------'''
				if desc != "": extra1 = localize(21821) + space2 + str(desc)
				else: extra1 = ""
				dialogok(localize(50) + space + addonString_servicefeatherence(32435).encode('utf-8') + '[CR]' + str(name), "ID" + space2 + str(url), "", extra1)
				'''---------------------------'''
				
	if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
		update_view(url, num, viewtype, installaddon=False)
		#xbmcplugin.endOfDirectory(int(sys.argv[1]))
		
	text = "name" + space2 + str(name) + newline + \
	"Custom_Playlist_ID" + space2 + str(Custom_Playlist_ID) + newline + \
	"Custom_Playlist_Name" + space2 + str(Custom_Playlist_Name) + newline + \
	"Custom_Playlist_Thumb" + space2 + str(Custom_Playlist_Thumb) + newline + \
	"thumb" + space2 + str(thumb) + newline + \
	"Custom_Playlist_Description" + space2 + str(Custom_Playlist_Description) + newline + \
	"Custom_Playlist_Fanart" + space2 + str(Custom_Playlist_Fanart) + newline + \
	"fanart" + space2 + str(fanart) + newline + \
	"New_ID" + space2 + str(New_ID) + newline + \
	"num" + space2 + str(num) + newline + \
	"url" + space2 + str(url) + newline
	'''---------------------------'''
	printlog(title="ManageCustom", printpoint=printpoint, text=text, level=2, option="")

def RenameSubCustom(mode, name, url, thumb, desc, num, viewtype, fanart):
	'''------------------------------
	---Rename-Sub-Button-------------
	------------------------------'''
	extra = "" ; printpoint = "" ; New_ID = "" ; Current_ID = "" ; Current_ID_ = "" ; Current_Name = name ; Current_Name_ = name ; containerfolderpath = xbmc.getInfoLabel('Container.FolderPath') ; containerfolderpath_ = ""
	
	Custom_Playlist_ID = "Custom_Playlist" + num + "_ID"
	Custom_Playlist_ID_ = getsetting(Custom_Playlist_ID)
	Custom_Playlist_ID_L = Custom_Playlist_ID_.split(',')
	if Custom_Playlist_ID == "": notification(addonString_servicefeatherence(32145).encode('utf-8'), addonString_servicefeatherence(32101).encode('utf-8'), "", 2000) ; printpoint = printpoint + "9"
	
	#Custom_Playlist_Name = "Custom_Playlist" + num + "_Name"
	#Custom_Playlist_Thumb = "Custom_Playlist" + num + "_Thumb"
	#Custom_Playlist_Description = "Custom_Playlist" + num + "_Description"
	#Custom_Playlist_Fanart = "Custom_Playlist" + num + "_Fanart"
	
	
	for i in Custom_Playlist_ID_L:
		if url in i:
			printpoint = printpoint + '1'
			Current_ID = i
			Current_ID_ = Current_ID
			break
	if Current_ID == "":
		printpoint = printpoint + '2'
		notification('error!','','',2000)
	else:
		if '&name_=' in Current_ID:
			'''Remove previous name'''
			printpoint = printpoint + '3'
			Current_Name = find_string(Current_ID, '&name_=', "&")
			Current_Name_ = Current_Name.replace('&name_=',"")
			Current_Name_ = Current_Name_.replace('&',"")
			Current_ID_ = Current_ID.replace(Current_Name,"",1)
		
		New_Name = dialogkeyboard(Current_Name_, addonString_servicefeatherence(32437).encode('utf-8'), 0, "", "", "")
		
		if New_Name == "skip" and New_Name != Current_Name:
			printpoint = printpoint + '4'
			New_ID = Custom_Playlist_ID_.replace(Current_ID, Current_ID_ + '&name_='+New_Name + '&')
			setsetting_custom1(addonID, Custom_Playlist_ID, str(New_ID))
			notification(addonString_servicefeatherence(32110).encode('utf-8') + space + addonString_servicefeatherence(32421).encode('utf-8'), to_utf8(New_Name), "", 4000) #Button Name Update Succesfully!

			xbmc.executebuiltin('Action(Back)')
			#update_view(containerfolderpath_, num, viewtype, installaddon=False)
			'''---------------------------'''
		else:
			printpoint = printpoint + '9'
			#notification('error!','','',2000)
	
	text = 'New_Name' + space2 + str(New_Name) + newline + \
	'Custom_Playlist_ID' + space2 + str(Custom_Playlist_ID) + newline + \
	'Custom_Playlist_ID_' + space2 + str(Custom_Playlist_ID_) + newline + \
	'name' + space2 + str(name) + newline + \
	'Current_Name' + space2 + str(Current_Name) + newline + \
	'Current_Name_' + space2 + str(Current_Name_) + newline + \
	'url' + space2 + str(url) + newline + \
	'url[-1:]' + space2 + str(url[-1:]) + newline + \
	'Current_ID' + space2 + str(Current_ID) + newline + \
	'Current_ID_' + space2 + str(Current_ID_) + newline + \
	'New_ID' + space2 + str(New_ID) + newline
	printlog(title="RenameSubCustom", printpoint=printpoint, text=text, level=1, option="")
	
def getLists(mode, name, url, iconimage, desc, num, viewtype, fanart):
	'''Gather videos in Play Random'''
	count = 0
	setProperty('script.featherence.service_random', "true", type="home")
	xbmc.executebuiltin('Container.Refresh') ; xbmc.sleep(2000)
	dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
	while count < 20 and dialogbusyW and not xbmc.abortRequested:
		if count == 0: notification('Random-Play','.','',2000)
		elif count == 4: notification('Random-Play','..','',2000)
		elif count == 8: notification('Random-Play','...','',2000)
		xbmc.sleep(500)
		dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
		count += 1
	
	setProperty('script.featherence.service_random', "", type="home")
	xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=17&value='+addonID+')')
	
def listURLS(mode, name, url, iconimage, desc, num, viewtype, fanart):
	try: page  = int(num)
	except: page = 1
	
	listURLS_(mode, name, url, iconimage, desc, page, viewtype, fanart)
	
def CATEGORIES_RANDOM(background="", default="", custom=""):
	'''אקראי'''
	addDir('-' + localize(590),list,1,featherenceserviceicons_path + 'random.png',addonString_servicefeatherence(32413).encode('utf-8'),'1',0,getAddonFanart(background, default=default, custom=custom))

def CATEGORIES_SEARCH(mode=3, name='-' + localize(137), url="", num=""):
	'''חיפוש'''
	printpoint = "" ; infile_ = ""
	if Search_History == 'true' and os.path.exists(Search_History_file) and mode == 30:
		infile_ = read_from_file(Search_History_file, silent=True, lines=True, retry=True, createlist=True, printpoint="", addlines="")
		if infile_ != "" and infile_ != []: pass
		else: mode = 3
	else: mode = 3
	addDir(name,url,mode,featherenceserviceicons_path + 'se.png',localize(137) + space + 'YouTube',num,"", getAddonFanart("", custom="", urlcheck_=True))
	
	text = 'mode' + space2 + str(mode) + newline + \
	'infile_' + space2 + str(infile_)
	printlog(title="CATEGORIES_SEARCH", printpoint=printpoint, text=text, level=0, option="")
	
def CATEGORIES_SEARCH2(mode, name, url, iconimage, desc, num, viewtype, fanart):
	'''רשימת חיפוש'''
	CATEGORIES_SEARCH()
	infile_ = read_from_file(Search_History_file, silent=True, lines=True, retry=True, createlist=True, printpoint="", addlines="")
	for x in infile_:
		CATEGORIES_SEARCH(url=str(x), name=str(x), num='Custom')

def Search_Menu(mode, name, url, iconimage, desc, num, viewtype, fanart):
	if num == 'Delete':
		replace_word(Search_History_file, url, "", infile_="", LineR=False , LineClean=False)
	elif num == 'Delete All':
		removefiles(Search_History_file)
	xbmc.sleep(500) ; xbmc.executebuiltin('Container.Refresh')

def MyFavourites(mode, name, url, iconimage, desc, num, viewtype, fanart):
	pass
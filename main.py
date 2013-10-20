# -*- coding: <utf-8>-*-
import win32clipboard
import win32con
import sys,time,os, urllib, urllib2
from urllib2 import URLError

server = 'http://copysync-cytangah.rhcloud.com/update'
local_server = "http://localhost:8000/update"
local_testing = False

def onClipTextChanged(data):
	print "TextChanged :", data
	print "Posting to server..."
	data = unicode(data.decode('big5'))
	data = data.encode('utf-8')
	post_data = [('data', data)]
	post_data = urllib.urlencode(post_data)
	if local_testing:
		request = urllib2.Request(local_server, post_data)
	else:
		request = urllib2.Request(server, post_data)

	request.add_header("Content-type", "application/x-www-form-urlencoded")
	try:
		page = urllib2.urlopen(request).read()
	except(URLError):
		print "Error : Server disconnected"
		return
	print "Result :",page
	print ""

if __name__ == "__main__":
	cliptext = ''
	new_cliptext = ''
	while(True):
		win32clipboard.OpenClipboard()
		try:
			new_cliptext = win32clipboard.GetClipboardData(win32con.CF_TEXT)
			#print new_cliptext
		except(TypeError):
			print "TypeError"
			#reset the clipboard to previous valid result
			new_cliptext = cliptext
			win32clipboard.SetClipboardData(win32con.CF_TEXT, cliptext)

		win32clipboard.CloseClipboard()
		if new_cliptext != cliptext:
			cliptext = new_cliptext
			onClipTextChanged(data=cliptext)
		time.sleep(1.5)



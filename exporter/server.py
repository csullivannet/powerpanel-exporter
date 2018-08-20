#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep, chdir, path
from sultan.api import Sultan
import re
import json

PORT_NUMBER = 8080

# Set working dir
abspath = path.abspath(__file__)
dname = path.dirname(abspath)
chdir(dname)

class handler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		if self.path=="/":
			self.path="/index.html"

		if self.path=="/metrics":
			
			# TODO - don't write to file
			# There's probably a better way to do this than writing to file,
			# then reading from that file, but Sultan outputting to STDOUT
			# currently outputs every character on a newline 
			with Sultan.load() as s:
			    s.sh("-c 'pwrstat -status'").redirect(
			     "pwrstats.txt",
			    append=False,
			    stdout=True,
			    stderr=False).run()

			# stats.json defines what outputs we are looking for from pwrstat
			with open('stats.json') as f:
				stats = json.load(f)

			with open ("pwrstats.txt", "r") as f:
			    for line in f:
			        for i in stats:
			            if re.findall(r'' + i['search'] + '', line):
			                if i['end']:
			                    end = int(i['end'])
			                else:
			                    end = None
			                i['stat'] = line[32:end].rstrip()

			with open ("metrics", "w") as f:
				for i in stats:
					# Reassign string values to booleans
					if i is 'power_supply':
						if i['stat'] is 'power_supply':
							i['stat'] = '0'
						else:
							i['stat'] = '1'
					f.write(i['help'] + '\n')
					f.write(i['type'] + '\n')
					f.write(i['metric'] + ' ' + i['stat'] + '\n')

		try:
			#Check the file extension required and
			#set the right mime type
			mimetype='text/html'

			#Open the static file requested and send it
			f = open(curdir + sep + self.path) 
			self.send_response(200)
			self.send_header('Content-type',mimetype)
			self.end_headers()
			self.wfile.write(f.read())
			f.close()

			return

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), handler)
	print 'Started httpserver on port ' , PORT_NUMBER

	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
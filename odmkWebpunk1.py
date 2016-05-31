# -*- coding: utf-8 -*-
# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header begin-----------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************
#
# __::((odmkWebpunk1.py))::__
#
# Experiments with HTTP and web services
# based on diveintopython3
#
# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header end-------------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************

import urllib.request
import httplib2

from odmkClear import *

# // *---------------------------------------------------------------------* //
clear_all()

print('// *--------------------------------------------------------------* //')
print('// *---::HTTP and web services exp::---*')
print('// *--------------------------------------------------------------* //')

print('\nurllib2 exp:')

proxy_info = {
    'user': 'NMCORP\FCT00110',
    'pass': 'barutan777Seijin',
    'host': "10.31.81.9",
    'port': 80}

proxy_support = urllib.request.ProxyHandler({"http": "http://%(user)s:%(pass)s@%(host)s@:%(port)d" % proxy_info})

opener = urllib.request.build_opener(proxy_support, urllib.request.HTTPHandler)

# Install the opener
urllib.request.install_opener(opener)

# Open the url

f = urllib.request.urlopen('http://www.python.org/')

print(f.headers)
print(f.read())



print('\n')
print('// *--------------------------------------------------------------* //')

# // *---------------------------------------------------------------------* //
# // *---------------------------------------------------------------------* //

#print('\nhttplib2 exp:')
#
#h = httplib2.Http('.cache')
#
##http = httplib2.Http(proxy_info.ProxyInfo(socks.PROXY_TYPE_HTTP, <proxy host address>, 8080, 
##                                          <proxy user id>, proxy_pass = <proxy password>))
#
#
#http = httplib2.Http(proxy_info.ProxyInfo(socks.PROXY_TYPE_HTTP, 'http://proxy.nml.jdc/proxy/proxy.pac'))
#
#NMCorp.Nissan.Biz
#
## http://proxy.nml.jdc/proxy/proxy.pac
#
#
#
#response, content = h.request('http://diveintopython3.org/examples/feed.xml')
#
#response.status
#
#
#print('\n')
#print('// *--------------------------------------------------------------* //')

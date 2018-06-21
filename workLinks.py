# myLinks
#
# byHaxxis

import webbrowser
from webbrowser import open_new_tab

# Store links in dictionary
wrkLinks = {
    'tcard': 'https://landing.paychex.com/ssologin/Login.aspx',
    'box': 'https://cisco.app.box.com/',
    'docs': 'https://docs.cisco.com/share/s/h0NwTDK2Tr2Ma1Pml7JqDg',
    'dcp': 'https://dcp.cisco.com/dcpplat/dcp/landing#/timeentryMgmt',
    'email': 'email: https://mail.cisco.com/owa/'
}

usrInput = input('Where to? ')

for link, urls in wrkLinks.items():
    if usrInput == link:
        webbrowser.open_new_tab(wrkLinks[link])
    if usrInput == '?':
        print(link)

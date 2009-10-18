#
# Makefile for FireFoxPersonal profile application
#
# Require py2app:
# http://svn.pythonmac.org/py2app/py2app/trunk/doc/index.html
#
# $Id: Makefile 11 2008-09-23 20:02:44Z vwelch $

APP_SCRIPTS = $(wildcard *.py)
APPS=$(APP_SCRIPTS:.py=.app)

default: apps

apps: $(APPS)

FireFoxDefault.app: FireFoxDefault.py Firefox.icns 
	py2applet $^

FireFoxPersonal.app: FireFoxPersonal.py Firefox.icns 
	py2applet $^

FireFoxProfileManager.app: FireFoxProfileManager.py Firefox.icns 
	py2applet $^

GnuClient.app: GnuClient.py gnu.icns
	py2applet $^

KindleSync.app: KindleSync.py
	py2applet $^

VMWareConsole.app: VMWareConsole.py vmware-icon.icns
	py2applet $^

install: apps
	@for app in $(APPS); do \
		echo Installing $${app}... ;\
		if test -d $${app} ; then \
			installedApp=/Applications/$${app} ;\
			rm -rf $${installedApp} ;\
			mv $${app} $${installedApp} ;\
		fi ;\
	done

clean::
	rm -rf $(APPS)

.phony: default app install clean


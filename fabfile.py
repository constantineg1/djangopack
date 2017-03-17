from fabric.api import local


def test():
	""" Running all tests """
	local('./runtests')
 

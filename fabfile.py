from fabric.api import local


def test():
	""" Running all tests """
	local('virtualenv -p /usr/local/lib/python2.7.9/bin/python .env')
	local('./.env/bin/pip install -r requirements.txt')
	local('./.env/bin/python thestackserver/manage.py test --noinput')
 

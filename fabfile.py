# fabfile.py for pruthvi_dot_me digital ocean website

from fabric.api import *

# env variables
env.user = '$user'
env.path = '/home/django'

# list of hosts
webserver = '127.0.0.1:8000'
env.hosts = [webserver, '45.55.84.69']
env.skip_bad_hosts = True
env.password = '$password'

# dictionary of servers as roles
env.roledefs = {
    'local':[webserver],
    'remote':['45.55.84.69']
    }

@roles('remote')
def uptime():
    run('uptime')

# deploy development code from Git
@roles('remote')
def deploy(directory="pruthvi_dot_me"):
    with cd(env.path):
        # delete directory if exists
        if directory is not None:
            run("rm -rf %s" % directory)
        # force clone
        run("git clone --branch digital_ocean_site https://github.com/pruthvidesai/Pruthvi.me.git %s" % directory)
        # restart nginx and gunicorn
        run("service gunicorn restart")
        run("service nginx restart")
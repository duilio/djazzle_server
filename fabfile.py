from fabric.api import env
env.use_ssh_config = True
env.hosts = ['djazzle']

from fabric.api import sudo, cd, run


def deploy(branch='master'):
    with cd('djazzle'):
        run('git fetch')
        run('git checkout -f %s' % branch)
        run('git merge origin/%s' % branch)
        sudo('pip install -r requirements.txt')
        run('./manage.py syncdb --noinput')
        # TODO: collectstatic

    # TODO: restart service

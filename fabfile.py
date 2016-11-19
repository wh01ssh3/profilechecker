from fabric.api import local


def startapp():
    """Create app from cookiecutter template"""
    local('cookiecutter https://github.com/singleton11/sdjat -o apps')


def startdb():
    """Up postgres docker container"""
    local('docker-compose up postgres')


def compiledeps(env='local'):
    """Compile *.in files into requirements.txt"""
    local('pip-compile --output-file requirements/{env}.txt '
          'requirements/common.in requirements/{env}.in'.format(env=env))


def sync(env='local'):
    """Compile *.in files into requirements.txt"""
    local('pip-sync requirements/{env}.txt'.format(env=env))


def coverage():
    """Open test coverage in browser"""
    local('coverage run manage.py test --keepdb --failfast')
    local('coverage html')
    local('xdg-open htmlcov/index.html & sleep 3')

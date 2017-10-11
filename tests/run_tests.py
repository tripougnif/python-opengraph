from os.path import abspath, dirname

import nose


def all():
    argv = ['nosetests', '--verbose', '--logging-level=ERROR']
    nose.run_exit(argv=argv, defaultTest=abspath(dirname(__file__)))

if __name__ == '__main__':
    all()

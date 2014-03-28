#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Just an example.
"""

import os
import sys


# PYTHON PATH MANAGEMENT
DIRNAME = os.path.dirname(__file__)
if DIRNAME == '':
    DIRNAME = '.'

DIRNAME = os.path.realpath(DIRNAME)
UPDIR   = os.path.split(DIRNAME)[0]

if UPDIR not in sys.path:
    sys.path.append(UPDIR)


from daemonify import Daemon


class ExampleDaemon(Daemon):
    """
    Inherits from Daemon.
    """
    def run(self):
        """Overriding run.
        """
        import time
        while True:
            time.sleep(1)

def main():
    """Main."""

    daemon = ExampleDaemon('/tmp/example-daemon.pid')

    if len(sys.argv) != 2:
        print "Usage: %s {start|stop|restart|status|foreground}" % sys.argv[0]
        sys.exit(2)

    if 'start' == sys.argv[1]:
        daemon.start()

    elif 'stop' == sys.argv[1]:
        daemon.stop()

    elif 'restart' == sys.argv[1]:
        daemon.restart()

    elif 'status' == sys.argv[1]:
        daemon.status()

    elif 'foreground' == sys.argv[1]:
        daemon.debug()

    else:
        print "Unknown command \"%s\"" % sys.argv[1]
        print "Usage: %s {start|stop|restart|status}" % sys.argv[0]
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":

    main()


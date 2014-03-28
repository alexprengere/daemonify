Daemonify
=========

Daemonify a Python script.

Example
-------

Just import the Daemon class and subclass it, overriding the *run* method.

.. code-block:: python

    from daemonify import Daemon

    class ExampleDaemon(Daemon):
        def run(self):
            import time
            while True:
                time.sleep(1)

    daemon = ExampleDaemon('/tmp/example-daemon.pid')
    daemon.start() # Daemon is running!

    # This can be called from another instance, as long
    # as the same pidfile is given at init.
    daemon.stop()


With the example:

.. code-block:: bash

 $ python examples/daemon_example.py start
 $ python examples/daemon_example.py stop


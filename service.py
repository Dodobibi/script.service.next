import xbmc

from resources.lib.monitor import NextMonitor


class NextService(object):

    def __init__(self):
        self.xbmc_monitor = xbmc.Monitor()
        self.next_monitor = NextMonitor()

    def run(self):
        while not self.xbmc_monitor.waitForAbort(1):
            self.next_monitor.run()
        pass


if __name__ == '__main__':
    import pydevd
    # pydevd.settrace('localhost', port=5555, stdoutToServer=True, stderrToServer=True)
    # NextService().run()

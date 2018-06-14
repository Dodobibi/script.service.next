import xbmc
import AddonSignals
from xbmcaddon import Addon


class NextMonitor(xbmc.Player):

    def __init__(self):
        super(NextMonitor, self).__init__()
        self.addon = Addon()
        self._skips = []
        self._next = None
        self._registering()

    def _registering(self):
        addon_name = self.addon.getAddonInfo('name')
        AddonSignals.registerSlot(addon_name, 'add_skip', self._skips.append)
        AddonSignals.registerSlot(addon_name, 'set_next', self.set_next)

    def set_next(self, _next):
        self._next = _next

    def onPlayBackStarted(self):
        pass

    def onPlayBackPaused(self):
        pass

    def onPlayBackResumed(self):
        pass

    def onPlayBackSeek(self, time, seekOffset):
        pass

    def onPlayBackSeekChapter(self, chapter):
        pass

    def onPlayBackSpeedChanged(self, speed):
        pass

    def onPlayBackStopped(self):
        pass

    def onPlayBackEnded(self):
        pass

    def onPlayBackError(self):
        pass

    def onQueueNextItem(self):
        pass

    def run(self):
        pass

    def check_skips(self):
        if self.isPlayingVideo():
            for skip in self._skips:
                skip_start = skip.get('start', 0)
                skip_end = skip.get('end', 0)
                playTime = self.getTime()
                if playTime > skip_start and playTime < skip_end:
                    pass




    def check_next(self):
        pass

from enigma import eHbbtv
from Source import Source
from Components.Element import cached

class HbbtvApplication(Source):

    def __init__(self):
        Source.__init__(self)
        self._available = False
        self._appname = ''
        eHbbtv.getInstance().redButtonAppplicationReady.get().append(self._redButtonApplicationReady)
        eHbbtv.getInstance().aitInvalidated.get().append(self._aitInvalidated)

    def _redButtonApplicationReady(self, appid):
        app = eHbbtv.getInstance().getApplication(appid)
        if app.isValid():
            self._available = True
            self._appname = app.getName()
            self.changed((self.CHANGED_ALL,))
        else:
            self._aitInvalidated()

    def _aitInvalidated(self):
        self._available = False
        self._appname = ''
        self.changed((self.CHANGED_ALL,))

    def destroy(self):
        eHbbtv.getInstance().redButtonAppplicationReady.get().remove(self._redButtonApplicationReady)
        eHbbtv.getInstance().aitInvalidated.get().remove(self._aitInvalidated)
        Source.destroy(self)

    @cached
    def getBoolean(self):
        return self._available

    boolean = property(getBoolean)

    @cached
    def getName(self):
        return self._appname

    name = property(getName)

from Source import Source
from Components.Element import cached
from enigma import eTimer

class Boolean(Source, object):

    def __init__(self, fixed = False, function = None, destroy = None, poll = 0):
        Source.__init__(self)
        self.function = function
        self.fixed = fixed
        self.post_destroy = destroy
        if poll > 0:
            self.poll_timer = eTimer()
            self.poll_timer.callback.append(self.poll)
            self.poll_timer.start(poll)
        else:
            self.poll_timer = None
        return

    @cached
    def getBoolean(self):
        if self.function is not None:
            return self.function()
        else:
            return self.fixed
            return

    def setBoolean(self, value):
        self.fixed = value
        self.poll()

    boolean = property(getBoolean, setBoolean)

    def poll(self):
        self.changed((self.CHANGED_ALL,))

    def destroy(self):
        try:
          if self.poll_timer:
            self.poll_timer.callback.remove(self.poll)
          if self.post_destroy is not None:
            self.fixed = self.post_destroy
            self.poll()            
            
            
        except:
         pass    

        Source.destroy(self)
        return
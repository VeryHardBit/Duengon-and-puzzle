from .__init__helper import *

class Wall(CommonObject):
    def __init__(self,data):
        CommonObject.__init__(self)
        data.setdefault('pos',[None,None])
        self.taken_positions=[data['pos']]
        self.holder=data['world']
    @property
    def display_prefix(self):
        return '|'

class Rotor:
    def __init__(self,rotor):
        self.rotor = rotor
        print('rotor has been created')
class Machine(Rotor):
    def __init__(self,enchiper):
        self.enchiper = enchiper
        Rotor.__init__(self,rotor='asd')
        print('inheritance used successfully ')
Rotor('asd')
Machine('asd')
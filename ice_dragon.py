from dragon import Dragon

#child class from dragon, inherits cow and dragon methods
class IceDragon(Dragon):
    def __init__(self, name, image):
        super().__init__(name, image)

    def can_breathe_fire():
        return False
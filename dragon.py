from cow import Cow

#child class from cow, inherits set image method
class Dragon(Cow):
    def __init__(self, name, image=None):
        super().__init__(name)
        self.set_image(image)
        

    def can_breathe_fire():
        return True
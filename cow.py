#creates cow objects with name and image attributes
class Cow:
    def __init__(self,name,image=None):
        self.name = name
        self.image = None

    def get_name(self):
        return self.name

    def get_image(self):
        return self.image

    def set_image(self,image):
        self.image = image






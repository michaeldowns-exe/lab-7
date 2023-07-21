from cow import Cow
class FileCow(Cow):
    def __init__(self, name, filename):
        super().__init__(name)

        try:
            with open(filename, 'rb') as f:
                self.image = f.read()
        except:
            raise RuntimeError("MOOOOO!!!!!!")

    def set_image(self, image):
        raise RuntimeError("Cannot reset FileCow Image")
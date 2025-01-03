class watch:
    @staticmethod
    def showtime():
        print("watch it show the time----!")
    @classmethod
    def showbrand(self):
        print("watch brand is rolex-----!") 
    def __init__(self,color):
        print("object is created--------!")
        self.color=color
    def get_color(self):
        print(self.color)
w1=watch("silver")
watch.showtime()
watch.showbrand
w1.get_color()
w1.showtime()                   
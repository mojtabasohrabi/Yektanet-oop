class BaseAdvertising(object):

    def __init__(self):
        self.__clicks = 0
        self.__views = 0

    def describe_me(self):
        print("BaseAdvertising desc")

    def inc_clicks(self):
        self.__clicks = self.__clicks + 1

    def inc_views(self):
        self.__views = self.__views + 1

    def get_clicks(self):
        print(self.__clicks)

    def get_views(self):
        print(self.__views)

from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    __clicks = 0
    __views = 0
    exists_ids = []

    def __init__(self, id, name):
        if id not in self.exists_ids:
            self.exists_ids.append(id)
        else:
            print("Advertiser id most be unique")
            quit()
        super().__init__()
        self.__id = id
        self.__name = name

    def get_name(self):
        print(self.__name)

    def set_name(self, new_name):
        self.__name = new_name

    @staticmethod
    def help():
        print("Advertiser help")

    @staticmethod
    def get_total_clicks():
        print(Advertiser.__clicks)

    def inc_clicks(self):
        super(Advertiser, self).inc_clicks()
        Advertiser.__clicks += 1

    def inc_views(self):
        super(Advertiser, self).inc_views()
        Advertiser.__views += 1

    def describe_me(self):
        print('Advertiser desc')

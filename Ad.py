from BaseAdvertising import BaseAdvertising


class Ad(BaseAdvertising):
    __clicks = 0
    __views = 0
    exists_ids = []

    def __init__(self, id, title, img_url, link, advertiser):
        if id not in self.exists_ids:
            self.exists_ids.append(id)
        else:
            print("Ad id most be unique")
            quit()
        super().__init__()
        self.__id = id
        self.__title = title
        self.__img_url = img_url
        self.__link = link
        self.__advertiser = advertiser

    def get_title(self):
        print(self.__title)

    def set_title(self, new_title):
        self.__title = new_title

    def get_img_url(self):
        print(self.__img_url)

    def set_img_url(self, new_img_url):
        self.__img_url = new_img_url

    def get_link(self):
        print(self.__link)

    def set_link(self, new_link):
        self.__link = new_link

    def describe_me(self):
        print('Ad desc')

    def inc_clicks(self):
        super(Ad, self).inc_clicks()
        self.__clicks += 1
        self.__advertiser.inc_clicks()

    def inc_views(self):
        super(Ad, self).inc_views()
        self.__views += 1
        self.__advertiser.inc_views()

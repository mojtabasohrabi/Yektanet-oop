from Ad import Ad
from Advertiser import Advertiser
from BaseAdvertising import BaseAdvertising

baseAdvertising = BaseAdvertising()

advertiser1 = Advertiser(1, "name1")
advertiser2 = Advertiser(2, "name2")
# advertiser2 = Advertiser(2, "name2") #repeated advertiser id

ad1 = Ad(1, "title1", "img-url1", "link1", advertiser1)
ad2 = Ad(2, "title2", "img-url2", "link2", advertiser2)
# ad2 = Ad(2, "title2", "img-url2", "link2", advertiser2)  #repeated Ad id


baseAdvertising.describe_me()
ad2.describe_me()
advertiser1.describe_me()
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad2.inc_views()
ad1.inc_clicks()
ad1.inc_clicks()
ad2.inc_clicks()
advertiser2.get_name()
advertiser2.set_name("new name")
advertiser2.get_name()
ad1.get_clicks()
advertiser2.get_clicks()
Advertiser.get_total_clicks()
Advertiser.help()



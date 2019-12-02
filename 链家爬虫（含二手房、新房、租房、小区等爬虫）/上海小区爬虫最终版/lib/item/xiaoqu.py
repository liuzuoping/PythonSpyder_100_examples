

class XiaoQu(object):
    def __init__(self, district, area, name, price, on_sale, link,niandai,leixing,wuyefei,wuyegs,kaifashang,loushu,wushu):
        self.district = district
        self.area = area
        self.price = price
        self.name = name
        self.on_sale = on_sale
        self.link=link
        self.niandai=niandai
        self.leixing=leixing
        self.wuyefei=wuyefei
        self.loushu=loushu
        self.wushu=wushu

    def text(self):
        return self.district + "," + \
                self.area + "," + \
                self.name + "," + \
                self.price + "," + \
                self.on_sale + "," + \
                self.link + "," + \
                self.niandai + "," + \
                self.leixing + "," + \
                self.wuyefei + "," + \
                self.loushu + "," + \
                self.wushu
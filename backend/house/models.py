from django.db import models


# Create your models here.
class House(models.Model):
    id = models.CharField(max_length=10, primary_key=True, help_text="591房屋id")
    cluster_id = models.IntegerField(help_text="建物群集")
    title = models.CharField(max_length=30, null=True, help_text="591房屋標題")
    shape_name = models.CharField(max_length=10, help_text="建物型態")
    region_name = models.CharField(max_length=3, help_text="縣市")
    section_name = models.CharField(max_length=10, help_text="區")
    address = models.CharField(max_length=30, help_text="地址")
    location = models.URLField(help_text="google map iframe url")
    price = models.FloatField(help_text="總價")
    unit_price = models.FloatField(help_text="單價")
    rooms = models.CharField(max_length=10, help_text="格局房數")
    age = models.IntegerField(help_text="屋齡")
    floor = models.CharField(max_length=10, help_text="樓層")
    area = models.FloatField(help_text="總面積")
    main_area = models.FloatField(help_text="主建坪")
    community_id = models.CharField(max_length=10,
                                    null=True,
                                    help_text="591社區id")
    tag = models.CharField(max_length=30, null=True, help_text="備註")

    def __str__(self):
        return f"{self.cluster_id}_{self.id}"

    def get_basic_info(self):
        return {
            "houseid": self.id,
            "cluster_id": self.cluster_id,
            "region_name": self.region_name,
            "section_name": self.section_name,
            "address": self.address,
            "price": self.price,
            "room": self.rooms,
            "area": self.area,
            "floor": self.floor,
            "houseage": self.age,
            "community_link": self.community_id
        }


class HouseImg(models.Model):
    house_id = models.CharField(max_length=10, help_text="591房屋id")
    img_url = models.CharField(max_length=1000, help_text="圖片連結")


class Community(models.Model):
    id = models.CharField(max_length=10, primary_key=True, help_text="591社區id")
    name = models.CharField(max_length=30, null=True, help_text="社區名稱")

    def __str__(self):
        return self.id


class Preference(models.Model):
    cluster_id = models.IntegerField(primary_key=True, help_text="建物群集")
    preference_point = models.IntegerField(default=0, help_text="喜好程度")

    def __str__(self):
        return self.cluster_id

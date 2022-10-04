from django.db import models


# Create your models here.
class House(models.Model):
    id = models.CharField(max_length=10, primary_key=True, help_text="591房屋id")
    cluster_id = models.IntegerField()
    shape_name = models.CharField(max_length=10, help_text="建物型態")
    region_name = models.CharField(max_length=3, help_text="縣市")
    section_name = models.CharField(max_length=10, help_text="區")
    address = models.CharField(max_length=30, help_text="地址")
    location = models.URLField(help_text="google map iframe url")
    price = models.FloatField(help_text="總價")
    unit_price = models.FloatField(help_text="單價")
    rooms = models.IntegerField(help_text="格局房數")
    age = models.IntegerField(help_text="屋齡")
    floor = models.CharField(max_length=10, help_text="樓層")
    area = models.FloatField(help_text="總面積")
    main_area = models.FloatField(help_text="主建坪")
    community_id = models.CharField(max_length=10,
                                    null=True,
                                    help_text="591社區id")
    tag = models.CharField(max_length=30, null=True, help_text="備註")

    def __str__(self):
        return f"{self.cluster_id}_{self.id_}"

    def get_basic_info(self):
        return {
            "id_": self.id_,
            "cluster_id": self.cluster_id,
            "region": f"{self.region_name}{self.section_name}",
            "price": self.price,
            "rooms": self.rooms,
            "area": self.area,
            "floor": self.floor,
            "age": self.age,
            "community": self.community_id
        }


class Community(models.Model):
    id = models.CharField(max_length=10, primary_key=True, help_text="591社區id")
    community_name = models.CharField(max_length=30,
                                      null=True,
                                      help_text="社區名稱")

    def __str__(self):
        return self.id_

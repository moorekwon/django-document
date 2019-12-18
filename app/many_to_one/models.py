from django.db import models


class Manufacturer(models.Model):
    name = models.CharField('제조사명', max_length=20)

    def __str__(self):
        return self.name


class Car(models.Model):
    # ForeignKeyㄹ르 선언한 모델은 Many-to-one에서의 'one'에 해당
    # 여러 개의 Car는 하나의 Manufacturer에 연결될 수 있음
    # Car 하나는 하나의 Manufacturer밖에 갖지 못함
    # 반대로 Many에 해당하는 Manufacturer는 자신에게 연결된 Car를 개수 제한없이 갖리 수 있음
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField('차량명', max_length=100)

    def __str__(self):
        return self.name

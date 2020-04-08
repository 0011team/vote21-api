from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=20, verbose_name="지역구 이름")
    count = models.PositiveIntegerField(verbose_name='정적수', default=1)
    state_name = models.CharField(max_length=20, verbose_name="지역구 행정구역 명")
    active_21 = models.BooleanField(_("Is 21 district"), default=False)
    active_20 = models.BooleanField(_("Is 20 district"), default=False)
    active_19 = models.BooleanField(_("Is 19 district"), default=False)

    class Meta:
        verbose_name = verbose_name_plural = '지역구'

    def __str__(self):
        return f"[{self.name}]"

class City(models.Model):
    province = models.CharField(max_length=20, verbose_name="시군구이름", blank=True)
    town = ArrayField(base_field=models.CharField(verbose_name='읍면동명', max_length=255), default=list)
    state = models.CharField(max_length=20, verbose_name="지역 이름")
    district = models.ForeignKey(verbose_name='지역구', 
        to=District, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        default=None
    ) # 비례인 경우 없음
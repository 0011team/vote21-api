from django.db import models
from district.models import District
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.
class ActiveLawMaker(models.Model):
    assembly_id = models.CharField(
        max_length=10,
        choices=(
            ("19", "19대"),
            ("20", "20대")
        )
    )    
    vote_count = models.CharField(max_length=30, verbose_name="득표수", blank=True)
    proposer_bill = ArrayField(
        models.CharField(max_length=20, blank=True, default=[])
    )
    approval_bill = ArrayField(
        models.CharField(max_length=20, blank=True, default=[])
    )
    representative_bill = ArrayField(
        models.CharField(max_length=20, blank=True, default=[])
    )
    representative_approval_bill = ArrayField(
        models.CharField(max_length=20, blank=True, default=[])
    )
    property = models.CharField(max_length=12, verbose_name="재산", blank=True)
    attend_rate = models.CharField(max_length=8, verbose_name="출석률", blank=True)
    committee_attend_info = JSONField(max_length=8, verbose_name="위원회 출석정보", blank=True, null=True)
    peoplepower21_url = models.CharField(max_length=100, verbose_name="재산", blank=True)
    ranking = JSONField(verbose_name="랭킹", blank=True, null=True)

    analysis_info = JSONField(verbose_name="대표발의 법안분석", blank=True, null=True)
    # major_bill_info = JSONField(verbose_name="주요법안 찬반투표", blank=True, null=True)
    major_bill = ArrayField(
        JSONField()
    )
    
    # # 발이의안 정보는 여기 
    # def __str__(self):
    #     return f"[{self.name}]"
        
class Person(models.Model):
    
    name = models.CharField(max_length=20, verbose_name="이름")
    name_en = models.CharField(max_length=20, verbose_name="영어 이름", blank=True)
    name_cn = models.CharField(max_length=20, verbose_name="한자 이름", blank=True)

    gender = models.CharField(
        max_length=10,
        choices=(
            ("m", "남성"),
            ("f", "여성"),
            ("n", "중성"),
            ("x", "표기안함"),
        )
    )

    party = models.CharField(max_length=10, verbose_name="정당", blank=True)
    birthday = models.CharField(max_length=30, blank=True)
    education = models.TextField(verbose_name='학력정보', blank=True)
    address = models.CharField(max_length=255, verbose_name="주소", blank=True)
    career = models.CharField(max_length=255, verbose_name="커리어", blank=True)
    image = models.FileField(verbose_name='이미지 파일', null=True, blank=True, upload_to='person/')
    image_url = models.CharField(max_length=255, verbose_name='이미지 url', null=True, blank=True)
    job = models.CharField(max_length=30, verbose_name="직업", blank=True)
    
    twitter = models.CharField(max_length=50, blank=True) 
    facebook = models.CharField(max_length=50, blank=True) 
    blog = models.CharField(max_length=255, blank=True) 
    page = models.CharField(max_length=255, blank=True) 

    wiki = models.TextField(verbose_name='추가 정보', blank=True)
    extra_info = models.TextField(verbose_name='추가 정보', blank=True)
    
    type = models.CharField(
        max_length=10,
        choices=(
            ("R", "비례"),
            ("D", "지역구"),
        )
    )

    district = models.ForeignKey(verbose_name='지역구', 
        to=District, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        default=None
    ) 
    
    active = models.ForeignKey(verbose_name='현역의원', 
        to=ActiveLawMaker, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        default=None
    ) # 현역인 경우에만 연결


    class Meta:
        verbose_name = verbose_name_plural = '지역구'

    def __str__(self):
        return f"[{self.name}]"



class Candidacy(models.Model):    
    name = models.CharField(max_length=20, verbose_name="이름")
    name_en = models.CharField(max_length=20, verbose_name="영어 이름", blank=True)
    name_cn = models.CharField(max_length=20, verbose_name="한자 이름", blank=True)

    gender = models.CharField(
        max_length=10,
        choices=(
            ("m", "남성"),
            ("f", "여성"),
            ("n", "중성"),
            ("x", "표기안함"),
        )
    )

    party = models.CharField(max_length=10, verbose_name="정당", blank=True)
    birthday = models.CharField(max_length=30, blank=True)
    education = models.TextField(verbose_name='학력정보', blank=True)
    address = models.CharField(max_length=255, verbose_name="주소", blank=True)
    career = models.CharField(max_length=255, verbose_name="커리어", blank=True)
    image = models.FileField(verbose_name='이미지 파일', null=True, blank=True, upload_to='person/')
    image_url = models.CharField(max_length=255, verbose_name='이미지 url', null=True, blank=True)
    job = models.CharField(max_length=30, verbose_name="직업", blank=True)
    
    twitter = models.CharField(max_length=50, blank=True) 
    facebook = models.CharField(max_length=50, blank=True) 
    blog = models.CharField(max_length=255, blank=True) 
    page = models.CharField(max_length=255, blank=True) 

    wiki = models.TextField(verbose_name='추가 정보', blank=True)
    extra_info = models.TextField(verbose_name='추가 정보', blank=True)

    nec_id = models.CharField(max_length=20, blank=True) 
    num = models.CharField(max_length=30, verbose_name="기호", blank=True)
    property = models.CharField(max_length=12, verbose_name="재산", blank=True)
    military_info = models.CharField(max_length=30, verbose_name="병역", blank=True)

    payed_tax = models.CharField(max_length=12, verbose_name="재산", blank=True)
    not_pay_tax_five = models.CharField(max_length=12, verbose_name="최근 5년간 체납금액", blank=True)
    not_pay_tax_current = models.CharField(max_length=12, verbose_name="현재채납급액", blank=True)

    conviction_count = models.CharField(max_length=10, verbose_name="전과", blank=True)
    candidacy_count = models.CharField(max_length=12, verbose_name="현재채납급액", blank=True)
    
    type = models.CharField(
        max_length=10,
        choices=(
            ("R", "비례"),
            ("D", "지역구"),
        )
    )

    district = models.ForeignKey(verbose_name='지역구', 
        to=District, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        default=None
    ) 

    assembly_id = models.CharField(
        max_length=10,
        choices=(
            ("21", "21대"),
        )
    )    
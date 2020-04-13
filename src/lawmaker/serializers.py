from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from .models import Person, ActiveLawMaker, Candidacy
import re
import datetime
import json

class PersonSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    representative_bill_count = serializers.SerializerMethodField()
    representative_bill_approval_count = serializers.SerializerMethodField()
    proposal_count = serializers.SerializerMethodField()
    approval_count = serializers.SerializerMethodField()
    birthday = serializers.SerializerMethodField()
    
    class Meta:
        model = Person
        depth = 1
        exclude = ('type', ) 
        ref_name = '국회의원'

    def get_image_url(self, obj):
        assembly_url = 'http://www.rokps.or.kr'
        img_url = f'{assembly_url}{obj.image_url}'
        return img_url
    
    def get_representative_bill_count(self, obj):
        bills_count = len((obj.active.representative_bill))
        return bills_count
    
    def get_representative_bill_approval_count(self, obj):
        bills_count = len((obj.active.representative_approval_bill))
        return bills_count
    
    def get_proposal_count(self, obj):
        bills_count = len((obj.active.proposer_bill))
        return bills_count
    
    def get_approval_count(self, obj):
        bills_count = len((obj.active.approval_bill))
        return bills_count
    
    def get_birthday(self, obj):
        try:
            f = re.split('[\(/\)]', obj.birthday)
            now = datetime.datetime.now()
            age = now.year+1-int(f[0])
            birthday = '{}/{}/{}({}세)'.format(f[0], f[1], f[2], age) 
        except:
            birthday = obj.birthday

        return birthday

class SummaryPersonserializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    active_info = serializers.SerializerMethodField()
    
    class Meta:
        model = Person
        fields = ('name', 'id', 'image_url', 'active_info')
    
    def get_image_url(self, obj):
        assembly_url = 'http://www.rokps.or.kr'
        img_url = f'{assembly_url}{obj.image_url}'
        return img_url
    
    def get_active_info(self, obj):
        active = obj.active

        active_info = {
            'ranking': active.ranking,
            'representative_bill': active.representative_bill
        }
        # assembly_url = 'http://www.rokps.or.kr'
        # img_url = f'{assembly_url}{obj.image_url}'
        return active_info

class SummaryCandidacyserializer(serializers.ModelSerializer):
    class Meta:
        model = Candidacy
        ref_name = "후보군"
        fields = ('id', 'name', 'party', 'district', 'num', 'image_url')
        # fields = ('item_nbr', 'plu')

class Candidacyserializer(serializers.ModelSerializer):
    property = serializers.SerializerMethodField()
    payed_tax = serializers.SerializerMethodField()
    
    class Meta:
        model = Candidacy
        fields = '__all__'
    
    def get_property(self, obj):
        return obj.property.replace(",", "")
    
    def get_payed_tax(self, obj):
        return format(int(obj.payed_tax.replace(",", ""))*1000, ',d')


class Rankserializer(serializers.ModelSerializer):
    lawmaker = serializers.SerializerMethodField()

    class Meta:
        model = ActiveLawMaker
        fields = ('ranking', 'lawmaker')

    def get_lawmaker(self, obj):
        try:
            lawmaker = Person.objects.get(active=obj) 
            p = PersonRankserializer(lawmaker)
            return p.data
        except ObjectDoesNotExist: 
            return json.dumps({})


class PersonRankserializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Person
        fields = ('name', 'party', 'image_url', 'district')
        depth = 1

    def get_image_url(self, obj):
        assembly_url = 'http://www.rokps.or.kr'
        img_url = f'{assembly_url}{obj.image_url}'
        return img_url
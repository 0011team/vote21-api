from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from .models import Person, ActiveLawMaker, Candidacy
from district.models import District, City
from .serializers import PersonSerializer, SummaryPersonserializer, SummaryCandidacyserializer, Candidacyserializer

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

import csv
import os
import re
import requests
import json


class LawmakerView(APIView):
    """
        지역구명을 조회하는  API 
    """

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):

        # persons = Person.objects.all()
            
        # 정보 가져오기
        query_district = self.request.query_params.get('district', None)
        lawmaker_district = self.request.query_params.get('name', None)
        
        district = District.objects.get(
            name=query_district.strip(), 
        )

        if ( lawmaker_district is not None):
            person = Person.objects.get(
                district=district,
                name=lawmaker_district
            )
        else:
            person = Person.objects.filter(
                district=district,
            )[1]
        s = PersonSerializer(person)
        return Response(s.data, status.HTTP_200_OK)
            
        
class LawmakerSummaryView(APIView):
    """
        지역구에 따른 요약정보 공유 
    """
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        query_district = self.request.query_params.get('district', None)
        if query_district is None:
            return Response({"msg": "지역구정보가 필요합니다."}, status.HTTP_400_BAD_REQUEST)        
        try:
            district = District.objects.get(name=query_district.strip())
        except (ObjectDoesNotExist):
            return Response({"msg": "해당하는 지역구정보가 존재하지않습니다."}, status.HTTP_400_BAD_REQUEST)


        persons = Person.objects.filter(district=district)
        candidacies = Candidacy.objects.filter(district=district).extra(select={'int_num': 'CAST(num AS INTEGER)'},
                      order_by=['int_num'])

        p = SummaryPersonserializer(persons[0])
        c = SummaryCandidacyserializer(candidacies, many=True)

        return Response(
            {
                "current_lawmaker": p.data,
                "candidacy_lawmaker": c.data
            }
        )

class CandidateView(APIView):
    """
        지역구에 따른 요약정보 공유 
    """
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        query_district = self.request.query_params.get('district', None)
        candidate = self.request.query_params.get('name', None)
        
        if query_district is None or candidate is None:
            return Response({"msg": "잘못된 접근입니다"}, status.HTTP_400_BAD_REQUEST)        
        else:
            try:
                district = District.objects.get(name=query_district.strip())
                candidate = Candidacy.objects.filter(district=district).get(name=candidate.strip())
            except (ObjectDoesNotExist):
                return Response({"msg": "해당하는 후보자 정보가 존재하지않습니다."}, status.HTTP_400_BAD_REQUEST)
            c = Candidacyserializer(candidate)
        return Response(c.data)


class LawmakerPushView(APIView):
    """
        지역구명을 조회하는  API 
    """

    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        
        # csv_dir = "/Users/donggeunyi/backup_by_dong/PycharmProjects/new-crawlers/bills/peoplepower21/"
        json_dir = "/Users/donggeunyi/backup_by_dong/PycharmProjects/new-crawlers/bills/json/20/"
        # nec_dir = "/Users/donggeunyi/backup_by_dong/PycharmProjects/new-crawlers/nec/candidates/"
        
        # with open( json_dir + '/2024795.json', newline='') as json_file:
            # json_data = json.load(json_file)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # persons = Person.objects.all()
        # for p in persons:
        #     active = p.active 
        #     active.major_bill = []
        #     active.save()

        # with open( base_dir + '/20_early.csv', newline='') as csv_file, open( base_dir + '/20_late.csv', newline='') as csv_file2:
        #     reader1 = list(csv.reader(csv_file, delimiter=',', ))
        #     reader2 = list(csv.reader(csv_file2, delimiter=',', ))

        #     reader = reader1[1:]

        #     names = reader1[0][5:]
        #     headers = reader1[1][5:]
            
        #     # print (names, headers)
        #     for r in reader[1:]:
        #         arr = r[5:]
        #         print (r[0], r[5:])

        #         r[0] = r[0].strip()
        #         if (r[0]=="金成泰" or r[0]=="金聖泰" or r[0] == "崔敬煥" or r[0] == "崔炅煥"):
        #             p = Person.objects.get(name_cn=r[0])
        #         else:
        #             p = Person.objects.get(name=r[0])
        #         active = p.active 
        #         info = active.major_bill
                
        #         for i, v in enumerate(headers):
        #             val = {
        #                 "bill_id": str(v), 
        #                 "title": names[i],
        #                 "vote": arr[i]
        #             }
        #             info.append(val)
        #         active.major_bill = info
        #         active.save()

        return Response({"data": [] })



from django.shortcuts import render
from django.db.models.expressions import F, RawSQL
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework import pagination


from .models import Person, ActiveLawMaker, Candidacy
from district.models import District, City
from .serializers import PersonSerializer, SummaryPersonserializer, SummaryCandidacyserializer, Candidacyserializer, Rankserializer

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

import csv
import os
import re
import requests
import json


def sort_query(category, page=1):
    qs = ActiveLawMaker.objects.annotate(
        _property=RawSQL("ranking->'{}'->'ranking'".format(category), [])
    ).order_by('_property')[:100]
    return qs
        
# 페이지네이션 추가
class QueryPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 10
    max_page_size = 10


class LawmakerView(APIView):
    """
        지역구명을 조회하는  API 
        해당 지역구의 의원 정보 가져오기 
    """

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
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
            person = Person.objects.get(
                district=district,
            )
        s = PersonSerializer(person)
        return Response(s.data, status.HTTP_200_OK)
            
        
class LawmakerSummaryView(APIView):
    """
        지역구의원의 요약정보
        20대 현역 의원 요약 정보 
        21대 의원 후보 요약 정보
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
        지역구 출마 후보의 정보  
        21대 의원 후보의 정보
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

class LawmakerRankView(APIView):
    """
        랭킹보드 정보
    """

    permission_classes = (permissions.AllowAny,)
    pagination_class = QueryPagination
    def get(self, request, format=None):
        category = self.request.query_params.get('category', None)
        if (category is not None):
            
            qs = sort_query(category, 1)
            r = Rankserializer(qs, many=True)
        else:
            actives = ActiveLawMaker.objects.filter(ranking__isnull=False)[:50]
        return Response(r.data)


class LawmakerPushView(APIView):
    """
        테스트용
    """

    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        return Response({"data": [] })


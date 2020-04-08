from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from .models import District, City
from .serializers import DistrictSerializer, AdressSerializer

import csv
import os


class DistrictView(APIView):
    """
        지역구명을 조회하는  API 
    """

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        districts = District.objects.all()
        s = DistrictSerializer(districts, many=True)
        return Response(s.data)


class AdressView(APIView):
    """
        지역구에 소속된 행정구역 명을 조회하는  API 
        ---
        ## 내용 
            - province: 시군구 
            - town: 읍면동
    """

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        state = self.request.query_params.get('state', None)
        # province = self.request.query_params.get('province', None)
        if state == "all":
            state_list = [
                '서울특별시', 
                '인천광역시', 
                '광주광역시',
                '대전광역시', 
                '부산광역시', 
                '대구광역시', 
                '울산광역시', 
                '세종특별자치시', 
                '경기도', 
                '경상북도', 
                '경상남도', 
                '충청북도',
                '충청남도', 
                '강원도', 
                '전라북도',
                '전라남도', 
                '제주특별자치도', 
            ]
            return Response(state_list)
        elif state is not None:
            adresses = City.objects.filter(state=state)
            s = AdressSerializer(adresses, many=True)
        else:
            adresses = City.objects.all()
            s = AdressSerializer(adresses, many=True)
        return Response(s.data)


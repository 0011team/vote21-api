from django.shortcuts import render
from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

import csv
import json

JSON_DIR = settings.JSON_DIR
CSV_DIR = settings.CSV_DIR

class BillDetailView(APIView):
    """
        법안 관련 상세 정보 조회
    """

    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        try: 
            json_dir = JSON_DIR
            with open( JSON_DIR + '{}.json'.format(self.kwargs['bill_id']), newline='') as json_file:
                json_data = json.load(json_file)
            return Response({"data": json_data })
        except:
            return Response({"msg": "해당 정보가 존재하지 않습니다."}, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg": "잘못된 접근입니다."}, status.HTTP_400_BAD_REQUEST)


class BillListView(APIView):
    """
        지역구명을 조회하는  API 
    """

    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        with open( CSV_DIR + '20.csv', newline='') as csv_file:
            # reader1 = list(csv.reader(csv_file, delimiter=',', ))
            # data = {
            #     "data": json.dumps(reader1)
            # }
            # M = dict(reader1)
            return Response({"msg":[] }, status.HTTP_200_OK)


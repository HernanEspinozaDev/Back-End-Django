from django.shortcuts import render
from abvApp.models import Student
from abvApp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        ser = StudentSerializer(students, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        ser = StudentSerializer(student)
        return Response(ser.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        ser = StudentSerializer(student, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
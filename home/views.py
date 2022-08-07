import json
from operator import le
from unittest import result
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Todo
import requests
from django.core.paginator import Paginator
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_word_filter import FullWordSearchFilter

from .serializer import Serializer
from .helper import paginate
from home import serializer

# Create your views here.

def main(request):
    return render(request, 'main.html')
    # return HttpResponse('heloo')

class TodoView(APIView):
    # def get(self, request):
        # r = requests.get('https://randomuser.me/api/?results=4').json()
        # # print(r['results'][0])
        # print("1===",r['results'][0])
        # print("2===",r['results'][1])
        # print("3===",r['results'][2])
        # print("4===",r['results'][3])

    def post(self, request):
        try:
            rec = requests.get('https://randomuser.me/api/?results=4').json()
            com=rec['results']
            # n = data['name']
            # f = n['first']
            # l = n['last']
            # name = str(f+ ' ' + l)
            # up = {"name" : name}
            # data.update(up)
            print("size==",len(com))
            for x in range(len(com)):
                data=com[x]
                del data['location']
                del data['login']
                del data['registered']
                del data['picture']
                n = data['name']
                f = n['first']
                l = n['last']
                name = str(f+ ' ' + l)
                up = {"name" : name}
                data.update(up)
                bd=data['dob']
                dob=str(bd['date'][:10])
                age = str(bd['age'])
                updob = {"dob" : dob, "age": age}
                data.update(updob)

                # Not including id from randomuser.me because in some data id: name/value are null/empty
                del data['id']
                # did = data['id']
                # # na = did['name']
                # va = str(did['value'])
                # # id =str(na+' '+va)
                # upid = {"id" : va}
                # data.update(upid)
                print("data==",data)
                serializer = Serializer(data=data)
                if serializer.is_valid():
                    print("serialisation done")
                    serializer.save()
                    print("saved in database")
                # print(len(com))
            return Response({
                    'status' : True,
                    'message' : 'Success save Data!!',
                    'data' : serializer.data
                })
        except Exception as e:
            print(e)

        return Response({
                'status' : False,
                'message' : 'Something went wrong!!',
                'data' : serializer.errors
            })


    def get(self, request):
        todo_objs = Todo.objects.all()
        page = request.GET.get('page', 2)
        page_obj = Paginator(todo_objs, page)
        # page_obj = paginator.get_page(page_number)
        results = paginate(todo_objs, page_obj,  page)

        serializer = Serializer(results['results'], many=True)
        
        # print(paginator)
        # print(serializer) 

        return Response({
            'status': True,
            'message': 'Todo Fetched',
            'data': {
                'data': serializer.data , 'pagination' : results['pagination']
            }
        })
        
class SearchTodoView(ListAPIView):
    serializer_class = Serializer
    queryset = Todo.objects.all()
    filter_backends = [DjangoFilterBackend, FullWordSearchFilter, OrderingFilter]
    filterset_fields = ['id','gender','name','email','dob','phone','cell','nat','age']
    word_fields = ['id','gender','name','email','dob','phone','cell','nat','age']
    ordering_fields = ['id','gender','name','email','dob','phone','cell','nat','age']
    def get(self, request):
        
        # todo_objs = Todo.objects.all()
        # req = request.GET.get('gender', 2)
        # n = request.GET
        # inp = list(n.items())
        # inp0 = inp[0][0]
        # print(str(inp[0][1]))
        todo_objs = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(instance=todo_objs, many = True)
        return Response({
            'status': True,
            'message': 'Todo Fetched',
            'data': serializer.data
        })
    
        

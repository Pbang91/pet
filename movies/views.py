from django.views import View
from django.http  import JsonResponse
from .models      import *
import json
import datetime


class ActorView(View):
    def get(self, request):
        # Actor 테이블 객체를 전부 가지고 온다.
        actor_list = Actor.objects.all()
        # Response 해줄 results 리스트를 선언해준다.
        results = []
        # 가지고 온 Actor 테이블의 정보를 하나씩 꺼내주자.
        for i in actor_list:
            # 하나씩 꺼내진 Actor 테이블의 객체의 아이디로 역참조를 해서 Movie 테이블의 객체를 가져와주자.
            movie_list = i.movie_set.filter(actors = i.id)
            # Response 해줄 Movie 의 타이틀을 담아 줄 title 리스트를 선언해준다.
            title_list = []
            # Movie 테이블의 객체를 하나씩 꺼내주자.
            for j in movie_list:
                # 하나씩 꺼낸 객체의 title을 위에서 만든 title 리스트에 담아주자.
                movie_title = j.title
                title_list.append(movie_title)
            # 하나씩 꺼낸 이름과 성, 타이틀 리스트를 담아주자.
            result = {
                'first_name' : i.first_name,
                'last_name'  : i.last_name,
                'movie_list' : title_list
            }
            # 위에서 담아준 result 정보를 Response 해줄 results 리스트에 담아주자.
            results.append(result)
        # 응답해주자.
        return JsonResponse({"result" : results}, status = 200)


    # def get(self, request):
    #     results = []
    #     actors_all  = Actor.objects.all()
    #     for actor in actors_all:
    #         title_list   = []
    #         actor_of_movies = ActorOfMovie.objects.all()
    #         for actor_of_movie in actor_of_movies:
    #            titles = actor.movie_set.get(actors = actor_of_movie.actor_id)
    #            title_list.append(titles)
    #         result = {
    #             'first_name' : actor.first_name,
    #             'last_name'  : actor.last_name,
    #             'movie_list' : title_list
    #         }
    #         results.append(result)

    #     return JsonResponse({"result" : results}, status = 200)

class MovieView(View):
    def get(self, request):
        # Movie 테이블의 객체를 전부 가지고 온다.
        movie_list = Movie.objects.all()
        # Response 해줄 results 리스트를 선언해준다.
        results    = []
        # 가져온 모든 Movie 테이블의 객체를 하나씩 뽑아준다.
        for i in movie_list:
            # Response 해줄 Actor 의 first_name 을 담아줄 name 리스트를 선언해준다.
            name_list = []
            # 위에서 뽑아준 Movie 테이블의 객체에 정참조된 Actor 테이블의 객체를 전부 가지고 온다.
            actor_list = i.actors.all()
            # 가져온 모든 Actor 테이블의 객체를 하나씩 뽑아준다.
            for j in actor_list:
                # Actort 테이블의 객체에서 first_name만 name 리스트에 넣어준다.
                name_list.append(j.first_name)
            # 하나씩 꺼낸 Movie 테이블 객체의 title, running_time, 네임리스트를 넣어주자.
            result = {
                "title"        : i.title,
                "running_time" : i.running_time,
                "actor_list"   : name_list
            }
            # 위에서 담아준 result를 results 리스트에 담아주자.
            results.append(result)
        # 응답해주자.
        return JsonResponse({"result" : results}, status = 200)
    
    # def get(self, request):
    #     results = []
    #     movies = Movie.objects.all()
    #     for movie in movies:
    #         actor_list = []
    #         actors = Actor.objects.all()
    #         for actor in actors:
    #             actor_information = {
    #                 "first_name" : actor.first_name
    #             }
    #             actor_list.append(actor_information)
    #         result = {
    #             "title" : movie.title,
    #             "running_time" : movie.running_time,
    #             "actor_first_name" : actor_list
    #         }
    #         results.append(result)
    #     return JsonResponse({"result" : results}, status = 200)
from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.models import Movie

from myapp.forms import MovieForm

# Create your views here.


# listing movies

# url:localhost:8000/movies/all/

# method:get


class MovieListView(View):

    def get(self,rquest,*args,**kwargs):

        qs=Movie.objects.all()#select * from movie

        return render(rquest,"movie_list.html",{"data":qs})
    


class MovieCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=MovieForm()#created a movieform instance

        return render(request,"movie_add.html",{"form":form_instance})
    
    
    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data#python dictionary
            # Movie.objects.create(title:"abscd")

            Movie.objects.create(**data)

            return redirect("movie-list")
        
        else:

            return render(request,"movie_add.html",{"form":form_instance})
        



# localhost:8000/movies/4/
# path("movies/<int:pk>/",Vi)
        

class MovieDeatilView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movie.objects.get(id=id)

        return render(request,"movie_detail.html",{"data":qs})




# url:localhost:8000/movies/{id}/remove/
# method:get


class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Movie.objects.get(id=id).delete()

        return redirect("movie-list")

    
# localhost:8000/movies/{id}/change/
# method:get,post

class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")#i

        movie_object=Movie.objects.get(id=id)#type of movie_object is queryset

        dictionary={
            "title":movie_object.title,
            "year":movie_object.year,
            "run_time":movie_object.run_time,
            "director":movie_object.director,
            "language":movie_object.language,
            "genre":movie_object.genre,
            "producer":movie_object.producer

        }

        form_instance=MovieForm(initial=dictionary)

        return render(request,"movie_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        id=kwargs.get("pk")

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Movie.objects.filter(id=id).update(**data)

            return redirect("movie-list")
        
        else:

            return render(request,"movie_edit.html",{"form":form_instance})
        



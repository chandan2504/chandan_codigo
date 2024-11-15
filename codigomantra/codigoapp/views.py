from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login as user_log
from .models import Blog
from .serializers import blogserializer


def signup(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		pass_1 = request.POST.get("pass")
		pass_2 = request.POST.get("re-pass")

		if pass_1 != pass_2:
			return HttpResponse("password did not match")
		else: 

			my_user = User.objects.create_user(username = name,email= email,password = pass_1)
			my_user.save()
			return redirect("login")
		print("the data is got as ",name,pass_1,pass_2)


	return render (request,"signup.html")
def login(request):

	if request.method == "POST":
		name = request.POST.get('first')
		pass_1 = request.POST.get('password')
		user = authenticate(request,username = name,password = pass_1)
		if user is not None:
			user_log(request,user)
			return redirect ("blog")
		else:
			return HttpResponse("login error")
		# print("the first name is ",name,pass_1)
	return render(request,"login.html")


# @api_view(["POST","GET","PATCH","PUT","DELETE"])
# def blog(request):
# 	if request.method == "POST":
# 		blog_title = request.POST.get("title")
# 		blog_description = request.POST.get("description")
# 		writer_name = request.POST.get("auther")

# 		data = Blog(title = blog_title,description = blog_description,author = writer_name)
# 		data.save()


# 	return render (request,"blog.html")
@api_view(["POST","GET","PATCH","PUT","DELETE"])
def blog(request):
	if request.method == "POST":
		data1 = request.data
		serializer = blogserializer(data = data1)
		if serializer.is_valid():
			serializer.save()
			return Response("blog posted successfully!!")
		return Response(serializer.errors)

	elif request.method == "GET":
		obj = Blog.objects.all()
		serializer = blogserializer(obj,many=True)
		return Response(serializer.data)
	elif request.method == "PATCH":
		data1 = request.data
		obj = Blog.objects.get(id = data1["id"])
		serializer = blogserializer(obj,data = data1,partial = True)
		if serializer.is_valid():
			serializer.save()
			return Response("Updated successfully!!")
		return Response(serializer.errors)

	elif request.method == "DELETE":
		data1 = request.data
		obj = Blog.objects.get(id = data1["id"])
		obj.delete()
		return Response("deleted successfully!!")

@api_view(["POST"])	
def like_button(request):
	if request.method == "POST":
		blog_id = request.data.get("id")
		try:
			blog = Blog.objects.get(id = blog_id)
			blog.like += 1
			blog.save()
			serializer = blogserializer(blog)
			return Response("liked")
		except :
			return Response("Blog does not exist")







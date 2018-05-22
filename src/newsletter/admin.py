from django.contrib import admin
from .models import SignUp
from .models import Post
# Register your models here.
from .forms import SignUpForm
from .forms import PostForm
class SignUpAdmin(admin.ModelAdmin):
	list_display =["__unicode__","timestamp","updated"]
	form = SignUpForm
class PostAdmin(admin.ModelAdmin):
	list_display=["title","author"]
	form = PostForm


admin.site.register(SignUp,SignUpAdmin)

admin.site.register(Post,PostAdmin)
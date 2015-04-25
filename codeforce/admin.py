from django.contrib import admin

# Register your models here.
import models

class AuthorProblem(admin.ModelAdmin):
    pass

class AuthorContest(admin.ModelAdmin):
    pass

class AuthorCFUsers(admin.ModelAdmin):
    pass

admin.site.register(models.Problem, AuthorProblem)

admin.site.register(models.Contest, AuthorContest)

admin.site.register(models.CFUsers, AuthorCFUsers)
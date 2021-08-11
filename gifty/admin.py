from django.contrib import admin
from django.db import models
from django.urls import path
from django.template.response import TemplateResponse
from django.contrib.auth.models import Group
from .models import User


admin.site.unregister(Group)
admin.site.register(User)

# https://stackoverflow.com/questions/10053981/how-can-i-create-custom-page-for-django-admin
class AppManager(models.Model):
    class Meta:
        app_label = 'gifty'
        verbose_name = '앱관리'
        verbose_name_plural = verbose_name


class CustomModelAdmin(admin.ModelAdmin):
    template_name = ''
    url = ''

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(self.url, self.admin_site.admin_view(self.view))
        ]
        return custom_urls + urls

    def view(self, request):
        if request.method == 'GET':
            return self.get(request)
        if request.method == 'POST':
            return self.post(request)

    def get(self, request):
        return self.render_to_response(request)

    def post(self, request):
        pass

    def get_context_data(self, request):
        return dict(self.admin_site.each_context(request))

    def render_to_response(self, request):
        return TemplateResponse(request, self.template_name, self.get_context_data(request))


@admin.register(AppManager)
class AppManagerAdmin(CustomModelAdmin):
    template_name = 'gifty/app_manage.html'
    url = ''

    def get_context_data(self, request):
        context = super().get_context_data(request)

        return context





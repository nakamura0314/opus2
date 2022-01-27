from django.contrib import admin
from .models import Department, Employee,Club

# admin管理サイトでmodelsのクラスを登録
# "python3 manage.py makemigrations　アプリ名" で登録
# "python3 manage.py migrate"でmigrateを起動
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Club)

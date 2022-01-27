from django.db import models
from django.utils import timezone


class Department(models.Model):
    name = models.CharField('部署名', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    # admin管理サイトで部署選択欄が表示される
    def __str__(self):
        return self.name

# Fieldを新しく追加するとmigrateを行う


class Club(models.Model):
    name = models.CharField('部活名', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField('名', max_length=20)
    last_name = models.CharField('姓', max_length=20)
    # emailっぽくなかったらエラーにしてくれる
    # blank=Trueで空文字列を許可する
    email = models.EmailField('メールアドレス', blank=True)
    # Departmentは結びつき先のmodel
    # 第一引数にどのモデルと紐付けるか、verbose_nameは説明、
    # on_deleteは指定したファイルを消すときにどのように動作するのかを示す
    # models.PROTECTとすると中身が一つでもあったら、そのファイルを守る
    # ForeignKeyの場合はフィールドにモデルのインスタンスが格納される
    department = models.ForeignKey(
        Department, verbose_name='部署', on_delete=models.PROTECT,
    )
    # 'models.ManyToMany'は'ForeignKey'とあまり変わりないが、複数のものと結びつけることができる
    # Clubは結びつき先のmodel、verbose_nameは説明
    club = models.ManyToManyField(
        Club, verbose_name='部活',
    )
    created_at = models.DateTimeField('日付', default=timezone.now)
    # 新しくFieldを追加するときにmigrateをすると、既存のFieldはどうするのかと訊かれるので
    # その場合は、default値を決めるか、blank=Trueとして空欄を作る
    # 'models.OneToOneField'一つずつを紐付けて、それ以外では使えないようにする

    def __str__(self):
        return '{0} {1} {2}'.format(self.last_name, self.first_name, self.department)

from django import forms
from .models import Club,Department


class SearchForm(forms.Form):
    #'何々ChoiceField'とすることで選択肢を出すことができる
    #ModelChoiceFieldとすることで、modelをもとに選択肢を出してくれる
    #'queryset'はどのmodelが選択肢になるかを指定する
    #'label'は説明
    #'required'は必須かどうか、これをTrueにすると必ずなんらかのデータを選択しなければならない
    club=forms.ModelChoiceField(
        queryset=Club.objects,label='サークル',required=False)

    department=forms.ModelChoiceField(
        queryset=Department.objects,label='部署',required=False)
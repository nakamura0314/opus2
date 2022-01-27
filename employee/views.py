from django.views import generic
from .forms import SearchForm
from .models import Employee


# templateを見せるだけのview
class IndexView(generic.ListView):
    model = Employee
    #ページング処理のオブジェクトを渡す数を指定
    #ページング処理はListViewで使うことができる
    paginate_by=1

    def get_context_data(self):
        """テンプレートへ渡す辞書の作成"""
        # 親クラスのget_context_dataを呼ぶことで、listview本来の辞書を作成
        context = super().get_context_data()
        # 関数viewにはselfはいらない、汎用viewはselfいる
        context['form'] = SearchForm(self.request.GET)  # 基の辞書に、formを追加
        return context

    def get_queryset(self):
        """テンプレートへ渡す「employee_list」を作成する"""
        # formの取得
        form = SearchForm(self.request.GET)
        # is_validは入力された値にエラーがないかを確認する
        # formsで空欄は許可してるので、if文はいらない
        form.is_valid()  # これにしないと、cleane_dataができない

        # 親の'get_queryset'を呼び出して、全社員のデータを取得
        queryset = super().get_queryset()

        # 部署の選択があれば、部署で絞り込み
        # 'cleaned_data'データを型に応じて一定のやり方で整形して返す
        department = form.cleaned_data['department']
        # querysetでなんらかの選択が行われていればの分岐
        # department(引数、field名)=department(31行目の変数),
        # 上記より、filterでformで選択された部署で絞り込みを行う
        if department:
            queryset = queryset.filter(department=department)

        # サークルの選択があれば、サークルで絞り込み(filter)
        club = form.cleaned_data['club']
        # (club=club)をわかりやすくすると、(first_name=吉田)のようになる
        if club:
            queryset = queryset.filter(club=club)
        return queryset

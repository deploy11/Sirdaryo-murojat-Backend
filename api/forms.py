# dwitter/forms.py

from django import forms
from .models import *

class DweetForm(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user",'tel_name')

# class DweetForm1(forms.ModelForm):
#     class Meta:
#         model = Hokimiyat
#         exclude = ("user", )
#     def __init__(self, *args, **kwargs):
#         super(DweetForm1, self).__init__(*args, **kwargs)
#         self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='суд  масалалари')

class TashkilotForm(forms.ModelForm):
    class Meta:
        model = Tashkilotlar
        fields = ['name']

class DweetForm1(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("tel_name",)  # 'tel_name' maydonini olib tashladik, e'tibor bering, tuple uchun vergul qo'shish kerak

    def __init__(self, *args, **kwargs):
        super(DweetForm1, self).__init__(*args, **kwargs)
        # 'orinbosar' va 'tashkilot' maydonlarini sozlash
        self.fields['orinbosar'].widget.attrs.update({'class': 'form-control'})
        self.fields['tashkilot'].widget.attrs.update({'class': 'form-control'})




class DweetForm2(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm2, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='ички ишлар  фаол.')

class DweetForm3(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm3, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='прокуратура фаол. оид')

class DweetForm4(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm4, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='алимент масаласи')

class DweetForm5(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm5, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='суд  ижросига оид')

class DweetForm6(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm6, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='соғлиқни сақлаш')

class DweetForm7(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm7, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='пенсия ва нафақа')


class DweetForm8(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm8, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni=' мактаб  таълими')

class DweetForm9(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm9, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='уй-жой, ер б-н таъм.')

class DweetForm10(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm10, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='иш б-н таъминлаш')


class DweetForm11(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm11, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='афв этиш масаласи')

class DweetForm12(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm12, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='олий таълим масалалариa')

class DweetForm13(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm13, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='кредит олиш')

class DweetForm14(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm14, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='банк-молия  масалалари')

class DweetForm15(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm15, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='газ, электр, сув, иссиқлик таъминоти')

class DweetForm16(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm16, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='коммунал тўловларни ҳисоблаш')

class DweetForm17(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm17, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='йўл қурилиши')

class DweetForm18(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm18, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='солиқ  тўловлари')

class DweetForm19(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm19, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='транспорт масалалари')

class DweetForm20(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm20, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='қурилиш  соҳаси')

class DweetForm21(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm21, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='тадбиркорлик  ҳуқукларини бузулиши  ')

class DweetForm22(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm22, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='санъ-ат, маърифат ва маданият масалалариa')

class DweetForm23(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm23, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='дори-дармонга нарх-наво масаласи')

class DweetForm24(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm24, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='биринчи эҳтиёж молларига нарх-наво масалалари')

class DweetForm25(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm25, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='давлат  хизмати фаолияти')

class DweetForm26(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm26, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='моддий  ёрдам  олиш')

class DweetForm27(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(DweetForm27, self).__init__(*args, **kwargs)
        self.fields['tel_name'].queryset = Sorov.objects.filter(korish=False,ariza_mazmuni='бошқа масалалар')
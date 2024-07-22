from django import forms
from cars.models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField()
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField()
    value = forms.IntegerField()
    photo = forms.ImageField()
    
    def save(self):
        car = Car(
            model = self.cleaned_data ['model'],
            brand = self.cleaned_data ['brand'],
            factory_year = self.cleaned_data ['factory_year'],
            model_year = self.cleaned_data ['model_year'],
            plate = self.cleaned_data ['plate'],
            value = self.cleaned_data ['value'],
            photo = self.cleaned_data ['photo'],
        )
        car.save()
        return car
    
class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser de $ 20.000')
        return value
    
    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')
        if model_year < 1975:
            self.add_error('model_year', 'Somente carros fabricados após 1975' )
        return model_year
    
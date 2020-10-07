from django import forms
from Users.models import Transfers, Users

class TransferForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['person1'].disabled = True

    class Meta():
        model = Transfers
        fields = ('person1','person2','amount')

    def clean(self):
        all_clean_data = super().clean()
        person1 = all_clean_data['person1']
        person2 = all_clean_data['person2']
        amount = all_clean_data['amount']
        query1 = Users.objects.get(name=str(person1))
        query2 = Users.objects.get(name=str(person2))
        if str(person1) == str(person2):
            raise forms.ValidationError("Make sure you are not transferring money to yourself!")
        if amount > query1.balance:
            raise forms.ValidationError("You have only " + str(query1.balance) + " in your account!")
        if amount < 1:
            raise forms.ValidationError("Minimum transaction amount is 1!")
        query1.balance -= amount
        query1.save()
        query2.balance += amount
        query2.save()
        



        



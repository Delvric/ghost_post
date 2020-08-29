from django import forms


class GhostPostForm(forms.Form):
    boast_or_roast = forms.BooleanField(required=False)
    post = forms.CharField(max_length=200)

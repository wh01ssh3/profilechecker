from codemirror2.widgets import CodeMirrorEditor
from django import forms

from .models import Rule


class RuleForm(forms.ModelForm):
    """Form for ``Rule`` form"""
    code = forms.CharField(widget=CodeMirrorEditor(options={'mode': 'python'}))

    class Meta:
        model = Rule
        fields = '__all__'

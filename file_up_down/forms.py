# -*- coding:utf-8 -*-
from django import forms

class courseware_form(forms.Form):
    content = forms.FileField(label='uploadfile')
'''
    def __unicode__(self):
        return str(self.name)
'''   
   #content = forms.FileField()

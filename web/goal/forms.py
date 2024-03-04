from django import forms
        
class detailForms(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'your Name',
        }
    ))
    
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':'form-control2',
            'placeholder':'your email'
        }
    ))
  
    
    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control3',
            'placeholder':'your Subject'
        }
    ))
    
    
    message = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control4',
            'placeholder':'yourMessages'
        }
    ))
 
    
    
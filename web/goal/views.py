from django.shortcuts import render,redirect
from django.views import View
from.models import card,banners,controls
from . forms import detailForms
# Create your views here.

class home(View):
    cards = card.objects.all().order_by('-id')[::-1]
    bannerss = banners.objects.all().order_by('-id')[::-1]
    controlss = controls.objects.all().order_by('-id')[::-1]
    form = detailForms()
    def get(self,request,*args,**kwargs):
    
        data = {
            'rec':self.cards,
            'rec1':self.bannerss,
            'rec2':self.controlss
        }
        # context = {}
        data['form']=detailForms()
  
        return render(request,'Home.html',data)
    
    # def post(self,request,*args,**kwargs):
    #     form = detailForm(request.POST)
    #     if form.is_valid:
    #         form.save()
    #     return redirect('home')
    
# class about(View):
#     form = detailForms()
#     def get(self,request,*args,**kwargs):
#         context = {}
#         context['form']=detailForms()
#         return render(request,'about.html',context)
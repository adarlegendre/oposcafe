from django.shortcuts import render,redirect
from django.views import generic
from django.http import HttpResponse
from oposapp.models import Dishes,Category,Orders,Employees,Customers,Stock,Supplies,Supplier,System_info
from django.views.decorators.csrf import csrf_exempt
import io
import json
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum,Count
from django.core import serializers
import array 
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime
from escpos.printer import Network



def write_pdf_view(pk):
    y = 700
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont('Helvetica', 10)
    p.drawString(220, y, "PDF generate at "+timezone.now().strftime('%Y-%b-%d'))
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

@csrf_exempt
def Pin(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body)
            #t = Employees.objects.filter(pin=data)
            t = Employees.objects.raw('''SELECT oposapp_employees.id,oposapp_employees.name,oposapp_title.name as empl FROM oposapp_employees JOIN oposapp_title ON oposapp_employees.title_id=oposapp_title.id WHERE oposapp_title.name="Waiter" AND oposapp_employees.pin=%s''',[data])
            t = serializers.serialize('json', t)
        return HttpResponse("%s" % (t))
   #return HttpResponse("OK")

@csrf_exempt
def PinCash(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body)
            #t = Employees.objects.filter(pin=data)
            t = Employees.objects.raw('''SELECT oposapp_employees.id,oposapp_employees.name,oposapp_title.name as empl FROM oposapp_employees JOIN oposapp_title ON oposapp_employees.title_id=oposapp_title.id WHERE oposapp_title.name="Cashier" AND oposapp_employees.pin=%s''',[data])
            t = serializers.serialize('json', t)
        return HttpResponse("%s" % (t))
   #return HttpResponse("OK")

@csrf_exempt
def Order(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body)
            r=["\n"]
            try:
                for order in data['business']:
                    buzz = int(order['order_content']['quantity'])
                    if  buzz > 0:
                        for x in range(buzz):
                            
                            r.append(order['order_content']['dish'])
                            r.append("\n")
                            b = Orders(name=order['order_content']['name'],dish_id=order['order_content']['id'],price=order['order_content']['cost'],employee_id=order['order_content']['employee'],customer_id=1,status='uncleared',pub_date=timezone.now(),updated=timezone.now())
                            b.save()
                    else:
                       
                        r.append(order['order_content']['dish'])
                        r.append("\n")          
                        b = Orders(name=order['order_content']['name'],dish_id=order['order_content']['id'],employee_id=order['order_content']['employee'] ,customer_id=1,status='uncleared',pub_date=timezone.now(),updated=timezone.now())
                        b.save()
                        
                        
            except:
                pass
            try:
               t = 5
               # d=str(timezone.now())
               # r="".join(r)
               # kitchen = Network("192.168.1.87") #Printer IP Address
               # kitchen.text("    THE BIG TABLE RESTAURANT\n")
               # kitchen.text("--------------------------------------------\n")
               # kitchen.text("CAPTAIN ORDER\n")
               # kitchen.text("Order Number:132234\n")
               # kitchen.text("___________________________________________\n")
               # kitchen.text(r)
               # kitchen.text("___________________________________________\n")
               # kitchen.text(d)
               # kitchen.text("\n")
               # kitchen.barcode('1324354657687', 'EAN13', 64, 2, '', '')
               # kitchen.cut()
            except:
                pass
        return HttpResponse("%s" % (data))
   #return HttpResponse("OK")
@csrf_exempt
def Clear(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body)
            data = data['val']
            t=Orders.objects.filter(name=data).update(status='cleared')
        return HttpResponse("%s" % (data))
   #return HttpResponse("OK")

@csrf_exempt
def OrderDetails(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body)
            data = data['val']
            total = Orders.objects.filter(name=data).aggregate(Sum('price'))
            #t=Orders.objects.filter(name=data).update(status='cleared')
        return HttpResponse("%s" % (total['price__sum']))
   #return HttpResponse("OK")
@csrf_exempt
def Flag(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body)
            order = data['val']
            flag = data['flag']
            t=Orders.objects.filter(name=order).update(status=flag)
        return HttpResponse("%s" % (data))
   #return HttpResponse("OK")


@csrf_exempt
def Sales(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body)
            data = data.split('/')

            #result=Orders.objects.filter(pub_date__range=[data[0], data[1]])
            
            #result = Orders.objects.raw('SELECT oposapp_orders.id,oposapp_dishes.name as name FROM oposapp_orders JOIN oposapp_dishes ON oposapp_orders.dish_id=oposapp_dishes.id')
            result = Orders.objects.raw('SELECT oposapp_orders.id,oposapp_dishes.name as name FROM oposapp_orders JOIN oposapp_dishes ON oposapp_orders.dish_id=oposapp_dishes.id WHERE oposapp_orders.status="cleared"')
            result = serializers.serialize('json', result)
          
        return HttpResponse("%s" % (result))
   #return HttpResponse("OK")
@csrf_exempt
def Meals_summary(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body)
            data = data.split('/')
            start_date = data[0]
            
            end_date = data[1]
            start_date = datetime.date.today()
           #result =Orders.objects.values('name').order_by('name').annotate(total_price=Sum('price'))

            #result = Orders.objects.raw('SELECT oposapp_orders.id,oposapp_dishes.name as name FROM oposapp_orders JOIN oposapp_dishes ON oposapp_orders.dish_id=oposapp_dishes.id')
           #result = Orders.objects.raw('''SELECT oposapp_orders.id,oposapp_dishes.name as name,sum(price) as price FROM oposapp_orders JOIN oposapp_dishes ON oposapp_orders.dish_id=oposapp_dishes.id WHERE oposapp_orders.status="cleared" AND oposapp_orders.pub_date=DATE(%s) GROUP BY oposapp_orders.dish_id''',[start_date])
            result = Orders.objects.raw('''SELECT oposapp_orders.id,oposapp_dishes.name as name,sum(price) as price,DATE(oposapp_orders.pub_date) FROM oposapp_orders JOIN oposapp_dishes ON oposapp_orders.dish_id=oposapp_dishes.id WHERE oposapp_orders.status="cleared" GROUP BY DATE(oposapp_orders.pub_date) ''')
            result = serializers.serialize('json', result)
          
        return HttpResponse("%s" % (result))
   #return HttpResponse("OK")

@csrf_exempt
def Sales_summary(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body)
            data = data.split('/')

            #result=Orders.objects.filter(pub_date__range=[data[0], data[1]])
            
            #result = Orders.objects.raw('SELECT oposapp_orders.id,oposapp_dishes.name as name FROM oposapp_orders JOIN oposapp_dishes ON oposapp_orders.dish_id=oposapp_dishes.id')
            result = Orders.objects.raw('SELECT oposapp_orders.id,oposapp_dishes.name as name,sum(price) as price FROM oposapp_orders JOIN oposapp_dishes ON oposapp_orders.dish_id=oposapp_dishes.id WHERE oposapp_orders.status="cleared" GROUP BY oposapp_orders.dish_id')
            result = serializers.serialize('json', result)
          
        return HttpResponse("%s" % (result))
   #return HttpResponse("OK")

@csrf_exempt
def Sales_summary_spoilt(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body)
            data = data.split('/')

            #result=Orders.objects.filter(pub_date__range=[data[0], data[1]])
            
            #result = Orders.objects.raw('SELECT oposapp_orders.id,oposapp_dishes.name as name FROM oposapp_orders JOIN oposapp_dishes ON oposapp_orders.dish_id=oposapp_dishes.id')
            result = Orders.objects.raw('SELECT oposapp_orders.id,oposapp_dishes.name as name,sum(price) as price FROM oposapp_orders JOIN oposapp_dishes ON oposapp_orders.dish_id=oposapp_dishes.id WHERE oposapp_orders.status<>"cleared" GROUP BY oposapp_orders.dish_id')
            result = serializers.serialize('json', result)
          
        return HttpResponse("%s" % (result))
   #return HttpResponse("OK")   

def logout_request(request):
    logout(request)
    return redirect("oposapp:index")

def reports(request):
    return render(request = request,template_name = "oposapp/reports.html",context=None)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request,'username or password not correct')
                return redirect('/oposapp')
        else:
                messages.error(request,'username or password not correct')
                return redirect('/oposapp')
    form = AuthenticationForm()
    return render(request = request,template_name = "oposapp/login.html",context={"form":form})

def Pdf(request):
     
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

class LoginView(generic.ListView):
    template_name='oposapp/login.html'
    
    def get_queryset(self):
        return System_info.objects.all()

class IndexView(generic.ListView):
    template_name='oposapp/dashboard.html'
    queryset = Dishes.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        sys_info= System_info.objects.filter(pk=1)
        context['info']= sys_info[0].name
        context['category']= Category.objects.all() 
        return context
    

class OrdersView(generic.ListView):
    template_name='oposapp/orders.html'
    #queryset = Orders.objects.values('name').order_by('-pub_date').annotate(total=Sum('dish'))
    queryset = Orders.objects.filter(pub_date__gte=datetime.date.today()).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(OrdersView, self).get_context_data(**kwargs)
        sys_info= System_info.objects.filter(pk=1)
        context['info']= sys_info[0].name
        context['category']= Category.objects.all() 
        context['meals']= Orders.objects.all()
        #context['summed'] = Orders.objects.filter(attribute__in=name).values('name').annotate(score = Sum('price')).order_by('-price')
        return context

class MetricsView(generic.ListView):
    template_name='oposapp/metrics.html'
   
    #def get_queryset(self):
    #   return  Orders.objects.raw('SELECT oposapp_orders.id,oposapp_dishes.name as name,sum(price) as total FROM oposapp_orders JOIN oposapp_dishes ON oposapp_orders.dish_id=oposapp_dishes.id WHERE oposapp_orders.status="cleared" GROUP BY date(oposapp_orders.pub_date)')
    
    queryset = Orders.objects.raw('SELECT oposapp_orders.id,oposapp_dishes.name as name,sum(price) as total FROM oposapp_orders JOIN oposapp_dishes ON oposapp_orders.dish_id=oposapp_dishes.id WHERE oposapp_orders.status="cleared" GROUP BY CAST(oposapp_orders.pub_date AS DATE)')

    def get_context_data(self, **kwargs):
        context = super(MetricsView, self).get_context_data(**kwargs)
        context['category']= Category.objects.all() 
        context['meals']= Orders.objects.all()
        #context['summed'] = Orders.objects.filter(attribute__in=name).values('name').annotate(score = Sum('price')).order_by('-price')
        return context

class StocksView(generic.ListView):
    template_name='oposapp/stock.html'
    
    def get_queryset(self):
        return Stock.objects.all()

class CustomersView(generic.ListView):
    template_name='oposapp/customers.html'
    
    def get_queryset(self):
        return Customers.objects.all()

class PettycashView(generic.ListView):
    template_name='oposapp/stock.html'
    
    def get_queryset(self):
        return Stock.objects.all()

class SuppliesView(generic.ListView):
    template_name='oposapp/supplies.html'
    
    def get_queryset(self):
        return Supplies.objects.all()

class SuppliersView(generic.ListView):
    template_name='oposapp/stock.html'
    
    def get_queryset(self):
        return Supplier.objects.all()

class CartsView(generic.ListView):
    template_name='oposapp/cart.html'
    
    def get_queryset(self):
        return Supplier.objects.all()

class UserFormView(generic.View):
    form_class = UserForm
    template_name = 'oposapp/login.html'
    
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user =aunthenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('oposapp:index')
        
        return render(request,self.template_name, {'form':form})


    
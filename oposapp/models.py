from django.db import models

class Status(models.Model):
    name  = models.CharField(max_length=50)
    desc = models.CharField(max_length=20)

    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Status"

class Foodcombos(models.Model):
    name=models.CharField(max_length=50)
    mix_ratio = models.FloatField()
    unit_ratio = models.FloatField()
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Food Combos"

class Title(models.Model):
    name  = models.CharField(max_length=50)
    res = models.CharField(max_length=300)
    
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Title"

class Employees(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    pin = models.IntegerField()
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    photo= models.FileField(upload_to='documents/employees')
    title=models.ForeignKey(Title,on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Employees"

class Category(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Category"

class Floor_plan(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Floor Plan"

class Dishes(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    cost = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    photo= models.FileField(upload_to='documents/dishes')
    status =models.ForeignKey(Status,on_delete=models.CASCADE)
    food_combo = models.ForeignKey(Foodcombos,on_delete=models.CASCADE)

    def __str__ (self):
        return self.name    
    class Meta:
        verbose_name_plural = "Dishes"

class Condiments(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    status =models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__ (self):
        return self.name    
    class Meta:
        verbose_name_plural = "Condiments"

class Recipes(models.Model):
    name = models.CharField(max_length=50)
    cost = models.FloatField()
    conds =  models.ForeignKey(Condiments,on_delete=models.CASCADE)
    dish =  models.ForeignKey(Dishes,on_delete=models.CASCADE)
    status =models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__ (self):
        return self.name    
    class Meta:
        verbose_name_plural = "Recipes"
    
class Customers(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Customers"

class Orders(models.Model):
    name = models.CharField(max_length=50)
    employee = models.ForeignKey(Employees,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    dish =  models.ForeignKey(Dishes,on_delete=models.CASCADE)
    updated = models.DateTimeField()
    price =  models.FloatField()
    pub_date = models.DateTimeField()
    status = models.CharField(max_length=50)

    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Orders"
    
class Supplier(models.Model):
    name=models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    photo= models.FileField(upload_to='documents/suppliers')
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Suppliers"



class Supplies(models.Model):
    name=models.CharField(max_length=50)
    units = models.FloatField()
    quantity = models.CharField(max_length=20)
    cost = models.FloatField()
    receipt = models.FileField(upload_to='documents/receipts/supplies')
    delivery_note = models.FileField(upload_to='documents/receipts/delivery_notes')
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    sup_date = models.DateTimeField()
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Supplies"


class Stockflags(models.Model):
    flag  = models.CharField(max_length=100)
    units = models.FloatField()
    dish =  models.ForeignKey(Dishes,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    photo= models.FileField(upload_to='documents/stockflags')
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Stock Flags"

class Stock(models.Model):
    name  = models.CharField(max_length=50)
    units = models.FloatField()
    dish =  models.ForeignKey(Dishes,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Stock"

class Pettycash(models.Model):
    name  = models.CharField(max_length=50)
    amount = models.FloatField()
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    receipt = models.FileField(upload_to='documents/receipts/supplies')
    
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Petty Cash"


class System_info(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    photo = models.FileField(upload_to='documents/logo')
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "System Information"

class Lpo(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    photo = models.FileField(upload_to='documents/receipts/LPO')
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Local Purchase Order"

class Invoice(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    photo = models.FileField(upload_to='documents/receipts/Invoice')
   
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Invoice"

class Imprest(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    pub_date = models.DateTimeField()
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Imprest"


class Petty_Cash(models.Model):
    name = models.CharField(max_length=50)
    units = models.FloatField()
    quantity = models.CharField(max_length=20)
    cost = models.FloatField()
    receipt = models.FileField(upload_to='documents/receipts/petty')
    pub_date = models.DateTimeField()
    status = models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Petty Cash"



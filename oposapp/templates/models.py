from django.db import models
#stores all the supplies incoming and outgoing depending on the weigh stage
class Suppliers(models.Model):
    name = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Suppliers"
#store the different transporters that bring in the supplies.A transporter can many suppliers and vice versa
class Transporters(models.Model):
    name = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    supplier = models.ManyToMany(Suppliers)
    contact = models.CharField(max_length=50)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Transporters"

#The different tractors from different transporters related to one transporter
class Tractors(models.Model):
    name=models.CharField(max_length=50)
    no_plate=models.CharField(max_length=20)
    front_photo= models.FileField(upload_to='documents/tractors/front')
    up_photo= models.FileField(upload_to='documents/tractors/up')
    side_photo= models.FileField(upload_to='documents/tractors/side')
    back_photo= models.FileField(upload_to='documents/tractors/back')
    plate_photo= models.FileField(upload_to='documents/tractors/plate')
    status=models.CharField(max_length=50)
    transporter=models.ForeignKey(Transporters,on_delete=models.CASCADE)
    reg_date=models.DateTimeField()
    
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Tractors" 

#the commodities brought in by the different suppliers and vice versa
class Commodity(models.Model):
    name = models.CharField(max_length=50)
    supplier = models.ManyToMany(Suppliers)
    desc = models.CharField(max_length=50)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Commodity"  

#employees and the title
class Employees(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Employees"

#different shifts in the institution
class Shifts(models.Model):
    name=models.CharField(max_length=50)
    clock_in=models.DateTimeField()
    clock_out=models.DateTimeField()

    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Shifts"

#different  employees working as operators of the weighbridge

class Operators(models.Model):
    name=models.CharField(max_length=50)
    stages=models.CharField(max_length=50)
    employee=models.ForeignKey(Employees,on_delete=models.CASCADE)
    pub_date= models.DateTimeField()
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Operators"

#clocking in and out of the shifts
class Shifts_tx(models.Model):
    name=models.CharField(max_length=50)
    operator=models.ForeignKey(Operators,on_delete=models.CASCADE)
    shift=models.ForeignKey(Shifts,on_delete=models.CASCADE)
    clock_in=models.DateTimeField()
    clock_out=models.DateTimeField()
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Shifts Performance"

#different weighing stages that the tractors go through
class Weigh_stages(models.Model):
    name=models.CharField(max_length=50)
    stages=models.CharField(max_length=50)
    operator = models.ForeignKey(Operators,on_delete=models.CASCADE)
    pub_date=models.DateTimeField()
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Weigh Stages"

#tickets that are generated for different weighing stages
class Tickets(models.Model):
    name=models.CharField(max_length=50)
    weight=models.CharField(max_length=50)
    commodity=models.ForeignKey(Commodity,on_delete=models.CASCADE)
    weigh_stage=models.ForeignKey(Weigh_stages,on_delete=models.CASCADE)
    pub_date=models.DateTimeField()
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Tickets"

#serial connections 
class Connections_serial(models.Model):
    name=models.CharField(max_length=50)
    baud=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Serial Connections"

#ethernet connections
class Connections_etho(models.Model):
    name=models.CharField(max_length=50)
    ip_address=models.CharField(max_length=50)
    port=models.CharField(max_length=50)
    mac_address=models.CharField(max_length=50)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Ethernet Connections"





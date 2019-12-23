import csv
from unesco.models import Site, Category, States, Region, ISO
from decimal import Decimal
def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader,None)
    Site.objects.all().delete()
    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    ISO.objects.all().delete()

    for row in reader:
        print(row)
        try:
            y = int(row[3])
        except:
            y = None
        try:
            l = Decimal(row[4])
        except:
            l = None
        try:
            a = Decimal(row[5])
        except:
            a = None
        try:
            z = Decimal(row[6])
        except:
            z = None

        s, created = States.objects.get_or_create(name=row[8])
        c, created = Category.objects.get_or_create(name=row[7])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = ISO.objects.get_or_create(name=row[10])
        site = Site(name=row[0],year=y,description=row[1],justification=row[2],longitude=l,latitude=a,area_hectares=z,category=c,states=s,region=r,iso=i)
        site.save()

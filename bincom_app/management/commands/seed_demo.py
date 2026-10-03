from django.core.management.base import BaseCommand
from bincom_app.models import State,LGA,Ward,PollingUnit,PollingUnitResult
from bincom_app.forms import PARTIES
class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        state,_=State.objects.get_or_create(id=25,defaults={"name":"Delta"})
        lga,_=LGA.objects.get_or_create(uniqueid=1,defaults={"lga_name":"Demo LGA","state":state})
        ward,_=Ward.objects.get_or_create(uniqueid=1,defaults={"ward_name":"Demo Ward","lga":lga})
        data=[(8,"Demo Polling Unit 8",[802,719,416,939,394,100,120,50,20]),
              (9,"Demo Polling Unit 9",[500,400,200,300,100,50,70,30,10])]
        for uid,name,scores in data:
            pu,_=PollingUnit.objects.get_or_create(uniqueid=uid,defaults={"polling_unit_name":name,"ward":ward,"lga":lga,"state":state})
            for party,score in zip(PARTIES,scores):
                PollingUnitResult.objects.update_or_create(polling_unit=pu,party=party,defaults={"score":score})
        self.stdout.write(self.style.SUCCESS("Demo data loaded."))

from django.db import models

class State(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class LGA(models.Model):
    uniqueid = models.PositiveIntegerField(primary_key=True)
    lga_name = models.CharField(max_length=150)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name="lgas")
    def __str__(self): return self.lga_name

class Ward(models.Model):
    uniqueid = models.PositiveIntegerField(primary_key=True)
    ward_name = models.CharField(max_length=150)
    lga = models.ForeignKey(LGA, on_delete=models.PROTECT, related_name="wards")
    def __str__(self): return self.ward_name

class PollingUnit(models.Model):
    uniqueid = models.PositiveIntegerField(primary_key=True)
    polling_unit_name = models.CharField(max_length=255)
    ward = models.ForeignKey(Ward, on_delete=models.PROTECT, related_name="polling_units")
    lga = models.ForeignKey(LGA, on_delete=models.PROTECT, related_name="polling_units")
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name="polling_units")
    def __str__(self): return self.polling_unit_name

class PollingUnitResult(models.Model):
    polling_unit = models.ForeignKey(PollingUnit, on_delete=models.CASCADE, related_name="results")
    party = models.CharField(max_length=20)
    score = models.PositiveIntegerField(default=0)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["polling_unit","party"], name="unique_pu_party")]
        ordering = ["party"]

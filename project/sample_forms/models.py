from django.db import models


class CarClass(models.Model):
    car_class = models.CharField(max_length=20)
    
    def __str__(self):
        return self.car_class

class BudgetOwner(models.Model):
    budget_owner = models.CharField(max_length=20)
    
    def __str__(self):
        return self.budget_owner

class Company(models.Model):
    company = models.CharField(max_length=20)
    
    def __str__(self):
        return self.company

class ScenarioBudget(models.Model):
    scenario_budget = models.CharField(max_length=20)
    
    def __str__(self):
        return self.scenario_budget
    
class TypeBudget(models.Model):
    type_budget = models.CharField(max_length=20)
    
    def __str__(self):
        return self.type_budget
    
class CompanySh(models.Model):
    company_sh = models.CharField(max_length=20)
    
    def __str__(self):
        return self.company_sh
    
class DepartmentSh(models.Model):
    department_sh = models.CharField(max_length=20)
    
    def __str__(self):
        return self.department_sh
    
class Grade(models.Model):
    grade = models.CharField(max_length=20)
    
    def __str__(self):
        return self.grade

class GroupSh(models.Model):
    group_sh = models.CharField(max_length=20)
    
    def __str__(self):
        return self.group_sh
    
class OtdelSh(models.Model):
    otdel_sh = models.CharField(max_length=20)
    
    def __str__(self):
        return self.otdel_sh

class Post(models.Model):
    post = models.CharField(max_length=20)
    
    def __str__(self):
        return self.post



class PlanBuyCarsVactionsModel(models.Model):
    type_car_class = models.ForeignKey(CarClass, on_delete=models.CASCADE)
    budget_owner = models.ForeignKey(BudgetOwner, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    scenario_budget = models.ForeignKey(ScenarioBudget, on_delete=models.CASCADE)
    type_budget = models.ForeignKey(TypeBudget, on_delete=models.CASCADE)
    company_sh = models.ForeignKey(CompanySh, on_delete=models.CASCADE)
    department_sh = models.ForeignKey(DepartmentSh, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    group_sh = models.ForeignKey(GroupSh, on_delete=models.CASCADE)
    otdel_sh = models.ForeignKey(OtdelSh, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    period = models.DateField()
    free_cars = models.IntegerField()
    vacations = models.DecimalField(max_digits=8, decimal_places=2)
    count_vacancy_buy = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-modified",]
    
    def __str__(self):
        return self.type_car_class.car_class
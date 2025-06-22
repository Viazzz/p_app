from django.contrib import admin

from . import models


@admin.register(models.CarClass)
class CarClassAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BudgetOwner)
class BudgetOwnerAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ScenarioBudget)
class ScenarioBudgetAdmin(admin.ModelAdmin):
    pass

@admin.register(models.TypeBudget)
class TypeBudgetAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CompanySh)
class CompanyShAdmin(admin.ModelAdmin):
    pass

@admin.register(models.DepartmentSh)
class DepartmentShAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Grade)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.GroupSh)
class GroupShAdmin(admin.ModelAdmin):
    pass

@admin.register(models.OtdelSh)
class OtdelShAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PlanBuyCarsVactionsModel)
class PlanBuyCarsVactionsAdmin(admin.ModelAdmin):
    pass
    # list_display = ["name", "date", "quantity", "created", "modified"]
    # list_filter = ["name", "date", "quantity", "created", "modified"]
    # search_fields = ["name", "date", "quantity", "created", "modified"] 

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required

from .forms import PlanBuyCarsVactionsForm
from . import models

@login_required
def home(request):
    return render(request, "sample_forms/home.html")

@login_required
def plan_buy_car_vactions_form(request):
    form = PlanBuyCarsVactionsForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("sample_forms:plan_buy_car_vactions_table")
        else:
            return render(request, "sample_forms/plan_buy_car_vactions_form.html", context)
    return render(request, "sample_forms/plan_buy_car_vactions_form.html", context)

@login_required
def plan_buy_car_vactions_table(request):
    qs = models.PlanBuyCarsVactionsModel.objects.all()
    context = {"qs": qs}
    # return render(request, "sample_forms/plan_buy_cars_vactions_list.html", context)
    return render(request, "sample_forms/plan_buy_cars_vactions_js_table.html", context)

@login_required
def plan_buy_car_vactions_table_data(request):
    qs = models.PlanBuyCarsVactionsModel.objects.all()
    data = list(
        qs.values(
            "id",
            "type_car_class__car_class",
            "budget_owner__budget_owner",
            "company__company",
            "scenario_budget__scenario_budget",
            "type_budget__type_budget",
            "company_sh__company_sh",
            "department_sh__department_sh",
            "grade__grade",
            "group_sh__group_sh",
            "otdel_sh__otdel_sh",
            "post__post",
            "period",
            "free_cars",
            "vacations",
            "count_vacancy_buy",
        )
    )
    return JsonResponse(data, safe=False)


class PlanBuyCarsVactionsEditView(UpdateView):
    template_name = "sample_forms/plan_buy_car_vactions_form.html"
    model = models.PlanBuyCarsVactionsModel
    form_class = PlanBuyCarsVactionsForm
    success_url = reverse_lazy("sample_forms:plan_buy_car_vactions_table")


class PlanBuyCarsVactionsDeleteView(DeleteView):
    model = models.PlanBuyCarsVactionsModel
    success_url = reverse_lazy("sample_forms:plan_buy_car_vactions_table")
    template_name = "sample_forms/car_confirm_delete.html"
# Generated by Django 5.2.3 on 2025-06-22 05:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('sample_forms', '0001_initial'), ('sample_forms', '0002_firstmodel_quantity'), ('sample_forms', '0003_budgetowner_carclass_company_companysh_departmentsh_and_more'), ('sample_forms', '0004_alter_planbuycarsvactionsmodel_period'), ('sample_forms', '0005_delete_period')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_owner', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CarClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_class', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CompanySh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_sh', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentSh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_sh', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GroupSh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_sh', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OtdelSh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otdel_sh', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioBudget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scenario_budget', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TypeBudget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_budget', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PlanBuyCarsVactionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_cars', models.IntegerField()),
                ('vacations', models.DecimalField(decimal_places=2, max_digits=8)),
                ('count_vacancy_buy', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('budget_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_forms.budgetowner')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_forms.company')),
                ('company_sh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_forms.companysh')),
                ('department_sh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_forms.departmentsh')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_forms.grade')),
                ('group_sh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_forms.groupsh')),
                ('otdel_sh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_forms.otdelsh')),
                ('period', models.DateField()),
                ('type_car_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_forms.carclass')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_forms.post')),
                ('scenario_budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_forms.scenariobudget')),
                ('type_budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_forms.typebudget')),
            ],
            options={
                'ordering': ['-modified'],
            },
        ),
    ]

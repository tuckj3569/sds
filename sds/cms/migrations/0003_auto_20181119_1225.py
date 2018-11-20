# Generated by Django 2.0.7 on 2018-11-19 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20181106_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='FBATool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Assessment_Title', models.CharField(blank=True, max_length=30)),
                ('Assessment_Date', models.DateField(auto_now=True)),
                ('Assessment_Brief', models.TextField(blank=True)),
                ('Assessment_Setting', models.CharField(blank=True, max_length=30)),
                ('Assessment_Antecedent', models.CharField(blank=True, max_length=30)),
                ('Assessment_Behaviour', models.CharField(blank=True, max_length=30)),
                ('Assessment_Consequence', models.CharField(blank=True, max_length=30)),
                ('Assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client_FBA', to='cms.Client')),
            ],
        ),
        migrations.AlterField(
            model_name='assessment',
            name='Assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client_Assessment', to='cms.Client'),
        ),
        migrations.AlterField(
            model_name='behavior',
            name='Behavior_Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client_Behavior', to='cms.Client'),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='Dislike_Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client_Dislike', to='cms.Client'),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='FamilyMember_Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client_FamilyMember', to='cms.Client'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='Friend_Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client_Friend', to='cms.Client'),
        ),
        migrations.AlterField(
            model_name='healthcareprofessional',
            name='HealthcareProfessional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client_HealthcareProfessional', to='cms.Client'),
        ),
        migrations.AlterField(
            model_name='hobbie',
            name='Hobbie_Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client_Hobbie', to='cms.Client'),
        ),
        migrations.AlterField(
            model_name='housemates',
            name='HouseMates',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client_HouseMates', to='cms.Client'),
        ),
        migrations.AlterField(
            model_name='like',
            name='Like_Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client_Like', to='cms.Client'),
        ),
    ]

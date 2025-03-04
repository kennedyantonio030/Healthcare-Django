from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.CharField(choices=[('morning', 'Morning'), ('evening', 'Evening')], max_length=10)),
                ('extra_note', models.TextField(blank=True, null=True)),
                ('doctors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='hospital.doctor')),
            ],
            options={
                'verbose_name_plural': 'Appointment',
            },
        ),
    ]

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='phone_number',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]

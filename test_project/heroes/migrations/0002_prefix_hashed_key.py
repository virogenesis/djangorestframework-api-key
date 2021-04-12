# Generated by Django 2.2.2 on 2019-06-29 10:38

from django.db import migrations, models

APP_NAME = "heroes"
MODEL_NAME = "heroapikey"
DEPENDENCIES = [(APP_NAME, "0001_initial")]


def populate_prefix_hashed_key(apps, schema_editor):  # type: ignore
    model = apps.get_model(APP_NAME, MODEL_NAME)

    for api_key in model.objects.all():
        prefix, _, hashed_key = api_key.id.partition(".")
        api_key.prefix = prefix
        api_key.hashed_key = hashed_key
        api_key.save()


class Migration(migrations.Migration):

    dependencies = DEPENDENCIES

    operations = [
        migrations.AddField(
            model_name=MODEL_NAME,
            name="hashed_key",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name=MODEL_NAME,
            name="prefix",
            field=models.CharField(max_length=8, unique=True, null=True),
        ),
        migrations.RunPython(populate_prefix_hashed_key, migrations.RunPython.noop),
        migrations.AlterField(
            model_name=MODEL_NAME,
            name="hashed_key",
            field=models.CharField(max_length=100, editable=False),
        ),
        migrations.AlterField(
            model_name=MODEL_NAME,
            name="prefix",
            field=models.CharField(max_length=8, unique=True, editable=False),
        ),
    ]
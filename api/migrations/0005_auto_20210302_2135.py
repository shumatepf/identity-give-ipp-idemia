# Generated by Django 3.1.6 on 2021-03-02 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_enrollmentrecord_record_csp_id"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="enrollmentrecord",
            unique_together={("record_csp_uuid", "record_csp_id")},
        ),
    ]

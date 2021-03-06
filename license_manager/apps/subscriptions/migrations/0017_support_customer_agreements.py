# Generated by Django 2.2.17 on 2020-12-04 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0016_require_enterprise_catalog_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubscriptionplan',
            name='enterprise_catalog_uuid',
            field=models.UUIDField(blank=True, help_text="If you do not explicitly set an Enterprise Catalog UUID, it will be set from the Subscription's Customer Agreement `default_enterprise_catalog_uuid`."),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='customer_agreement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='subscriptions.CustomerAgreement'),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='enterprise_catalog_uuid',
            field=models.UUIDField(blank=True, help_text="If you do not explicitly set an Enterprise Catalog UUID, it will be set from the Subscription's Customer Agreement `default_enterprise_catalog_uuid`."),
        ),
        migrations.AlterUniqueTogether(
            name='subscriptionplan',
            unique_together={('title', 'customer_agreement')},
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-10 02:30

import django.db.models.deletion
from django.db import migrations

import djstripe.enums
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0005_2_2"),
    ]

    operations = [
        migrations.RemoveField(model_name="invoice", name="closed",),
        migrations.RemoveField(model_name="invoice", name="forgiven",),
        migrations.RemoveField(model_name="upcominginvoice", name="closed",),
        migrations.RemoveField(model_name="upcominginvoice", name="forgiven",),
        migrations.AddField(
            model_name="invoice",
            name="status",
            field=djstripe.fields.StripeEnumField(
                blank=True,
                default="",
                enum=djstripe.enums.InvoiceStatus,
                help_text="The status of the invoice, one of draft, open, paid, uncollectible, or void.",
                max_length=13,
            ),
        ),
        migrations.AddField(
            model_name="upcominginvoice",
            name="status",
            field=djstripe.fields.StripeEnumField(
                blank=True,
                default="",
                enum=djstripe.enums.InvoiceStatus,
                help_text="The status of the invoice, one of draft, open, paid, uncollectible, or void.",
                max_length=13,
            ),
        ),
        migrations.RenameField(
            model_name="subscription", old_name="billing", new_name="collection_method",
        ),
        migrations.AddField(
            model_name="invoice",
            name="discount",
            field=djstripe.fields.JSONField(
                blank=True,
                help_text="Describes the current discount applied to this subscription, if there is one. When billing, a discount applied to a subscription overrides a discount applied on a customer-wide basis.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="default_payment_method",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The default payment method for the subscription. It must belong to the customer associated with the subscription. If not set, invoices will use the default payment method in the customer’s invoice settings.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="djstripe.PaymentMethod",
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="discount",
            field=djstripe.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="subscription",
            name="next_pending_invoice_item_invoice",
            field=djstripe.fields.StripeDateTimeField(
                blank=True,
                help_text="Specifies the approximate timestamp on which any pending invoice items will be billed according to the schedule provided at pending_invoice_item_interval.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="pending_invoice_item_interval",
            field=djstripe.fields.JSONField(
                blank=True,
                help_text="Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling Create an invoice for the given subscription at the specified interval.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="pending_update",
            field=djstripe.fields.JSONField(
                blank=True,
                help_text="If specified, pending updates that will be applied to the subscription once the latest_invoice has been paid.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="start_date",
            field=djstripe.fields.StripeDateTimeField(
                blank=True,
                help_text="Date when the subscription was first created. The date might differ from the created date due to backdating.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="upcominginvoice",
            name="default_source",
            field=djstripe.fields.PaymentMethodForeignKey(
                help_text="The default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription’s default source, if any, or to the customer’s default source.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="upcoming_invoices",
                to="djstripe.DjstripePaymentMethod",
            ),
        ),
        migrations.AddField(
            model_name="upcominginvoice",
            name="discount",
            field=djstripe.fields.JSONField(
                blank=True,
                help_text="Describes the current discount applied to this subscription, if there is one. When billing, a discount applied to a subscription overrides a discount applied on a customer-wide basis.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="default_source",
            field=djstripe.fields.PaymentMethodForeignKey(
                blank=True,
                help_text="The default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription’s default source, if any, or to the customer’s default source.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="invoices",
                to="djstripe.DjstripePaymentMethod",
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="default_source",
            field=djstripe.fields.PaymentMethodForeignKey(
                blank=True,
                help_text="The default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If not set, defaults to the customer’s default source.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="subscriptions",
                to="djstripe.DjstripePaymentMethod",
            ),
        ),
    ]

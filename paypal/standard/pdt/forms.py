#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from paypal.standard.forms import PayPalStandardBaseForm
from paypal.standard.pdt.models import PayPalPDT

# Change: excluded payment_date and notify_version which were causing errors
class PayPalPDTForm(PayPalStandardBaseForm):
    class Meta:
        model = PayPalPDT
        exclude = ['ipaddress', 'flag', 'flag_code',
                   'flag_info', 'query', 'response',
                   'created_at', 'updated', 'form_view', 
                   'payment_date', 'notify_version']

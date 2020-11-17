# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt
from frappe import utils
from frappe.utils import date_diff


# import frappe


def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_record(filters)
    return columns, data


def get_columns():
    return [
		{
			"fieldname": "party_name",
			"label": _("Customer Name"),
			"fieldtype": "Data",
			"width": 150

		},
		{
			"fieldname": "status",
			"label": _("Status"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "transaction_date",
			"label": _("Quotation Date"),
			"fieldtype": "Data",
			"width": 150
		},

		{
			"fieldname": "name",
			"label": _("Quotation Name"),
			"fieldtype": "Data",
			"width": 150
		}

	]



def get_record(filters):
    data = []
    conditions = get_conditions(filters)
    data = frappe.db.sql('''select Qt.party_name,Qt.status,Qt.transaction_date,Qt.name

        from tabQuotation as Qt
             {}

        '''.format(conditions))
    return data


def get_conditions(filters):
    conditions = ''
    if filters.get('company'):
        conditions += " and Qt.party_name = '{}'".format(filters.get('party_name'))

    if filters.get('from_date') and filters.get('to_date'):
        conditions = "where date(transaction_date) between '{}' and '{}'".format(filters.get('from_date'),
                                                                                filters.get('to_date'))



    if filters.get('status'):
        conditions += "and Qt.status = '{}'".format(filters.get('status'))
    return conditions
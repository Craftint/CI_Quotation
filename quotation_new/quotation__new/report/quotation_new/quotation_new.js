// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Quotation New"] = {
	"filters": [
	                {
				"fieldname": "company",
				"label": __("Company"),
				"fieldtype": "Link",
				"options"  : "Company",
				"default"  : "CRAFT INTERACTIVE TECHNOLOGY LLC",

			},

	                {
				"fieldname": "from_date",
				"label": __("From Date"),
				"fieldtype": "Date",
				"default":frappe.defaults.get_user_default("year_start_date"),

			},
			{
				"fieldname": "to_date",
				"label": __("To Date"),
				"fieldtype": "Date",
				"default":frappe.datetime.get_today(),

			},
		    {
			    "fieldname": "status",
				"label": __("Status"),
				"fieldtype": "Select",
				"options"  :"Draft\nOpen\n Replied \nOrdered\nLost",



		       }

	]
};

# Copyright (c) 2023, Self and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta

class RateDetails(Document):
	pass


@frappe.whitelist(allow_guest=True)
def get_rate_details(doctype, name, item):
	rate_data = {}
	current_date = datetime.now()

	if name != None and item != None:
		customer = frappe.get_doc(doctype, name)
		for rate in customer.customer_rate_details:
			if rate.active == 1 and rate.job_type == item:
				rate_data.update({
									"job_type":rate.job_type,
								    "tax_type":rate.tax_type,
								    "customer_rate":rate.customer_rate,
								    "rate_minimum":rate.rate_minimum,
								    "dalivery_days":rate.dalivery_days,
								    "active": rate.active
								})
				expacted_date = current_date + timedelta(days=rate_data['dalivery_days'])
				rate_data.update({'expacted_date': expacted_date})
				return rate_data
	return rate_data
	
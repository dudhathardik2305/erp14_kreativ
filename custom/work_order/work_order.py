# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import json

import frappe
from dateutil.relativedelta import relativedelta
from frappe import _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.query_builder import Case
from frappe.query_builder.functions import Sum
from frappe.utils import (
	cint,
	date_diff,
	flt,
	get_datetime,
	get_link_to_form,
	getdate,
	nowdate,
	time_diff_in_hours,
)
from pypika import functions as fn

from erpnext.manufacturing.doctype.bom.bom import (
	get_bom_item_rate,
	get_bom_items_as_dict,
	validate_bom_no,
)
from erpnext.manufacturing.doctype.manufacturing_settings.manufacturing_settings import (
	get_mins_between_operations,
)
from erpnext.stock.doctype.batch.batch import make_batch
from erpnext.stock.doctype.item.item import get_item_defaults, validate_end_of_life
from erpnext.stock.doctype.serial_no.serial_no import (
	auto_make_serial_nos,
	clean_serial_no_string,
	get_auto_serial_nos,
	get_serial_nos,
)
from erpnext.stock.stock_balance import get_planned_qty, update_bin_qty
from erpnext.stock.utils import get_bin, get_latest_stock_qty, validate_warehouse_company
from erpnext.utilities.transaction_base import validate_uom_is_integer



class WorkOrder(Document):
	def onload(self):
		print('\n\nWork Order\n\n')



# Copyright (c) 2023, Self and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class DrawingDetails(Document):
	pass



@frappe.whitelist(allow_guest=True)
def get_drawing_details_customer(doctype, name):
	drawing_data = {}
	if name:
		drawing_name = frappe.get_doc(doctype, name).drawing_details
		drawing = frappe.get_doc("Drawing Details", drawing_name) 
		drawing_data.update({
								"name":drawing_name,
								"drwno":drawing.drwno,
								"boreod":drawing.boreod,
								"kwd":drawing.kwd,
								"remarks":drawing.remarks,
								"type":drawing.type,
								"flangethickness":drawing.flangethickness,
								"kwt":drawing.kwt,
								"boreid":drawing.boreid,
								"kww":drawing.kww,
								"degree":drawing.degree,
								"active":drawing.active
							})
		return drawing_data
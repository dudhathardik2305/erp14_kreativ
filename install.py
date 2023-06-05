# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


import frappe
import click
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.desk.page.setup_wizard.setup_wizard import add_all_roles_to
from frappe.utils import cint

from erpnext.accounts.doctype.cash_flow_mapper.default_cash_flow_mapper import DEFAULT_MAPPERS
from erpnext.setup.default_energy_point_rules import get_default_energy_point_rules
from erpnext.setup.doctype.incoterm.incoterm import create_incoterms
# from .default_success_action import get_default_success_action

default_mail_footer = """<div style="padding: 7px; text-align: right; color: #888"><small>Sent via
	<a style="color: #888" href="http://erpnext.org">ERPNext</a></div>"""


def before_install():
	create_custom_fields(get_custom_fields())
	frappe.clear_cache(doctype="Customer")
	frappe.clear_cache(doctype="Work Order")
	# make_fixtures()
	# setup_notifications()
	# update_hr_defaults()
	# add_non_standard_user_types()
	# set_single_defaults()
	# update_erpnext_access()
	# frappe.db.commit()
	# run_post_install_patches()
	# click.secho("Thank you for installing Frappe HR!", fg="green")



def get_custom_fields():
	print('\n\nget_custom_fields\n\n')
	"""HR specific custom fields that need to be added to the masters in ERPNext"""
	return {
		"Customer": [
				{
					"collapsible": 0,
					"fieldname": "section_of_tab_break_for_extra_info",
					"fieldtype": "Tab Break",
					"label": "Roller Details",
					"insert_after": "disabled",
				},{
					"fieldname": "pi_value",
					"fieldtype": "Float",
					"label": "PI Value",
					"insert_after": "section_of_tab_break_for_extra_info",
					"precision": "4",
				},
				{
					"fieldname": "printing_section",
					"fieldtype": "Section Break",
					"label": "Printing Section",
					"insert_after": "drawing_details",
				},{
					"fieldname": "print_side",
					"fieldtype": "Select",
					"label": "Print Side",
					"insert_after": "printing_section",
					"options": "Serface\nReverse"
				},{
					"fieldname": "print_on",
					"fieldtype": "Select",
					"label": "Print On",
					"insert_after": "print_side",
					"options": "20OPP (PCT)\nALUMINIUM FOIL\nBON POLY(NAYLON POLY)\nBOPP\nGLOSSY\nLDPE-NATURAL\nLDPE-WHITE\nLEATHER\nLTS OPP 40MIC\nMATT BOPP\nMATT PET\nMETALLIZE\nNATURAL POLY\nOPP (PCT)\nPAPER\nPER. BOPP\nPOLYESTER\nPVC\nSHRINK\nWhite polly"
				},{
					"fieldname": "artwork",
					"fieldtype": "Select",
					"label": "Artwork",
					"insert_after": "print_on",
					"options": "EMAIL\nJPEG\nJPEG & SAMPLE MATCH\nMEDIA\nSAMPLE MATCH"
				},{
					"fieldname": "slitting_mark",
					"fieldtype": "Check",
					"label": "Slitting Mark",
					"insert_after": "artwork",
				},{
					"fieldname": "sr_mark",
					"fieldtype": "Check",
					"label": "SR Mark",
					"insert_after": "slitting_mark",
				},{
					"fieldname": "auto_tone_mark",
					"fieldtype": "Check",
					"label": "Auto Tone Mark",
					"insert_after": "sr_mark",
				},{
					"fieldname": "gravure_proof_dt",
					"fieldtype": "Data",
					"label": "Gravure Proof Dt",
					"insert_after": "auto_tone_mark",
				},{
					"fieldname": "gravure_proof_no",
					"fieldtype": "Select",
					"label": "Gravure Proof No",
					"insert_after": "gravure_proof_dt",
					"options":" \n1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
				},{
					"fieldname": "printing_right_section",
					"fieldtype": "Column Break",
					"label": "",
					"insert_after": "gravure_proof_no",
					"options":" \n1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
				},{
					"fieldname": "print_on_2",
					"fieldtype": "Select",
					"label": "Print On 2",
					"insert_after": "printing_right_section",
					"options":" \nALUMINIUM FOIL\nBOPP\nfoil\nLDPE-NATURAL\nMATT BOPP\nMATT PET\nMETALLIZE\nMETALLIZE WHITE\nMettalized BOPP\nMAILKY POLY\nNATURAL POLY\nPAPER\nPearal BOPP\nPER. BOPP\nPVC\nWHITE Poly"
				},{
					"fieldname": "ink_type",
					"fieldtype": "Select",
					"label": "Ink Type",
					"insert_after": "print_on_2",
					"options":" \nNCPU\nNTNK\nNTPU\nPAPER INK\nPU\nSAKATA\nUV\nVINAYL\nWATER BAS"
				},{
					"fieldname": "proof_match_with",
					"fieldtype": "Select",
					"label": "Proof Match With",
					"insert_after": "ink_type",
					"options":" \nold Job\nOUR  DIGTAL PRINT\nOU  TEST CUT\nPARTY  COOUR PRINT\nPRINED SAMPLE\nSHADE CARD"
				},{
					"fieldname": "eye_mark",
					"fieldtype": "Check",
					"label": "Eye Mark",
					"insert_after": "proof_match_with",
				},{
					"fieldname": "monogram",
					"fieldtype": "Check",
					"label": "Monogram",
					"insert_after": "eye_mark",
				},{
					"fieldname": "web_direction",
					"fieldtype": "Select",
					"label": "Web Direction",
					"insert_after": "monogram",
					"options": " \nUP\nDOWN"
				},{
					"fieldname": "coil_no",
					"fieldtype": "Check",
					"label": "Coil No",
					"insert_after": "web_direction",
				},{
					"fieldname": "colour_print_dt",
					"fieldtype": "Data",
					"label": "Colour Print Dt",
					"insert_after": "coil_no",
				},{
					"fieldname": "colour_print_no",
					"fieldtype": "Select",
					"label": "Colour Print No",
					"insert_after": "colour_print_dt",
					"options": " \n1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
				}
		],
		"Work Order": [
				{
					"fieldname": "customer",
					"fieldtype": "Link",
					"label": "Customer",
					"options": "Customer",
					"insert_after": "bom_no",
				},{
					"collapsible": 0,
					"fieldname": "section_of_customer_break_for_extra_info",
					"fieldtype": "Section Break",
					"label": "Roller Details",
					"insert_after": "amended_from",
				},{
					"fieldname": "fab_roll",
					"fieldtype": "Float",
					"label": "Fab Roll",
					"insert_after": "section_of_customer_break_for_extra_info",
				},
				{
					"fieldname": "fab_rate",
					"fieldtype": "Float",
					"label": "Fab Rate",
					"insert_after": "fab_roll",
				},
				{
					"fieldname": "repeat_height",
					"fieldtype": "Float",
					"label": "Repeat Height",
					"insert_after": "fab_rate",
				},
				{
					"fieldname": "step_width",
					"fieldtype": "Float",
					"label": "Step width",
					"insert_after": "repeat_height",
				},
				{
					"fieldname": "supp_roll",
					"fieldtype": "Float",
					"label": "Supp Roll",
					"insert_after": "step_width",
				},
				{
					"fieldname": "supp_rate",
					"fieldtype": "Float",
					"label": "Supp Rate",
					"insert_after": "supp_roll",
				},
				{
					"fieldname": "roller_dimensions",
					"fieldtype": "Column Break",
					"label": "",
					"insert_after": "supp_rate",
				},
				{
					"fieldname": "x_repeat",
					"fieldtype": "Float",
					"label": "X Repeat",
					"insert_after": "roller_dimensions",
				},
				{
					"fieldname": "x_step",
					"fieldtype": "Float",
					"label": "X Step",
					"insert_after": "x_repeat",
				},
				{
					"fieldname": "circum",
					"fieldtype": "Float",
					"label": "Circum",
					"insert_after": "x_step",
				},
				{
					"fieldname": "len",
					"fieldtype": "Float",
					"label": "Len",
					"insert_after": "circum",
				},{
					"fieldname": "tmm",
					"fieldtype": "Float",
					"label": "TMM",
					"insert_after": "circum",
				},
				{
					"fieldname": "total_speciale",
					"fieldtype": "Section Break",
					"label": "Total Speciale",
					"insert_after": "len",
				},
				{
					"fieldname": "total_roll",
					"fieldtype": "Int",
					"label": "Total Roll",
					"insert_after": "total_speciale",
				},
				{
					"fieldname": "special_rate",
					"fieldtype": "Float",
					"label": "Special Rate",
					"insert_after": "total_roll",
				},
				{
					"fieldname": "dia",
					"fieldtype": "Float",
					"label": "Dia",
					"insert_after": "special_rate",
				},{
					"fieldname": "pi_value",
					"fieldtype": "Float",
					"label": "PI Value",
					"insert_after": "dia",
					"precision": "4",
				},{
					"fieldname": "total_column_break",
					"fieldtype": "Column Break",
					"label": "",
					"insert_after": "pi_value",
				},{
					"fieldname": "r_width",
					"fieldtype": "Float",
					"label": "R Width",
					"insert_after": "total_column_break",
				},{
					"fieldname": "add_width",
					"fieldtype": "Float",
					"label": "Add Width",
					"insert_after": "r_width",
				},{
					"fieldname": "cylinder_length",
					"fieldtype": "Float",
					"label": "Cylinder Length",
					"insert_after": "add_width",
				},{
					"fieldname": "mat_width",
					"fieldtype": "Float",
					"label": "Mat Width",
					"insert_after": "cylinder_length",
				},{
					"fieldname": "printing_section",
					"fieldtype": "Section Break",
					"label": "Printing Section",
					"insert_after": "job_details",
				},{
					"fieldname": "print_side",
					"fieldtype": "Select",
					"label": "Print Side",
					"insert_after": "printing_section",
					"options": "Serface\nReverse"
				},{
					"fieldname": "print_on",
					"fieldtype": "Select",
					"label": "Print On",
					"insert_after": "print_side",
					"options": "20OPP (PCT)\nALUMINIUM FOIL\nBON POLY(NAYLON POLY)\nBOPP\nGLOSSY\nLDPE-NATURAL\nLDPE-WHITE\nLEATHER\nLTS OPP 40MIC\nMATT BOPP\nMATT PET\nMETALLIZE\nNATURAL POLY\nOPP (PCT)\nPAPER\nPER. BOPP\nPOLYESTER\nPVC\nSHRINK\nWhite polly"
				},{
					"fieldname": "artwork",
					"fieldtype": "Select",
					"label": "Artwork",
					"insert_after": "print_on",
					"options": "EMAIL\nJPEG\nJPEG & SAMPLE MATCH\nMEDIA\nSAMPLE MATCH"
				},{
					"fieldname": "slitting_mark",
					"fieldtype": "Check",
					"label": "Slitting Mark",
					"insert_after": "artwork",
				},{
					"fieldname": "sr_mark",
					"fieldtype": "Check",
					"label": "SR Mark",
					"insert_after": "slitting_mark",
				},{
					"fieldname": "auto_tone_mark",
					"fieldtype": "Check",
					"label": "Auto Tone Mark",
					"insert_after": "sr_mark",
				},{
					"fieldname": "gravure_proof_dt",
					"fieldtype": "Data",
					"label": "Gravure Proof Dt",
					"insert_after": "auto_tone_mark",
				},{
					"fieldname": "gravure_proof_no",
					"fieldtype": "Select",
					"label": "Gravure Proof No",
					"insert_after": "gravure_proof_dt",
					"options":" \n1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
				},{
					"fieldname": "printing_right_section",
					"fieldtype": "Column Break",
					"label": "",
					"insert_after": "gravure_proof_no",
				},{
					"fieldname": "print_on_2",
					"fieldtype": "Select",
					"label": "Print On 2",
					"insert_after": "printing_right_section",
					"options":" \nALUMINIUM FOIL\nBOPP\nfoil\nLDPE-NATURAL\nMATT BOPP\nMATT PET\nMETALLIZE\nMETALLIZE WHITE\nMettalized BOPP\nMAILKY POLY\nNATURAL POLY\nPAPER\nPearal BOPP\nPER. BOPP\nPVC\nWHITE Poly"
				},{
					"fieldname": "ink_type",
					"fieldtype": "Select",
					"label": "Ink Type",
					"insert_after": "print_on_2",
					"options":" \nNCPU\nNTNK\nNTPU\nPAPER INK\nPU\nSAKATA\nUV\nVINAYL\nWATER BAS"
				},{
					"fieldname": "proof_match_with",
					"fieldtype": "Select",
					"label": "Proof Match With",
					"insert_after": "ink_type",
					"options":" \nold Job\nOUR  DIGTAL PRINT\nOU  TEST CUT\nPARTY  COOUR PRINT\nPRINED SAMPLE\nSHADE CARD"
				},{
					"fieldname": "eye_mark",
					"fieldtype": "Check",
					"label": "Eye Mark",
					"insert_after": "proof_match_with",
				},{
					"fieldname": "monogram",
					"fieldtype": "Check",
					"label": "Monogram",
					"insert_after": "eye_mark",
				},{
					"fieldname": "web_direction",
					"fieldtype": "Select",
					"label": "Web Direction",
					"insert_after": "monogram",
					"options": " \nUP\nDOWN"
				},{
					"fieldname": "coil_no",
					"fieldtype": "Check",
					"label": "Coil No",
					"insert_after": "web_direction",
				},{
					"fieldname": "colour_print_dt",
					"fieldtype": "Data",
					"label": "Colour Print Dt",
					"insert_after": "coil_no",
				},{
					"fieldname": "colour_print_no",
					"fieldtype": "Select",
					"label": "Colour Print No",
					"insert_after": "colour_print_dt",
					"options": " \n1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
				},
				#  Customer Addresses
				{
					"fieldname": "customer_address",
					"fieldtype": "Link",
					"label": "Primery Address",
					"options" : "Address",
					"insert_after": "company",
				},{
					"fieldname": "customer_invoice_address",
					"fieldtype": "Link",
					"label": "Invoice Address",
					"options" : "Address",
					"insert_after": "customer_address",
				},{
					"fieldname": "customer_address_party_delivery",
					"fieldtype": "Link",
					"label": "Customer Delivery Address",
					"options" : "Address",
					"insert_after": "customer_invoice_address",
				},{
					"fieldname": "customer_address_party_html",
					"fieldtype": "Read Only",
					"label": "Customer Party HTML Address",
					"options" : "Address",
					"insert_after": "customer_address_party_delivery",
				},
	#########	#  Marketing Section   #########	
				{
					"fieldname": "marketing_section_break",
					"fieldtype": "Section Break",
					"label": "Marketing",
					"insert_after": "colour_print_no",
				},{
					"fieldname": "marketing_instructions",
					"fieldtype": "Text",
					"label": "Marketing Instructions",
					"insert_after": "marketing_section_break",
				},{
					"fieldname": "marketing_copper_gap",
					"fieldtype": "Int",
					"label": "Copper Gap",
					"insert_after": "marketing_instructions",
				},{
					"fieldname": "marketing_dispatch_instructions",
					"fieldtype": "Text",
					"label": "Dispatch Instructions",
					"insert_after": "marketing_copper_gap",
				},{
					"fieldname": "marketing_column_break1",
					"fieldtype": "Column Break",
					"label": "",
					"insert_after": "marketing_dispatch_instructions",
				},{
					"fieldname": "marketing_expt_del_date",
					"fieldtype": "Date",
					"label": "Expt Del Date",
					"insert_after": "marketing_column_break1",
				},{
					"fieldname": "marketing_proj_del_date",
					"fieldtype": "Date",
					"label": "Proj Del Date",
					"insert_after": "marketing_expt_del_date",
				},{
					"fieldname": "marketing_ps_clear_date",
					"fieldtype": "Date",
					"label": "PS Clear Date",
					"insert_after": "marketing_proj_del_date",
				},{
					"fieldname": "marketing_fab_release_date",
					"fieldtype": "Date",
					"label": "Fab Release Date",
					"insert_after": "marketing_ps_clear_date",
				},{
					"fieldname": "marketing_column_break2",
					"fieldtype": "Column Break",
					"label": "",
					"insert_after": "marketing_fab_release_date",
				},{
					"fieldname": "marketing_delivery_date",
					"fieldtype": "Date",
					"label": "Delivery Date",
					"insert_after": "marketing_column_break2",
				},{
					"fieldname": "marketing_user",
					"fieldtype": "Link",
					"label": "Marketing Date",
					"options": "User",
					"insert_after":"marketing_delivery_date",
				},{
					"fieldname": "marketing_fab_release",
					"fieldtype": "Button",
					"label": "Fab Release",
					"insert_after": "marketing_user",
				},
	#########	#  Graphics Section   #########	
				{
					"fieldname": "graphics_section_break",
					"fieldtype": "Section Break",
					"label": "Graphics",
					"insert_after": "marketing_fab_release",
				},{
					"fieldname": "graphics_grainst",
					"fieldtype": "Text",
					"label": "GRAINST",
					"insert_after": "graphics_section_break",
				},{
					"fieldname": "graphics_column_break1",
					"fieldtype": "Column Break",
					"label": "",
					"insert_after": "graphics_grainst",
				},{
					"fieldname": "graphics_user",
					"fieldtype": "Data",
					"label": "Graphics User",
					"insert_after": "graphics_column_break1",
				},{
					"fieldname": "graphics_alguid",
					"fieldtype": "Date",
					"label": "ALGUID",
					"insert_after": "graphics_user",
				},{
					"fieldname": "graphics_status",
					"fieldtype": "Select",
					"label": "Status",
					"options": " \nActive\nInactive",
					"insert_after": "graphics_alguid",
				},{
					"fieldname": "graphics_column_break2",
					"fieldtype": "Column Break",
					"label": "",
					"insert_after": "graphics_status",
				},{
					"fieldname": "graphics_graph_date",
					"fieldtype": "Date",
					"label": "Graph Date",
					"insert_after": "graphics_column_break2",
				},{
					"fieldname": "graphics_entry_by",
					"fieldtype": "Link",
					"options": "User",
					"label": "Entry By",
					"insert_after": "graphics_graph_date",
				}
		],
	}


def after_install():
	create_custom_fields(get_custom_fields_after())


def get_custom_fields_after():
	print('\n\nget_custom_fields after\n\n')
	"""HR specific custom fields that need to be added to the masters in ERPNext"""
	return {
		"Customer": [
						{
							"fieldname": "pi_column_break",
							"fieldtype": "Column Break",
							"label": "",
							"insert_after": "pi_value",
						},{
							"fieldname": "drawing_details",
							"fieldtype": "Link",
							"label": "Drawing Details",
							"options": "Drawing Details",
							"insert_after": "pi_column_break",
						},{
							"fieldname": "customer_rate_section_break",
							"fieldtype": "Section Break",
							"label": "",
							"insert_after": "accounts"
						},{
							"fieldname": "customer_rate_details",
							"fieldtype": "Table",
							"label": "Rate",
							"options": "Rate Details",
							"insert_after": "customer_rate_section_break"
						},
					],
		"Work Order": [
						############    Drawing Section    #######
						{
							"fieldname": "drawing_section_break",
							"fieldtype": "Section Break",
							"label": "Drawing Section",
							"insert_after": "graphics_entry_by",
						},{
							"fieldname": "drawno",
							"fieldtype": "Link",
							"label": "Drawno",
							"options": "Drawing Details",
							"insert_after": "drawing_section_break",
						},{
							"fieldname": "boreod",
							"fieldtype": "Float",
							"label": "BOREOD",
							"insert_after": "drawno",
						},{
							"fieldname": "kwd",
							"fieldtype": "Float",
							"label": "KWD",
							"insert_after": "boreod",
						},{
							"fieldname": "remarks",
							"fieldtype": "Text",
							"label": "Remarks",
							"insert_after": "kwd",
						},{   
							"fieldname": "column_break0",
							"fieldtype": "Column Break",
							"label": "",
							"insert_after": "remarks",
						},{
							"fieldname": "type",
							"fieldtype": "Select",
							"label": "Type",
							"options": " \nHOLLOW\nSHAFTED",
							"insert_after": "column_break0",
						},{
							"fieldname": "flangethickness",
							"fieldtype": "Float",
							"label": "FLANGETHICKNESS",
							"insert_after": "type",
						},{
							"fieldname": "kwt",
							"fieldtype": "Select",
							"label": "KWT",
							"options": " \nPA\nPB",
							"insert_after": "flangethickness",
						},{   
							"fieldname": "column_break11",
							"fieldtype": "Column Break",
							"label": "",
							"insert_after": "kwt",
						},{
							"fieldname": "boreid",
							"fieldtype": "Float",
							"label": "BOREID",
							"insert_after": "column_break11",
						},{
							"fieldname": "kww",
							"fieldtype": "Float",
							"label": "KWW",
							"insert_after": "boreid",
						},{
							"fieldname": "degree",
							"fieldtype": "Float",
							"label": "Degree",
							"insert_after": "kww",
						},{
							"fieldname": "active",
							"fieldtype": "Check",
							"label": "Active",
							"insert_after": "degree",
						},
						#####    Job Details #####
						{
							"fieldname": "section_job_details",
							"fieldtype": "Section Break",
							"label": "Job Details",
							"insert_after": "mat_width",
						},{
							"fieldname": "job_details",
							"fieldtype": "Table",
							"label": "Job Details",
							"options": "Job Details",
							"insert_after": "section_job_details",
						}
					]
				}

def before_uninstall():
	print('\n\nbefore_uninstall\n\n')
	delete_custom_fields()


def delete_custom_fields():
	cu_custom = [
					"section_of_tab_break_for_extra_info",
					"pi_value",
					"printing_section",
					"print_side",
					"print_on",
					"artwork",
					"slitting_mark",
					"sr_mark",
					"auto_tone_mark",
					"gravure_proof_dt",
					"gravure_proof_no",
					"printing_right_section",
					"print_on_2",
					"ink_type",
					"proof_match_with",
					"eye_mark",
					"monogram",
					"web_direction",
					"coil_no",
					"colour_print_dt",
					"colour_print_no",
					"customer_rate_section",
					"customer_rate_section_break",
					"customer_rate_details",
					"drawing_details"
				]
	print('\n\n customer custom field delete\n')
	for customer in cu_custom:
		filters = {"fieldname": customer}

		for field in frappe.get_all("Custom Field", filters=filters):
			status = frappe.delete_doc("Custom Field", field.name)
			# print('\n\nstatus',str(status))
	
	frappe.clear_cache(doctype="Custom Field")

	wo_custom = [
					"section_of_customer_break_for_extra_info",
					"customer",
					"fab_roll",
					"fab_rate",
					"repeat_height",
					"step_width",
					"supp_roll",
					"supp_rate",
					"roller_dimensions",
					"x_repeat",
					"x_step",
					"circum",
					"len",
					"total_speciale",
					"total_roll",
					"special_rate",
					"dia",
					"pi_value",
					"total_column_break",
					"r_width",
					"add_width",
					"cylinder_length",
					"mat_width",
					"printing_section",
					"print_side",
					"print_on",
					"artwork",
					"slitting_mark",
					"sr_mark",
					"auto_tone_mark",
					"gravure_proof_dt",
					"gravure_proof_no",
					"printing_right_section",
					"print_on_2",
					"ink_type",
					"proof_match_with",
					"eye_mark",
					"monogram",
					"web_direction",
					"coil_no",
					"colour_print_dt",
					"colour_print_no",
					"customer_address",
					"customer_invoice_address",
					"customer_address_party_delivery",
					"customer_address_party_html",
					"marketing_section_break",
					"marketing_instructions",
					"marketing_copper_gap",
					"marketing_dispatch_instructions",
					"marketing_column_break1",
					"marketing_expt_del_date",
					"marketing_proj_del_date",
					"marketing_ps_clear_date",
					"marketing_fab_release_date",
					"marketing_column_break2",
					"marketing_delivery_date",
					"marketing_user",
					"marketing_fab_release",
					"graphics_section_break",
					"graphics_grainst",
					"graphics_column_break1",
					"graphics_user",
					"graphics_alguid",
					"graphics_status",
					"graphics_column_break2",
					"graphics_graph_date",
					"graphics_entry_by",
					"drawing_section_break",
					"drawno",
					"boreod",
					"kwd",
					"remarks",
					"column_break0",
					"type",
					"flangethickness",
					"kwt",
					"column_break11",
					"boreid",
					"kww",
					"degree",
					"active",
					"section_job_details",
					"job_details"
				]
	print('\n\n Work order custom field delete\n')
	for work in wo_custom:
		filters = {"fieldname": work}

		for field in frappe.get_all("Custom Field", filters=filters):
			status = frappe.delete_doc("Custom Field", field.name)
			# print('\n\nstatus',str(status))
	frappe.clear_cache(doctype="Custom Field")


def check_setup_wizard_not_completed():
	if cint(frappe.db.get_single_value("System Settings", "setup_complete") or 0):
		message = """ERPNext can only be installed on a fresh site where the setup wizard is not completed.
You can reinstall this site (after saving your data) using: bench --site [sitename] reinstall"""
		frappe.throw(message)  # nosemgrep


def set_single_defaults():
	for dt in (
		"Accounts Settings",
		"Print Settings",
		"Buying Settings",
		"Selling Settings",
		"Stock Settings",
	):
		default_values = frappe.db.sql(
			"""select fieldname, `default` from `tabDocField`
			where parent=%s""",
			dt,
		)
		if default_values:
			try:
				doc = frappe.get_doc(dt, dt)
				for fieldname, value in default_values:
					doc.set(fieldname, value)
				doc.flags.ignore_mandatory = True
				doc.save()
			except frappe.ValidationError:
				pass

	frappe.db.set_default("date_format", "dd-mm-yyyy")

	setup_currency_exchange()


def setup_currency_exchange():
	ces = frappe.get_single("Currency Exchange Settings")
	try:
		ces.set("result_key", [])
		ces.set("req_params", [])

		ces.api_endpoint = "https://frankfurter.app/{transaction_date}"
		ces.append("result_key", {"key": "rates"})
		ces.append("result_key", {"key": "{to_currency}"})
		ces.append("req_params", {"key": "base", "value": "{from_currency}"})
		ces.append("req_params", {"key": "symbols", "value": "{to_currency}"})
		ces.save()
	except frappe.ValidationError:
		pass


def create_print_setting_custom_fields():
	create_custom_fields(
		{
			"Print Settings": [
				{
					"label": _("Compact Item Print"),
					"fieldname": "compact_item_print",
					"fieldtype": "Check",
					"default": "1",
					"insert_after": "with_letterhead",
				},
				{
					"label": _("Print UOM after Quantity"),
					"fieldname": "print_uom_after_quantity",
					"fieldtype": "Check",
					"default": "0",
					"insert_after": "compact_item_print",
				},
				{
					"label": _("Print taxes with zero amount"),
					"fieldname": "print_taxes_with_zero_amount",
					"fieldtype": "Check",
					"default": "0",
					"insert_after": "allow_print_for_cancelled",
				},
			]
		}
	)


def create_default_cash_flow_mapper_templates():
	for mapper in DEFAULT_MAPPERS:
		if not frappe.db.exists("Cash Flow Mapper", mapper["section_name"]):
			doc = frappe.get_doc(mapper)
			doc.insert(ignore_permissions=True)


def create_default_success_action():
	for success_action in get_default_success_action():
		if not frappe.db.exists("Success Action", success_action.get("ref_doctype")):
			doc = frappe.get_doc(success_action)
			doc.insert(ignore_permissions=True)


def create_default_energy_point_rules():

	for rule in get_default_energy_point_rules():
		# check if any rule for ref. doctype exists
		rule_exists = frappe.db.exists(
			"Energy Point Rule", {"reference_doctype": rule.get("reference_doctype")}
		)
		if rule_exists:
			continue
		doc = frappe.get_doc(rule)
		doc.insert(ignore_permissions=True)


def add_company_to_session_defaults():
	settings = frappe.get_single("Session Default Settings")
	settings.append("session_defaults", {"ref_doctype": "Company"})
	settings.save()


def add_standard_navbar_items():
	navbar_settings = frappe.get_single("Navbar Settings")

	erpnext_navbar_items = [
		{
			"item_label": "Documentation",
			"item_type": "Route",
			"route": "https://erpnext.com/docs/user/manual",
			"is_standard": 1,
		},
		{
			"item_label": "User Forum",
			"item_type": "Route",
			"route": "https://discuss.erpnext.com",
			"is_standard": 1,
		},
		{
			"item_label": "Report an Issue",
			"item_type": "Route",
			"route": "https://github.com/frappe/erpnext/issues",
			"is_standard": 1,
		},
	]

	current_navbar_items = navbar_settings.help_dropdown
	navbar_settings.set("help_dropdown", [])

	for item in erpnext_navbar_items:
		current_labels = [item.get("item_label") for item in current_navbar_items]
		if not item.get("item_label") in current_labels:
			navbar_settings.append("help_dropdown", item)

	for item in current_navbar_items:
		navbar_settings.append(
			"help_dropdown",
			{
				"item_label": item.item_label,
				"item_type": item.item_type,
				"route": item.route,
				"action": item.action,
				"is_standard": item.is_standard,
				"hidden": item.hidden,
			},
		)

	navbar_settings.save()


def add_app_name():
	frappe.db.set_value("System Settings", None, "app_name", "ERPNext")


def setup_log_settings():
	log_settings = frappe.get_single("Log Settings")
	log_settings.append("logs_to_clear", {"ref_doctype": "Repost Item Valuation", "days": 60})

	log_settings.save(ignore_permissions=True)

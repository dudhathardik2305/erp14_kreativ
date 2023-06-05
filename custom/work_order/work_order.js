// Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Work Order", {
	refresh: function(frm) {
		// its loading and worked


    // frm.add_custom_button(__("Sales Order"), function() {
      // if (this.frm.doc.docstatus===0) {
            frm.add_custom_button(__('Sales Order'),
              function() {
                erpnext.utils.map_current_doc({
                  method: "erpnext.selling.doctype.quotation.quotation.make_sales_order",
                  source_doctype: "Sales Order",
                  target: me.frm,
                  setters: [
                    {
                      label: "Customer",
                      fieldname: "customer",
                      fieldtype: "Link",
                      options: "Customer",
                      default: me.frm.doc.customer || undefined
                    }
                  ],
                  get_query_filters: {
                    company: me.frm.doc.company,
                    docstatus: 1,
                    status: ["!=", "Lost"]
                  }
                })
              }, __("Create"));
          // }    
        // }, __("Create"));


    frm.add_custom_button(__("Expense Claim"), function() {
        frappe.call({
        method: "erp14_kreativ.erp14_kreativ.doctype.rate_details.rate_details.get_rate_details",
        args: {
          doctype: "Customer",
          name: frm.doc.customer
        },
      callback: function(r) {
        // // Update the Work Order Printing Section custom fields with the customer data
        // frm.set_value("drawno", r.message.name);
        // frm.set_value("boreod", r.message.boreod);
        // frm.set_value("kwd", r.message.kwd);
        // frm.set_value("remarks", r.message.remarks);
        // frm.set_value("type", r.message.type);
        // frm.set_value("flangethickness", r.message.flangethickness);
        // frm.set_value("kwt", r.message.kwt);
        // frm.set_value("boreid", r.message.boreid);
        // frm.set_value("kww", r.message.kww);
        // frm.set_value("degree", r.message.degree);
        // frm.set_value("active", r.message.active);
      }
    });
      }, __("Create"));
	},

  

	customer: function(frm) {
    
    // Get the customer document based on the selected customer in the Work Order
    frappe.call({
      method: "frappe.client.get",
      args: {
        doctype: "Customer",
        name: frm.doc.customer
      },
      callback: function(r) {
        // Update the Work Order Printing Section custom fields with the customer data
        frm.set_value("print_side", r.message.print_side);
        frm.set_value("print_on", r.message.print_on);
        frm.set_value("artwork", r.message.artwork);
        frm.set_value("slitting_mark", r.message.slitting_mark);
        frm.set_value("sr_mark", r.message.sr_mark);
        frm.set_value("auto_tone_mark", r.message.auto_tone_mark);
        frm.set_value("gravure_proof_dt", r.message.gravure_proof_dt);
        frm.set_value("gravure_proof_no", r.message.gravure_proof_no);
        
        // Update the Work Order printing right section fields with the customer data
        frm.set_value("print_on_2", r.message.print_on_2);
        frm.set_value("ink_type", r.message.ink_type);
        frm.set_value("proof_match_with", r.message.proof_match_with);
        frm.set_value("eye_mark", r.message.eye_mark);
        frm.set_value("monogram", r.message.monogram);
        frm.set_value("web_direction", r.message.web_direction);
        frm.set_value("coil_no", r.message.coil_no);
        frm.set_value("colour_print_dt", r.message.colour_print_dt);
        frm.set_value("colour_print_no", r.message.colour_print_no);

        frm.set_value("pi_value", r.message.pi_value);
        frm.set_value("customer_address_party_delivery", r.message.customer_primary_address);
      }
    });

    //set data for drawing details 

      frappe.call({
        method: "erp14_kreativ.erp14_kreativ.doctype.drawing_details.drawing_details.get_drawing_details_customer",
        args: {
          doctype: "Customer",
          name: frm.doc.customer
        },
      callback: function(r) {
          // // Update the Work Order Printing Section custom fields with the customer data
          frm.set_value("drawno", r.message.name);
          frm.set_value("boreod", r.message.boreod);
          frm.set_value("kwd", r.message.kwd);
          frm.set_value("remarks", r.message.remarks);
          frm.set_value("type", r.message.type);
          frm.set_value("flangethickness", r.message.flangethickness);
          frm.set_value("kwt", r.message.kwt);
          frm.set_value("boreid", r.message.boreid);
          frm.set_value("kww", r.message.kww);
          frm.set_value("degree", r.message.degree);
          frm.set_value("active", r.message.active);
        }
      });

    // set rate details 
    if (frm.doc.production_item && frm.doc.customer){
      frappe.call({
        method: "erp14_kreativ.erp14_kreativ.doctype.rate_details.rate_details.get_rate_details",
        args: {
          doctype: "Customer",
          name: frm.doc.customer,
          item: frm.doc.production_item,
        },
      callback: function(r) {
        console.log('\n\n rate details', r.message);
          // Update the Work Order Printing Section custom fields with the customer data
          frm.set_value("fab_rate", r.message.customer_rate);
          frm.set_value("expected_delivery_date", r.message.expacted_date);
        }
      });
    }

  // frm.trigger("set_address_html");
  },

  customer_address_party_delivery: function(frm) {
    if(frm.doc.customer_address_party_delivery){
      frappe.call({
        method: 'frappe.contacts.doctype.address.address.get_address_display',
        args: {
          "address_dict": frm.doc.customer_address_party_delivery
        },
        callback: function(r) {
          frm.set_value("customer_address_party_html", r.message);
        }
      });
    }
    if(!frm.doc.customer_primary_address){
      frm.set_value("customer_address_party_html", "");
    }
  },

  marketing_fab_release: function(frm){
    frappe.confirm(
        __("Are you sure you want to set current date to Fab Date"),
        () => {
                frm.set_value('marketing_fab_release_date', frappe.datetime.get_today());
        }
      );
    },

  fab_roll: function(frm){
    var tableField = frm.fields_dict['job_details'].grid.remove_all();
    var tableFieldadd = frm.fields_dict['job_details'].grid;
    for (var row = 0; frm.doc.fab_roll > row; row++ ){
      var newRow = tableFieldadd.add_new_row();
      frappe.model.set_value(newRow.doctype, newRow.name, 'color', '');
    }
    tableFieldadd.refresh();
    // update Qty in Manufacturing
    if(frm.doc.supp_roll == undefined || frm.doc.supp_roll == null){
          frm.set_value("supp_roll", 0.00);
    }

    var total_qty = frm.doc.fab_roll * frm.doc.supp_roll;
    frm.set_value("qty", total_qty);
    
    //update total roll
    var total_roll = frm.doc.fab_roll + frm.doc.supp_roll;
    frm.set_value("total_roll", total_roll);
  },

  supp_roll: function(frm){
    //update qty in manufacturing
    if(frm.doc.fab_roll == undefined || frm.doc.fab_roll == null){
          frm.set_value("fab_roll", 0.00);
    }
    
    var total_qty = frm.doc.fab_roll * frm.doc.supp_roll;
    frm.set_value("qty", total_qty);
    
    //update total roll
    var total_roll = frm.doc.fab_roll + frm.doc.supp_roll;
    frm.set_value("total_roll", total_roll);
  },

  x_repeat: function(frm){
    if (frm.doc.repeat_height == undefined || frm.doc.repeat_height == null){
      frm.set_value("repeat_height", 0.00);
    }
    var total_circum = frm.doc.repeat_height * frm.doc.x_repeat;
    frm.set_value("circum", total_circum);
  },

  repeat_height: function(frm){
    if (frm.doc.x_repeat == undefined || frm.doc.x_repeat == null){
      frm.set_value("x_repeat", 0.00);
    }
    var total_circum = frm.doc.repeat_height * frm.doc.x_repeat;
    frm.set_value("circum", total_circum);
  },

  x_step: function(frm){
      if (frm.doc.step_width == undefined || frm.doc.step_width == null){
        frm.set_value("step_width", 0.00);
        frm.refresh_field('step_width');
      }
      var total_len = frm.doc.x_step * frm.doc.step_width;
      frm.set_value("len", total_len);
      frm.refresh_field('len');
    },

  step_width: function(frm){
      if (frm.doc.x_step == undefined || frm.doc.x_step == null){
        frm.set_value("x_step", 0.00);
        frm.refresh_field('x_step');
      }
      var total_len = frm.doc.x_step * frm.doc.step_width;
      frm.set_value("len", total_len);
      frm.refresh_field('len');
    },

  circum: function(frm){
      if (frm.doc.pi_value == undefined || frm.doc.pi_value == null){
        frappe.msgprint("Set Customer");
      }
      var total_dia = frm.doc.circum / frm.doc.pi_value;
      frm.set_value("dia", total_dia);
      frm.refresh_field('dia');

      // set tmm
      frm.set_value("cylinder_length", 1.0);
      frm.refresh_field('cylinder_length');
      var total_tmm = (frm.doc.circum * frm.doc.cylinder_length) / 1000;
      frm.set_value("tmm", total_tmm);
      frm.refresh_field('dia');

    },

  r_width: function(frm){
      if (frm.doc.len == undefined || frm.doc.len == null){
        frm.set_value('len', 0.00);
      }
      if (frm.doc.add_width == undefined || frm.doc.add_width == null){
        frm.set_value('add_width', 0.00);
      }
      var c_total = frm.doc.len + frm.doc.add_width + frm.doc.r_width;
      frm.set_value('cylinder_length', c_total);
  },
    
  cylinder_length: function(frm){
    if (frm.doc.circum == undefined || frm.doc.circum == null){
      frappe.msgprint("Please Calculate Circum First");
    }
    var total_tmm = (frm.doc.circum * frm.doc.cylinder_length) / 1000;
    frm.set_value("tmm", total_tmm);
    frm.refresh_field('tmm');
  },

  len: function(frm){
      if (frm.doc.r_width == undefined || frm.doc.r_width == null){
        frm.set_value('r_width', 0.00);
      }
      if (frm.doc.add_width == undefined || frm.doc.add_width == null){
        frm.set_value('add_width', 0.00);
      }
      var c_total = frm.doc.len + frm.doc.add_width + frm.doc.r_width;
      frm.set_value('cylinder_length', c_total);
  },

  add_width: function(frm){
      if (frm.doc.len == undefined || frm.doc.len == null){
        frm.set_value('r_width', 0.00);
      }
      if (frm.doc.r_width == undefined || frm.doc.r_width == null){
        frm.set_value('add_width', 0.00);
      }
      var c_total = frm.doc.len + frm.doc.add_width + frm.doc.r_width;
      frm.set_value('cylinder_length', c_total);
  }
});

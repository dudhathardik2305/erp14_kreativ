// Copyright (c) 2023, Self and contributors
// For license information, please see license.txt

frappe.ui.form.on('Inward Master', {
	refresh: function(frm) {
		frm.set_value("entry_by", frappe.session.user);
	}
});

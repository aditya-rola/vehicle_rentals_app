// Copyright (c) 2025, Adi and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
  refresh(frm) {
    console.log("CALLING >>>>>>")
  },
  rate(frm) {
    console.log("CALLING >>>>>>")

    frm.trigger("update_total_amount");
  },
  update_total_amount(frm) {
    let total_d = 0;
    for (let itm of frm.doc.items) {
      total_d += itm.distance;
    }

    const amount = frm.doc.rate * total_d;
    frm.set_value("total_amount", amount);
  },
});

frappe.ui.form.on("Ride Booking item", {
  refresh(frm) {},
  distance(frm) {
    frm.trigger("update_total_amount");
  },
  items_remove(frm){
    frm.trigger("update_total_amount")
  }
});

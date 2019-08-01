import frappe
from frappe.core.doctype.sms_settings.sms_settings import send_sms

def customer_sms(doc, method):
	customer = doc.customer
	contact_mobile = doc.contact_mobile
	if customer and contact_mobile and doc.is_pos == 1:
		oralcare_settings = frappe.get_doc('Oralcare Settings')
		customer_sms_message = oralcare_settings.customer_sms
		context = {"doc": doc}
		msg = frappe.render_template(customer_sms_message, context)
		mobno = [contact_mobile]
		send_sms(mobno, msg)

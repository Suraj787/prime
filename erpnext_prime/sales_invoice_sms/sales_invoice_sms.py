import frappe
from frappe.core.doctype.sms_settings.sms_settings import send_sms

def customer_sms(doc, method):
	customer = doc.customer
	contact_mobile = doc.contact_mobile
	if customer and contact_mobile and doc.is_pos == 1:
		prime_sms = frappe.get_doc('SMS Prime')
		customer_sms_message = prime_sms.customer_sms
		context = {"doc": doc}
		msg = frappe.render_template(customer_sms_message, context)
		mobno = [contact_mobile]
		send_sms(mobno, msg)

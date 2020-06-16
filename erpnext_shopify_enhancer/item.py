import frappe
import json
@frappe.whitelist(allow_guest=True)
def truncate_item_name_from_shopify(self,name):
    # print(frappe._dict(self))
    print('---'*100,self.item_name)
    frappe.msgprint('Inside truncate_item_name_from_shopify',self.item_name)
    enable_shopify=frappe.db.get_single_value('Shopify Settings', 'enable_shopify')
    print('enable_shopify',enable_shopify)
    frappe.msgprint('enable_shopify',enable_shopify)
    if enable_shopify==1:
        print('1'*100,self.item_name)
        frappe.msgprint('sync_with_shopify',self.item_name)
        self.item_name=self.item_name[0:140]
        frappe.msgprint('after sync_with_shopify',self.item_name)
        print('2'*100,self.item_name)
        # return self

@frappe.whitelist(allow_guest=True)
def truncate_item_name_from_shopify_for_SO(self,name):
    for item in self.items:
        item.item_name

@frappe.whitelist(allow_guest=True)
def kartra_simple_call():
    print('##'*100)
    print(frappe.local.form_dict)
    x=frappe.local.form_dict
    frappe.msgprint('Inside kartra_simple_call')
    frappe.msgprint('Inside kartra_simple_call',x)



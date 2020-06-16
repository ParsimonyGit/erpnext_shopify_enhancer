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


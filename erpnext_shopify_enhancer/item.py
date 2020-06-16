import frappe
import json
from frappe.utils import add_to_date, date_diff, getdate, nowdate
from frappe import _

@frappe.whitelist(allow_guest=True)
def truncate_item_name_from_shopify(self,name):
    # print(frappe._dict(self))
    print('---'*100,self.item_name)
    frappe.msgprint('Inside truncate_item_name_from_shopify',self.item_name)
    enable_shopify=frappe.db.get_single_value('Shopify Settings', 'enable_shopify')
    print('enable_shopify',enable_shopify)
    frappe.msgprint('enable_shopify',enable_shopify)
    if enable_shopify==1 and self.shopify_product_id:
        print('1'*100,self.item_name)
        frappe.msgprint('sync_with_shopify',self.item_name)
        self.item_name=self.item_name[0:140]
        frappe.msgprint('after sync_with_shopify',self.item_name)
        print('2'*100,self.item_name)
        # return self

@frappe.whitelist(allow_guest=True)
def truncate_item_name_from_shopify_for_SO(self,name):
    enable_shopify=frappe.db.get_single_value('Shopify Settings', 'enable_shopify')
    if  enable_shopify==1 and self.shopify_order_id:
        for item in self.items:
            item.item_name=item.item_name[0:140]

@frappe.whitelist(allow_guest=True)
def kartra_simple_call(**data):
    print('55'*100)
    doc = frappe.new_doc('Task')
    doc.subject=nowdate()
    doc.description=json.dumps(frappe.form_dict.get("action_details",{}).get("transaction_details",{})) or frappe.form_dict.get("action") 
    print('66'*100)
    print(doc.description,'-----')
    doc.insert(ignore_permissions=True)    
    frappe.db.commit()



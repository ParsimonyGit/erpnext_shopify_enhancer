import frappe
import json
from frappe.utils import add_to_date, date_diff, getdate, nowdate
from frappe import _

@frappe.whitelist(allow_guest=True)
def truncate_item_name_from_shopify(self,name):
    enable_shopify=frappe.db.get_single_value('Shopify Settings', 'enable_shopify')
    if enable_shopify==1 and self.shopify_product_id:
        self.item_name=self.item_name[0:140]

@frappe.whitelist(allow_guest=True)
def truncate_item_name_from_shopify_for_SO(self,name):
    enable_shopify=frappe.db.get_single_value('Shopify Settings', 'enable_shopify')
    if  enable_shopify==1 and self.shopify_order_id:
        for item in self.items:
            item.item_name=item.item_name[0:140]

# hook is not required for SI and Delivery Note as both of these doctypes are made based on SO.            
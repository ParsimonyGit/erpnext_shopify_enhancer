import frappe

@frappe.whitelist(allow_guest=True)
def truncate_item_name_from_shopify(self,name):
    enable_shopify=frappe.db.get_single_value('Shopify Settings', 'enable_shopify')
    if enable_shopify==1:
        if self.sync_with_shopify==1:
            if len(self.item_name)>140:
                self.item_name=self.item_name[0:140]

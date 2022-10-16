import frappe
from ecta_dispatch.api.ecta_webpage_permission_api import checkPermisson

def get_context(context):
  context.UserAvatar = frappe.session.user.upper()[0]
  context.user = frappe.session.user
  context.side_bar_ecta =frappe.get_doc('ECTA Sidebar', 'ECTA sidebar')
  context.side_bar_group = "ECTA"
  context.uid= frappe.session.user
  context.first_name = frappe.db.get_value('User', {'username': context.uid}, ['first_name'])
#   context.new_dispatches = frappe.db.get_list("ECTA Dispatches", filters={'file_attached_by':frappe.session.user}, fields=['center','exporter_name','sent_warehouse','exporter_type','name','creation','excel_import'])
  def calculateSumFromDispatch(): 
    sumofKG = 0
    sumofBag = 0
    i = 0
    for items in context.dispatches:
      sumofKG += context.dispatches[i]['volume_in_ton']
      sumofBag += context.dispatches[i]['volume_in_bag']
      i = i+1
      
    # context.warehouse = frappe.db.get_list("Warehouse",'*',filters={'warehouse_name':"Goods In Transit"});
    context.sumofKG = sumofKG
    context.sumofBag = sumofBag
  
  if checkPermisson("ecta"):
    context.dispatches = frappe.db.get_list("ECTA Dispatches", fields=['name','center','exporter_name','sent_warehouse','exporter_type','name','creation','excel_import','status', 'proof_of_delivery','name','approved', 'serial_number', 'modified','volume_in_bag','volume_in_ton','received_volume_in_bag','received_volume_in_ton'], order_by='status asc')
    calculateSumFromDispatch()
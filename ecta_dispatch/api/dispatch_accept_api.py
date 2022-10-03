
import frappe

@frappe.whitelist()

def dispatchAcceptanceForm(**args):
    
    doc = frappe.get_doc({
                    'doctype': 'ECTA Dispatches',
                    'id':args.get('warehouseName'),
                    'received_volume_in_bag': args.get('volumeInBag'),
                    'received_volume_in_ton': args.get('volumeInTon'),
                    #'proof_of_delivery': args.get('volumeIn'),
                    'status':args.get('status'),
                   
                })
    doc.insert()
    doc.save()
    frappe.db.commit()
    return "updated"
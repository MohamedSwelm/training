from odoo import fields, models

class RejectedReason(models.TransientModel):
    _name='rejected.reason'

    rejection_reason = fields.Text(required=True)
    purchase_request_id = fields.Many2one('purchase.request')

    
    
    def action_confirm(self):
        request_id = self.env['purchase.request'].search([('rejection_reason','=',self.purchase_request_id.rejection_reason)])
        print(request_id)
        request_id.write({
            'rejection_reason':self.rejection_reason,
            'status':'reject'
        })
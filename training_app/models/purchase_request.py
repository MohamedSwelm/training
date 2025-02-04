from odoo import models, fields, api



class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'purchase request model'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(required=True, string="Request Name")
    requested_by = fields.Many2one('res.users', required=True, default=lambda self: self.env.user.id)
    start_date = fields.Date(default=fields.date.today())
    end_date = fields.Date()
    rejection_reason = fields.Text(readonly=True)
    order_lines = fields.One2many('purchase.request.line', 'purchase_request_line_id')
    total_price = fields.Float(compute='_compute_total_price')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('to be approved', 'To Be Approved'),
        ('approved', 'Approved'),
        ('reject', 'Reject'),
        ('cancelled', 'Cancelled'),
    ],default='draft')

    @api.depends('order_lines.total')
    def _compute_total_price(self):
        for rec in self:
            total_price = 0
            for rec_line in rec.order_lines:
                total_price += rec_line.total
                print(total_price)
            rec.total_price = total_price

    def change_state_approval(self):
        for rec in self:
            rec.status ='approved'
            rec._send_approval_email()



    def _send_approval_email(self):
        purchase_manager_group = self.env.ref('training_app.training_manager_group')
        purchase_managers = purchase_manager_group.users
        print(purchase_managers)
        mail_values = {
            'subject': f"Purchase Request {self.name} has been approved",
            'email_from': self.env.user.email or 'noreply@example.com',
        }
        mail = self.env['mail.mail'].create(mail_values)
        print(mail)
        mail.send()

    def change_state_to_be_approved(self):
        for rec in self:
            rec.status = 'to be approved'

    def change_state_draft(self):
        for rec in self:
            rec.status = 'draft'

    def change_state_reject(self):
        for rec in self:
            action = rec.env['ir.actions.actions']._for_xml_id('training_app.rejected_reason_action')
            return action

    def change_state_cancelled(self):
        for rec in self:
            rec.status = 'cancelled'


class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'
    _description = 'purchase request line'

    purchase_request_line_id = fields.Many2one('purchase.request')
    product_id = fields.Many2one('product.product', required=True)
    description = fields.Char(related="product_id.name")
    quantity = fields.Float(default=1)
    cost_price = fields.Float(readonly=True, related="product_id.standard_price")
    total = fields.Float(compute='_compute_total', readonly=True)

    @api.depends('quantity', 'cost_price')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.cost_price * rec.quantity

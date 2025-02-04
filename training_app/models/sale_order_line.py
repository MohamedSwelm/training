from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    dimension = fields.Char(string='Dimension')


    @api.onchange('product_id')
    def onchange_dimension_value(self):
        if self.product_id:
            self.dimension =self.product_id.dimension



from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit='stock.move'

    dimension = fields.Char()

    @api.model
    def create(self, vals):
        sale_line = self.env['sale.order.line'].browse(vals['sale_line_id'])
        print(sale_line)
        vals['dimension'] = sale_line.dimension
        return super(StockPicking, self).create(vals)


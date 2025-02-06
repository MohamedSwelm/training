from odoo import fields, models, api

class StockMove(models.Model):
    _inherit='stock.move'

    dimension = fields.Char()

    @api.model
    def create(self, vals):
        print(vals)
        sale_line = self.env['sale.order.line'].browse(vals['sale_line_id'])
        print(sale_line)
        print(sale_line.dimension)
        vals['dimension'] = sale_line.dimension
        print(vals['dimension'])
        return super(StockMove,self).create(vals)


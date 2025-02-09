from odoo import fields, models, api

class StockRuleInherit(models.Model):
    _inherit = 'stock.rule'
    dimension = fields.Char()


    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_dest_id, name, origin, company_id, values):
        move_values = super()._get_stock_move_values(
            product_id, product_qty, product_uom, location_dest_id, name, origin, company_id, values)
        sale_line = values.get('sale_line_id')
        sale_line_rec = self.env['sale.order.line'].browse(sale_line)
        values['dimension']= sale_line_rec.dimension
        move_values['dimension'] = values['dimension']
        return move_values

class StockMove(models.Model):
    _inherit='stock.move'

    dimension = fields.Char()







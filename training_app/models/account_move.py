from odoo import fields, models, api

class AccountMove(models.Model):
    _inherit='account.move'


    dimension = fields.Char()


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    dimension = fields.Char(readonly=True)

    # @api.model
    # def create(self, vals_list):
    #     print(vals_list)
    #     stock_move_id = self.env['stock.move'].browse(vals_list['move_id'])
    #     print(stock_move_id)
    #     print(stock_move_id.name)
    #     print(stock_move_id.dimension)
    #     return super(AccountMoveLine, self).create(vals_list)

    @api.model
    def create(self, vals_list):
        move_lines = super(AccountMoveLine,self).create(vals_list)
        for move_line in move_lines:
            if move_line.sale_line_ids:
                stock_move = self.env["stock.move"].search([
                    ('sale_line_id', 'in', move_line.sale_line_ids.ids),
                    ('state', '=', 'done')  # Ensure move is completed
                ], limit=1, order="date desc")

                if stock_move and hasattr(stock_move, 'dimension'):
                    move_line.dimension = stock_move.dimension

        return move_lines








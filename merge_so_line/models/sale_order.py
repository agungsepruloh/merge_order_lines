from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @staticmethod
    def merge_duplicate_product_lines(res):
        for line in res.order_line:
            if line.id in res.order_line.ids:
                line_ids = res.order_line.filtered(lambda m: m.product_id.id == line.product_id.id)
                line_ids[0].product_uom_qty = sum(line_ids.mapped('product_uom_qty'))
                line_ids[1:].unlink()

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        auto_merge_so_line = self.env['ir.config_parameter'].sudo().get_param('merge_so_line.auto_merge_so_line', False)
        if bool(auto_merge_so_line):
            self.merge_duplicate_product_lines(res)
        return res

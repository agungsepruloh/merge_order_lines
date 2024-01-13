from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def merge_duplicate_product_lines(self, res):
        auto_merge_po_line = self.env['ir.config_parameter'].sudo().get_param('merge_po_line.auto_merge_po_line', False)
        if bool(auto_merge_po_line):
            for line in res.order_line:
                if line.id in res.order_line.ids:
                    line_ids = res.order_line.filtered(lambda m: m.product_id.id == line.product_id.id)
                    line_ids[0].product_qty = sum(line_ids.mapped('product_qty'))
                    line_ids[1:].unlink()

    @api.model
    def create(self, vals):
        res = super(PurchaseOrder, self).create(vals)
        self.merge_duplicate_product_lines(res)
        return res

    def write(self, vals):
        res = super(PurchaseOrder, self).write(vals)
        self.merge_duplicate_product_lines(self)
        return res

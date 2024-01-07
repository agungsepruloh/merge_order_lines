from odoo.tests import common


class TestSaleOrder(common.TransactionCase):
    def setUp(self):
        super(TestSaleOrder, self).setUp()
        self.SaleOrder = self.env['sale.order']
        self.customer = self.env.ref('base.res_partner_1')
        self.product = self.env.ref('product.product_product_25')

    def test_inactive_merge_duplicate_product_lines(self):
        self.env['ir.config_parameter'].sudo().set_param('merge_so_line.auto_merge_so_line', False)
        sale_order = self.SaleOrder.create({
            'partner_id': self.customer.id,
            'order_line': [
                (0, 0, {'product_id': self.product.id, 'product_uom_qty': 1}),
                (0, 0, {'product_id': self.product.id, 'product_uom_qty': 2})
            ]
        })
        self.assertEqual(len(sale_order.order_line), 2)

    def test_active_merge_duplicate_product_lines(self):
        self.env['ir.config_parameter'].sudo().set_param('merge_so_line.auto_merge_so_line', True)
        sale_order = self.SaleOrder.create({
            'partner_id': self.customer.id,
            'order_line': [
                (0, 0, {'product_id': self.product.id, 'product_uom_qty': 1}),
                (0, 0, {'product_id': self.product.id, 'product_uom_qty': 2})
            ]
        })
        self.assertEqual(len(sale_order.order_line), 1)
        self.assertEqual(sale_order.order_line.product_uom_qty, 3)

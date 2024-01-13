from odoo.tests import common


class TestPurchaseOrder(common.TransactionCase):
    def setUp(self):
        super(TestPurchaseOrder, self).setUp()
        self.PurchaseOrder = self.env['purchase.order']
        self.customer = self.env.ref('base.res_partner_1')
        self.product = self.env.ref('product.product_product_25')

    def test_inactive_merge_duplicate_product_lines(self):
        self.env['ir.config_parameter'].sudo().set_param('merge_po_line.auto_merge_po_line', False)
        purchase_order = self.PurchaseOrder.create({
            'partner_id': self.customer.id,
            'order_line': [
                (0, 0, {'product_id': self.product.id, 'product_qty': 1}),
                (0, 0, {'product_id': self.product.id, 'product_qty': 2})
            ]
        })
        self.assertEqual(len(purchase_order.order_line), 2)

    def test_active_merge_duplicate_product_lines(self):
        self.env['ir.config_parameter'].sudo().set_param('merge_po_line.auto_merge_po_line', True)
        purchase_order = self.PurchaseOrder.create({
            'partner_id': self.customer.id,
            'order_line': [
                (0, 0, {'product_id': self.product.id, 'product_qty': 1}),
                (0, 0, {'product_id': self.product.id, 'product_qty': 2})
            ]
        })
        self.assertEqual(len(purchase_order.order_line), 1)
        self.assertEqual(purchase_order.order_line.product_qty, 3)

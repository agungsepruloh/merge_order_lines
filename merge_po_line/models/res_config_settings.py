from odoo import models, fields, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    auto_merge_po_line = fields.Boolean(string="Auto Merge Purchase Order Line", config_parameter='merge_po_line.auto_merge_po_line')

from odoo import models, fields, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    auto_merge_so_line = fields.Boolean(string="Auto Merge Sale Order Line", config_parameter='merge_so_line.auto_merge_so_line')

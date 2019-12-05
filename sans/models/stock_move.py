# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

class StockMove(models.Model):
    _inherit = "stock.move"

    def create(self, vals):
        res = super(StockMove, self).create(vals)
        return res

    def write(self, vals):
        res = super(StockMove, self).write(vals)
        if self.picking_id:
            self.picking_id.event_reasign()
        return res
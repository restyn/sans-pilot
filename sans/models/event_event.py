# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

class Event(models.Model):
    _inherit = 'event.event'

    print_vendor_id = fields.Many2one(
        'res.partner', string='Print Vendor',
        tracking=True)

    dropship_location_id = fields.Many2one(
        'res.partner', string='Dropship Ship Location', help="Dropship Ship Location, defaults to event location",
        tracking=True)

    warehouse_location_id = fields.Many2one(
        'res.partner', string='Warehouse Ship Location', help="Warehouse Ship Location, defaults to event location",
        tracking=True)

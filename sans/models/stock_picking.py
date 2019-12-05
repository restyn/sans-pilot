# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    attendees = fields.One2many('event.registration','sale_order_id', related="sale_id.attendees")

    def event_reasign(self):
        o = self
        s = o['state']
        msg = ""
        if o["picking_type_id"] == 19:
            if o['move_line_ids_without_package']['location_id']['name'] == 'Sir Speedy Warehouse Stock':
                o['state'] = 'draft'
                o['location_id'] = o['move_line_ids_without_package']['location_id']['id']
                o["picking_type_id"] = 7
                o['state'] = s
            elif o['move_line_ids_without_package']['location_id']['name'] == 'SANS Warehouse Stock':
                o['state'] = 'draft'
                o['location_id'] = o['move_line_ids_without_package']['location_id']['id']
                o["picking_type_id"] = 2
                o['state'] = s

        msg += o['name'] + ' ' + str(o['location_id']['name']) + '\n'
        msg += '\tpicking_type_id: ' + str(o["picking_type_id"]["name"]) + '\n'

        e = o['attendees'].mapped('event_id')
        if len(e.ids) > 0:
            msg += '\t ' + str(e['name']) + '\n'
            if e['warehouse_location_id']:
                msg += '\twarehouse_location_id: ' + str(e['warehouse_location_id']) + '\n'
                o['partner_id'] = e['warehouse_location_id']
            else:
                msg += '\taddress:' + str(e['address_id']) + '\n'
                o['partner_id'] = e['address_id']

        print(msg)
        return
# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class EventRegistration(models.Model):
    _inherit = 'event.registration'

    street = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Char("State")

    @api.model
    def _prepare_attendee_values(self, registration):
        """ Override to add address related stuff """
        att_data = super(EventRegistration, self)._prepare_attendee_values(registration)
        if att_data:
            att_data.update({
                'street': registration.get('street', False),
                'city': registration.get('city', False),
                'state_id': registration.get('state_id', False),
                'zip': registration.get('zip', False),
            })
        return att_data
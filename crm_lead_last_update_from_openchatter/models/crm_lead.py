# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, fields


class CRMLead(models.Model):
    _name = "crm.lead"
    _inherit = [
        "crm.lead",
    ]

    @api.depends(
        "write_date",
    )
    @api.multi
    def _compute_last_update_openchatter(self):
        for document in self:
            document.last_update_openchatter = \
                document.message_ids[0].create_date

    last_update_openchatter = fields.Datetime(
        string="Last Update from OpenChatter",
        compute="_compute_last_update_openchatter",
        store=True,
    )

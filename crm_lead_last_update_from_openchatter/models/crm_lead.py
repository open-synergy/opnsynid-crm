# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api, fields, models


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
            document.last_update_openchatter = False
            if (
                len(
                    document.message_ids.filtered(
                        lambda r: r.create_uid != SUPERUSER_ID
                    )
                )
                > 0
            ):
                document.last_update_openchatter = document.message_ids.filtered(
                    lambda r: r.create_uid != SUPERUSER_ID
                )[0].create_date

    last_update_openchatter = fields.Datetime(
        string="Last Update from OpenChatter",
        compute="_compute_last_update_openchatter",
        store=True,
    )

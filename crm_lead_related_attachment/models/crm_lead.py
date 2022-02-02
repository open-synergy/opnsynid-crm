# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, models


class CRMLead(models.Model):
    _inherit = [
        "crm.lead",
        "mixin.related_attachment",
    ]
    _name = "crm.lead"

    @api.onchange(
        "partner_id",
        "user_id",
        "team_id",
        "funnel_type_id",
    )
    def onchange_related_attachment_template_id(self):
        super(CRMLead, self)._onchange_related_attachment_template_id()

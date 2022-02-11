# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, models


class CRMLead(models.Model):
    _inherit = [
        "crm.lead",
        "mixin.custom_info",
    ]
    _name = "crm.lead"

    @api.onchange(
        "partner_id",
        "user_id",
        "team_id",
        "funnel_type_id",
    )
    def onchange_custom_info_template_id(self):
        self.custom_info_template_id = self._get_template_custom_info()

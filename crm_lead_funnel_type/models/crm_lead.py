# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class CRMLead(models.Model):
    _inherit = "crm.lead"

    funnel_type_id = fields.Many2one(
        string="Funnel Type",
        comodel_name="crm.funnel_type"
    )

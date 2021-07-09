# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class CRMLead(models.Model):
    _inherit = "crm.lead"

    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Salesperson",
        readonly=True,
        default=False
    )

    salesperson_history_ids = fields.One2many(
        string="Salesperson History",
        comodel_name="crm.lead.salesperson_history",
        inverse_name="lead_id",
        readonly=True,
    )

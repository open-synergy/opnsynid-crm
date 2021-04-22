# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class CRMStageChangeConstrainTemplate(models.Model):
    _name = "crm.stage_change_constrain_template"
    _description = "CRM Lead State Change Constrain Template"

    name = fields.Char(
        string="Name",
        required=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    sequence = fields.Integer(
        string="Sequence",
        default=1,
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    description = fields.Text(
        string="Description",
    )
    python_code = fields.Text(
        string="Python Code",
        required=True,
        default="result = False",
    )
    detail_ids = fields.One2many(
        string="Details",
        comodel_name="crm.stage_change_constrain_detail",
        inverse_name="template_id",
    )

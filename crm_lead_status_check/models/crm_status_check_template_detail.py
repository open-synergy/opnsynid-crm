# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class CRMStatusCheckTemplateDetail(models.Model):
    _name = "crm.status_check_template_detail"
    _description = "CRM Status Check Template Detail"

    template_id = fields.Many2one(
        string="Status Check Template",
        comodel_name="crm.status_check_template",
        ondelete="cascade",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
    )
    status_check_item = fields.Many2one(
        string="Status Check Item",
        comodel_name="crm.status_check_item",
        ondelete="restrict",
        required=True,
    )

# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class CRMStageChangeConstrainDetail(models.Model):
    _name = "crm.stage_change_constrain_detail"
    _description = "CRM Lead State Change Constrain Detail"

    template_id = fields.Many2one(
        string="Stage Change Constrain Template",
        comodel_name="crm.stage_change_constrain_template",
        ondelete="cascade",
        required=True,
    )
    stage_id = fields.Many2one(
        string="Stage",
        comodel_name="crm.stage",
        ondelete="restrict",
        required=True,
    )
    status_check_item_ids = fields.Many2many(
        string="Status Check Item",
        comodel_name="crm.status_check_item",
        relation="rel_stage_change_constrain_status_check_item",
        column1="status_check_item_id",
        column2="stage_change_constrain_detail_id",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=1,
    )

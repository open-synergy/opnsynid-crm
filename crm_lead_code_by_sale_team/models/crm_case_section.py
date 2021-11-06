# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class CrmCaseSection(models.Model):
    _inherit = "crm.case.section"

    lead_sequence_id = fields.Many2one(
        string="Leads Sequence",
        comodel_name="ir.sequence",
        company_dependent=True,
    )

# -*- coding: utf-8 -*-
# Copyright 2020 PT. Simetri Sinergi Indonesia
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class CrmLead(models.Model):
    _inherit = "crm.lead"

    type_id = fields.Many2one(
        string="Type",
        comodel_name="sale.order.type",
    )

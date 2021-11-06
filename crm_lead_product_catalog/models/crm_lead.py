# -*- coding: utf-8 -*-
# Copyright 2020 PT. Simetri Sinergi Indonesia
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class CrmLead(models.Model):
    _name = "crm.lead"
    _inherit = "crm.lead"

    product_ids = fields.Many2many(
        string="Products",
        comodel_name="product.product",
        relation="rel_crm_lead_2_product_catalog",
        column1="lead_id",
        column2="product_id",
    )
    pricelist_id = fields.Many2one(
        string="Pricelist",
        comodel_name="product.pricelist",
    )

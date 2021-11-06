# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProcurementOrder(models.Model):
    _inherit = "procurement.order"

    lead_id = fields.Many2one(
        string="Lead/Opportunity",
        comodel_name="crm.lead",
    )

    @api.onchange("warehouse_id")
    def onchange_update_cust_promotion_route(self):
        if self.env.context.get("crm_promotion", False):
            wh = self.warehouse_id
            if wh.customer_promotion_route_id:
                self.route_ids = [wh.customer_promotion_route_id.id]

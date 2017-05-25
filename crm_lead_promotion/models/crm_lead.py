# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api, fields


class CrmLead(models.Model):
    _inherit = "crm.lead"

    @api.multi
    @api.depends(
        "partner_id")
    def _compute_cust_promotion_loc_id(self):
        global_loc = self.env["ir.property"].get(
            "property_stock_customer_promotion_id",
            "res.partner")
        for lead in self:
            if not lead.partner_id:
                lead.cust_promotion_loc_id = global_loc.id
            else:
                lead.cust_promotion_loc_id = \
                    lead.partner_id.property_stock_customer_promotion_id

    procurement_group_id = fields.Many2one(
        string="Procurement group",
        comodel_name="procurement.group",
    )
    procurement_ids = fields.One2many(
        string="Procurement",
        comodel_name="procurement.order",
        inverse_name="lead_id",
    )
    cust_promotion_loc_id = fields.Many2one(
        string="Cust. Promotion Loc",
        comodel_name="stock.location",
        store=False,
        compute="_compute_cust_promotion_loc_id",
    )

    @api.multi
    def view_customer_promotions(self):
        self.ensure_one()
        waction = self.env.ref(
            "stock.do_view_pickings")
        result = waction.read()[0]
        group_id = self.procurement_group_id.id
        result["domain"] = [('group_id', '=', group_id)]
        return result

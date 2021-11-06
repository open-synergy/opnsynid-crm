# -*- coding: utf-8 -*-
# Copyright 2020 PT. Simetri Sinergi Indonesia
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class CrmMakeSale(models.TransientModel):
    _inherit = "crm.make.sale"

    @api.multi
    def makeOrder(self):
        self.ensure_one()
        _super = super(CrmMakeSale, self)
        obj_case = self.env["crm.lead"]
        obj_sale = self.env["sale.order"]
        case = obj_case.browse([self.env.context.get("active_id", False)])[0]
        type_id = case.type_id and case.type_id.id or False
        result = _super.makeOrder()
        sale_id = result["res_id"]
        sale = obj_sale.browse([sale_id])[0]
        sale.write({"type_id": type_id})
        return result

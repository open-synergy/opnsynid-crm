# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class CRMStatusCheckTemplate(models.Model):
    _name = "crm.status_check_template"
    _description = "CRM Status Check Template"

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
        default=5,
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
        comodel_name="crm.status_check_template_detail",
        inverse_name="template_id",
    )

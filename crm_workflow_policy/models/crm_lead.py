# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, fields
from odoo.exceptions import Warning as UserError
from odoo.tools.translate import _


class CRMLead(models.Model):
    _name = "crm.lead"
    _inherit = [
        "crm.lead",
        "base.workflow_policy_object"
    ]

    @api.multi
    @api.depends(
        "team_id",
    )
    def _compute_policy(self):
        _super = super(CRMLead, self)
        _super._compute_policy()

    won_ok = fields.Boolean(
        string="Can Won",
        compute="_compute_policy",
        store=False,
    )
    lost_ok = fields.Boolean(
        string="Can Lost",
        compute="_compute_policy",
        store=False,
    )
    archieve_ok = fields.Boolean(
        string="Can Archieve",
        compute="_compute_policy",
        store=False,
    )
    restore_ok = fields.Boolean(
        string="Can Restore",
        compute="_compute_policy",
        store=False,
    )

    @api.multi
    @api.constrains(
        "probability",
    )
    def _check_allowed_won(self):
        for document in self:
            if document.probability == 100 and document.won_ok == False:
                raise UserError(_("User is not allowed to Mark Won"))
        return {}

    @api.multi
    @api.constrains(
        "probability",
        "active",
    )
    def _check_allowed_lost(self):
        for document in self:
            if (
                document.probability == 0 and
                document.lost_ok == False and
                document.active == False
            ):
                raise UserError(_("User is not allowed to Mark Lost"))
        return {}

    @api.multi
    @api.constrains(
        "active",
    )
    def _check_allowed_archive(self):
        for document in self:
            if (
                document.archieve_ok == False and
                document.active == False
            ):
                raise UserError(_("User is not allowed to Archive"))
        return {}

    @api.multi
    @api.constrains(
        "active",
    )
    def _check_allowed_restore(self):
        for document in self:
            if (
                document.restore_ok == False and
                document.active == True
            ):
                raise UserError(_("User is not allowed to Restore"))
        return {}

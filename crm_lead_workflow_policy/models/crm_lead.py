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

    @api.multi
    def _compute_is_current_user_team(self):
        for document in self:
            result = False
            if  (
                document.user_id == self.env.user or
                self.env.user.id in document.team_id.member_ids.ids
                ):
                result = True
            document.is_current_user_team = result

    current_user_id = fields.Many2one(
        string="Current User",
        comodel_name="res.users",
        compute="_compute_current_user_id",
        store=False,
    )
    is_current_user_team = fields.Boolean(
        string="Is Salesperson or Team",
        compute="_compute_is_current_user_team",
        store=False,
    )
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
    show_detail_ok = fields.Boolean(
        string="Can Show Detail",
        compute="_compute_policy",
        store=False,
    )

    @api.multi
    @api.constrains(
        "probability",
    )
    def _check_allowed_won(self):
        for document in self:
            if document.probability == 100 and not document.won_ok:
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
                not document.lost_ok
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
                not document.archieve_ok and
                not document.active
            ):
                raise UserError(_("User is not allowed to Archive"))
        return {}

    @api.multi
    @api.constrains(
        "active",
    )
    def _check_allowed_restore(self):
        for document in self:
            # To Prevent Constraints for A New Data
            if document.create_date == fields.Datetime.now():
                continue

            if (
                not document.restore_ok and
                document.active
            ):
                raise UserError(_("User is not allowed to Restore"))
        return {}

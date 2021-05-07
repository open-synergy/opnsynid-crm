# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class CRMFunnelType(models.Model):
    _name = "crm.funnel_type"
    _description = "CRM Funnel Type"

    name = fields.Char(
        string="Name",
        required=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    description = fields.Text(
        string="Description",
    )
    lead_ids = fields.One2many(
        string="Leads",
        comodel_name="crm.lead",
        inverse_name="funnel_type_id",
    )
    user_id = fields.Many2one(
        string="Manager",
        comodel_name="res.users",
        required=True,
    )
    member_ids = fields.Many2many(
        string="Members",
        comodel_name="res.users",
        relation="rel_funnel_type_member",
        column1="funnel_type_id",
        column2="user_id",
    )
    window_action_id = fields.Many2one(
        string="Window Action",
        comodel_name="ir.actions.act_window",
        readonly=True,
    )
    menu_id = fields.Many2one(
        string="Menu",
        comodel_name="ir.ui.menu",
        readonly=True,
    )

    @api.multi
    def _create_window_action(self):
        self.ensure_one()
        window_action = False

        if not self.window_action_id:
            pipeline_waction_id = \
                self.env.ref("crm.crm_lead_opportunities_tree_view")
            new_waction = pipeline_waction_id.copy()
            new_waction.name = self.name
            new_waction.domain = [("funnel_type_id", "=", self.id)]
            new_waction.context = {
                "default_funnel_type_id": self.id,
            }
            window_action = new_waction

        return window_action

    @api.multi
    def _create_menu(self):
        self.ensure_one()
        menu = False
        obj_ir_ui_menu = self.env["ir.ui.menu"]
        parent_menu_id = self.env.ref("crm.crm_menu_pipeline")

        if not self.menu_id:
            res = {
                "name": self.name,
                "sequence": 500,
                "parent_id": parent_menu_id.id,
                "action": "ir.actions.act_window,%s" % self.window_action_id.id
            }

            menu = obj_ir_ui_menu.create(res)

        return menu

    @api.multi
    def action_create_menu(self):
        self.ensure_one()
        window_action =\
            self._create_window_action()
        self.window_action_id = window_action and window_action.id or False

        menu = self._create_menu()
        self.menu_id = menu and menu.id or False

        return {
            "type": "ir.actions.client",
            "tag": "reload",
        }

    @api.multi
    def action_delete_menu(self):
        self.ensure_one()
        if self.window_action_id:
            self.window_action_id.unlink()
        if self.menu_id:
            self.menu_id.unlink()

        return {
            "type": "ir.actions.client",
            "tag": "reload",
        }

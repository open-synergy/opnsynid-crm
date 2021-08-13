# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from psycopg2.extensions import AsIs

from odoo import fields, models
from odoo.tools import drop_view_if_exists


class CRMLeadStageChangeHistorySummary(models.Model):
    _name = "crm.lead_stage_change_history_summary"
    _description = "CRM Lead Stage Change History Summary"
    _auto = False

    lead_id = fields.Many2one(
        string="# Lead",
        comodel_name="crm.lead",
    )
    latest_stage_to_id = fields.Many2one(
        string="Latest Stage To",
        comodel_name="crm.stage",
    )
    change_count = fields.Integer(
        string="Change Count",
        default=0,
    )
    latest_date_change = fields.Datetime(
        string="Latest Date Change",
    )
    latest_user_id = fields.Many2one(
        string="Latest User",
        comodel_name="res.users",
    )

    def _select(self):
        select_str = """
            SELECT
                row_number() OVER() AS id,
                a.lead_id AS lead_id,
                a.user_id AS latest_user_id,
                a.stage_to_id AS latest_stage_to_id,
                a.date_change AS latest_date_change,
                b.change_count AS change_count
        """
        return select_str

    def _from(self):
        from_str = """
            FROM crm_lead_stage_change_history AS a
        """
        return from_str

    def _join(self):
        join_str = """
            JOIN (
                SELECT
                    b1.lead_id,
                    b1.user_id,
                    b1.stage_to_id,
                    COUNT(b1.user_id) AS change_count
                FROM
                   crm_lead_stage_change_history AS b1
               GROUP BY
                   b1.lead_id, b1.user_id, b1.stage_to_id
            ) AS b ON a.lead_id=b.lead_id
                   AND a.user_id=b.user_id
                   AND a.stage_to_id=b.stage_to_id
            JOIN (
                SELECT
                    c1.lead_id,
                    c1.user_id,
                    c1.stage_to_id,
                    MAX(c1.date_change) AS max_date_change
                FROM
                   crm_lead_stage_change_history AS c1
                GROUP BY
                   c1.lead_id, c1.user_id, c1.stage_to_id
            ) AS c ON a.lead_id=c.lead_id
                   AND a.user_id=c.user_id
                   AND a.stage_to_id=c.stage_to_id
        """
        return join_str

    def _order_by(self):
        order_by_str = """
            ORDER BY a.user_id, a.date_change DESC
        """
        return order_by_str

    def _where(self):
        _where = """
            WHERE a.date_change = c.max_date_change
        """
        return _where

    def init(self):
        drop_view_if_exists(self.env.cr, self._table)
        view_query = """{}
            {}
            {}
            {}
            {}""".format(
            self._select(),
            self._from(),
            self._join(),
            self._where(),
            self._order_by(),
        )
        self.env.cr.execute(
            "CREATE OR REPLACE VIEW %s AS %s", (AsIs(self._table), AsIs(view_query))
        )

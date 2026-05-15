import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-open-synergy-opnsynid-crm",
    description="Meta package for open-synergy-opnsynid-crm Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-crm_disable_m2o_option',
        'odoo11-addon-crm_lead_assign_salesperson',
        'odoo11-addon-crm_lead_auto_archieve',
        'odoo11-addon-crm_lead_custom_information',
        'odoo11-addon-crm_lead_day_on_stage',
        'odoo11-addon-crm_lead_funnel_type',
        'odoo11-addon-crm_lead_last_update_from_openchatter',
        'odoo11-addon-crm_lead_manual_date_won',
        'odoo11-addon-crm_lead_mark_as_won',
        'odoo11-addon-crm_lead_related_attachment',
        'odoo11-addon-crm_lead_stage_change_history',
        'odoo11-addon-crm_lead_state_change_constrain',
        'odoo11-addon-crm_lead_status_check',
        'odoo11-addon-crm_lead_workflow_policy',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)

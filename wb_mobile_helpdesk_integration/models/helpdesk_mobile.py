import logging
import json
import requests
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class WBMobileRequestRegistration(models.Model):
    _name = "wb.mobile.request.registration"
    _description = "Mobile Helpdesk Request Registratiton List"

    name = fields.Selection([('fse','FSE')])
    request = fields.Text("Request")
    response = fields.Text("Response")
    state = fields.Selection([('draft', 'Draft'),
                              ('invalid', 'Invalid'),
                              ('done','Done')], default='draft')
    active = fields.Boolean("Active", default=True)
    process_message = fields.Char("Proceed Message")

    def getCustomerList(self):
        return [{'name':prd.display_name, 'id':prd.id, 'customer_id': prd.x_studio_customer_id} for prd in self.env['res.partner'].sudo().search([('id','>',5)])]

    def getCompanyList(self):
        return [{'name':prd.name, 'id':prd.id, } for prd in self.env['res.company'].sudo().search([])]

    def getHelpdeskTeamList(self):
        return [{'name': prd.name, 'id': prd.id, 'company_id': prd.company_id.id} for prd in self.env['helpdesk.team'].sudo().search([])]

    def getHelpdeskList(self):
        return [{'name': prd.name,
                 'id': prd.id,
                 'helpdesk_number':prd.x_studio_helpdesk_id or '',
                 'helpdesk_team_id': prd.team_id.id,
                 'helpdesk_team_name': prd.team_id.name,
                 'sale_id': prd.x_studio_many2one_field_fD8Y4.name,
                 'assigned_user_id': prd.user_id.id,
                 'assigned_user_name': prd.user_id.name,
                 'ticket_type_id': prd.ticket_type_id.id,
                 'ticket_type_name': prd.ticket_type_id.name,
                 'created_by': prd.create_uid.name,
                 'created_date': prd.create_date,
                 'customer_id': prd.partner_id.id,
                 'customer_name': prd.partner_id.name,
                 'area_manager_id': prd.x_studio_many2one_field_F3tVh.id,
                 'area_manager_name': prd.x_studio_many2one_field_F3tVh.name,
                 'fse_id': prd.x_studio_fse.id,
                 'fse_name': prd.x_studio_fse.name,
                 'company_id': prd.company_id.id,
                 'company_name': prd.company_id.name,
                 'stage_list':[{'stage_name': sts.name,
                                 'stage_id': sts.id,
                                 'is_last_status': sts.is_close}
                                for sts in self.env['helpdesk.stage'].search(['team_ids', 'in', prd.team_id.ids], order='sequence')],
                 'stage_id': prd.state_id.id,
                 'stage_name': prd.state_id.name,
                 }
                for prd in self.env['helpdesk.ticket'].search([])]

    def getProductList(self):
        return [{'id':prd.id, 'name':prd.name} for prd in
                self.env['product.product'].search([('sale_ok', '=', True)])]

    def getTeamList(self):
        return [{'id': prd.id, 'name': prd.name} for prd in
                self.env.ref('base.group_user').sudo().users]

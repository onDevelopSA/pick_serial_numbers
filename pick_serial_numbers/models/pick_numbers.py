# © 2021 onDevelop.SA
# ondevelop.sa@gmail.com
# Autor: Idelis Gé Ramírez

from odoo import fields, models, tools, api
from odoo.exceptions import UserError, ValidationError


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'
    _description = 'Inherit for update the Serial Number or the given pick.'

    product_ref = fields.Char()
    pick_number = fields.Char()

    @api.model
    def create(self, vals):
        '''Call the pick update with the given serial number for the specific
        product.

        '''
        lot_serial = False
        if not ('product_ref' in vals and 'pick_number' in vals):
            lot_serial = super(StockProductionLot, self).create(vals)
        elif 'product_ref' in vals and 'pick_number' in vals:
            product = self.env['product.product'].search(
                [('default_code', '=', vals['product_ref'])], limit=1)
            if not product:
                msg_err = "No exist a product with the given reference {ref}."+\
                          "Please enter the product Reference to use."
                raise UserError(_(msg_err.format(ref=vals['product_ref'])))
            vals['product_id'] = product.id
            lot_serial = super(StockProductionLot, self).create(vals)
            pick = self.env['stock.picking'].search([
                ('name', '=', vals['pick_number'])])
            if not pick:
                raise UserError("The pick given {p} doesn't exist.".format(
                    p=vals['pick_number']))
            pick.upd_move_lines_serial_numbers(product, vals['pick_number'],
                                               lot_serial)
        return lot_serial

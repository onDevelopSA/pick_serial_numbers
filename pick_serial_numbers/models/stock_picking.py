# © 2021 onDevelop.SA
# ondevelop.sa@gmail.com
# Autor: Idelis Gé Ramírez

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    _description = 'Add the method for update the serial numbers.'

    def validate_serial_number(self, product, lot_serial_id):
        '''Validate if the given serial number was previously used in any
        other stock move.

        '''
        if any(self.env['stock.move.line'].search([
                ('lot_id', '=', lot_serial_id), ('product_id', '=', product.id)])):
            msg_err = "The serial number '{n}' already was used, please verify."
            raise UserError(_(msg_err.format(n=lot_serial_id.name)))

    def upd_move_lines_serial_numbers(self, product, pick_number, lot_serial):
        '''Update pick moves lines with the given Lot Serial Number'''
        self.validate_serial_number(product, lot_serial.id)
        move_funct = lambda m: m.product_id.default_code == product.default_code
        moves = self.move_lines.filtered(move_funct)
        if len(moves) == 0:
            msg_err = "The product with reference {r} is not in the order {o}."
            assert False, msg_err.format(r=product.default_code, o=pick_number)
        lines = moves.move_line_ids.filtered(lambda l: l.lot_name == False)
        if lines:
            lines[0].lot_name = lot_serial.name
            lines[0].lot_id = lot_serial.id

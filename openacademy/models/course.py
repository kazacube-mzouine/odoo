# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class openacademy(models.Model):
    _name = 'course'
    _sql_constraints = [
        ('unique_name', 'unique (name)',
         "Title should be unique!")]
    # _sql_constraints = [
    #     ('check_name_different_description', 'check (name != desc)',
    #      "Name and Description must be different")]    does not work because they're not the same type


    name = fields.Char(string="Title", required=True)
    desc = fields.Text(string="Description")
    supervisor_id = fields.Many2one('res.users', string='Superviser user')
    session_ids = fields.One2many('session', 'course_id', string='Sessions')


class Session(models.Model):
    _name = 'session'

    name = fields.Char(string="Name",required=True)
    start_date = fields.Date('Start Date')
    duration = fields.Float('Duration')
    number_of_seats = fields.Float('Number of seats')
    seats_occupied = fields.Float('Seats occupied')
    instructor_id = fields.Many2one('res.partner', string='Instructor')
    course_id = fields.Many2one('course', string='Course', required=True)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')
    occupation_ratio = fields.Float(string='Occupation ratio', compute='set_occupation_ratio')

    @api.one
    @api.depends('number_of_seats', 'seats_occupied')
    def set_occupation_ratio(self):
        if self.number_of_seats > 0:
            self.occupation_ratio = (self.seats_occupied / self.number_of_seats)*100

    @api.one
    @api.onchange('number_of_seats')
    def alert_number_of_seats(self):
        # _logger.info("xxxxxx")
        # _logger.info("xxxxxx",self.number_of_seats)
        print("*****************************")

        if self.number_of_seats < 0:
            raise ValidationError("You can't enter a negative number of seats")

    @api.one
    @api.constrains('instructor_id', 'attendee_ids')
    def check_instructor(self):
        if self.instructor_id in self.attendee_ids:
            raise ValidationError("Instructor shouldn't be an attendee")


    # @api.one
    # @api.onchange('seats_occupied')
    # def alert_seats_occupied(self):
    #     if self.number_of_seats and self.seats_occupied > self.number_of_seats:
    #         raise ValidationError("You can enter a higher number than number of seats")


class ResParner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Instructor')
    session_ids = fields.Many2many('session', string='Sessions')
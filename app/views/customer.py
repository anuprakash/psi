# encoding=utf-8
from datetime import datetime

from app.views import ModelViewWithAccess
from flask.ext.babelex import lazy_gettext
from app.views.formatter import default_date_formatter
from app.models.customer import Customer


class CustomerAdmin(ModelViewWithAccess):
    column_list = ('id', 'name', 'mobile_phone', 'email', 'address', 'birthday',
                   'join_date', 'member_age', 'join_channel', 'level', 'total_spent')

    column_labels = {
        'id': lazy_gettext('id'),
        'name': lazy_gettext('Name'),
        'mobile_phone': lazy_gettext('Mobile Phone'),
        'email': lazy_gettext('Email'),
        'birthday': lazy_gettext('Birthday'),
        'address': lazy_gettext('Address'),
        'join_date': lazy_gettext('Join Date'),
        'member_age': lazy_gettext('Member Year'),
        'join_channel': lazy_gettext('Join Channel'),
        'level': lazy_gettext('Customer Level'),
        'total_spent': lazy_gettext('Total Spent'),
        'first_name': lazy_gettext('First Name'),
        'last_name': lazy_gettext('Last Name'),
        'points': lazy_gettext('Points'),
        'sales_orders': lazy_gettext('Sales Order')
    }

    # column_filters = ['member_age', 'total_spent']

    edit_modal = True
    create_modal = True

    form_excluded_columns = ('sales_orders',)

    column_searchable_list = ['first_name', 'last_name', 'mobile_phone', 'address', 'email']

    column_formatters = {
        'join_date': default_date_formatter,
    }

    form_create_rules = form_edit_rules = ['last_name', 'first_name', 'mobile_phone',
                                           'email', 'address', 'birthday', 'join_channel',
                                           'join_date', 'level', 'points']

    column_details_list = ['last_name', 'first_name', 'mobile_phone',
                           'email', 'address', 'birthday', 'join_channel',
                           'join_date', 'level', 'points', 'sales_orders']

    form_args = dict(
        join_channel=dict(query_factory=Customer.join_channel_filter),
        level=dict(query_factory=Customer.level_filter),
        join_date=dict(default=datetime.now()),
    )

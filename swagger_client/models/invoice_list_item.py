# coding: utf-8

"""
    Bind ERP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InvoiceListItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'serie': 'str',
        'date': 'datetime',
        'number': 'int',
        'uuid': 'str',
        'expiration_date': 'datetime',
        'client_id': 'str',
        'client_name': 'str',
        'rfc': 'str',
        'cost': 'float',
        'subtotal': 'float',
        'discount': 'float',
        'vat': 'float',
        'ieps': 'float',
        'isr_ret': 'float',
        'vat_ret': 'float',
        'total': 'float',
        'payments': 'float',
        'credit_notes': 'float',
        'currency_id': 'str',
        'location_id': 'str',
        'warehouse_id': 'str',
        'price_list_id': 'str',
        'cfdiid': 'str',
        'cfdi_use': 'int',
        'exchange_rate': 'float',
        'vat_ret_rate': 'float',
        'comments': 'str',
        'vat_rate': 'float',
        'purchase_order': 'str',
        'is_fiscal_invoice': 'bool',
        'show_ieps': 'bool',
        'status': 'int'
    }

    attribute_map = {
        'serie': 'Serie',
        'date': 'Date',
        'number': 'Number',
        'uuid': 'UUID',
        'expiration_date': 'ExpirationDate',
        'client_id': 'ClientID',
        'client_name': 'ClientName',
        'rfc': 'RFC',
        'cost': 'Cost',
        'subtotal': 'Subtotal',
        'discount': 'Discount',
        'vat': 'VAT',
        'ieps': 'IEPS',
        'isr_ret': 'ISRRet',
        'vat_ret': 'VATRet',
        'total': 'Total',
        'payments': 'Payments',
        'credit_notes': 'CreditNotes',
        'currency_id': 'CurrencyID',
        'location_id': 'LocationID',
        'warehouse_id': 'WarehouseID',
        'price_list_id': 'PriceListID',
        'cfdiid': 'CFDIID',
        'cfdi_use': 'CFDIUse',
        'exchange_rate': 'ExchangeRate',
        'vat_ret_rate': 'VATRetRate',
        'comments': 'Comments',
        'vat_rate': 'VATRate',
        'purchase_order': 'PurchaseOrder',
        'is_fiscal_invoice': 'IsFiscalInvoice',
        'show_ieps': 'ShowIEPS',
        'status': 'Status'
    }

    def __init__(self, serie=None, date=None, number=None, uuid=None, expiration_date=None, client_id=None, client_name=None, rfc=None, cost=None, subtotal=None, discount=None, vat=None, ieps=None, isr_ret=None, vat_ret=None, total=None, payments=None, credit_notes=None, currency_id=None, location_id=None, warehouse_id=None, price_list_id=None, cfdiid=None, cfdi_use=None, exchange_rate=None, vat_ret_rate=None, comments=None, vat_rate=None, purchase_order=None, is_fiscal_invoice=None, show_ieps=None, status=None):  # noqa: E501
        """InvoiceListItem - a model defined in Swagger"""  # noqa: E501

        self._serie = None
        self._date = None
        self._number = None
        self._uuid = None
        self._expiration_date = None
        self._client_id = None
        self._client_name = None
        self._rfc = None
        self._cost = None
        self._subtotal = None
        self._discount = None
        self._vat = None
        self._ieps = None
        self._isr_ret = None
        self._vat_ret = None
        self._total = None
        self._payments = None
        self._credit_notes = None
        self._currency_id = None
        self._location_id = None
        self._warehouse_id = None
        self._price_list_id = None
        self._cfdiid = None
        self._cfdi_use = None
        self._exchange_rate = None
        self._vat_ret_rate = None
        self._comments = None
        self._vat_rate = None
        self._purchase_order = None
        self._is_fiscal_invoice = None
        self._show_ieps = None
        self._status = None
        self.discriminator = None

        if serie is not None:
            self.serie = serie
        if date is not None:
            self.date = date
        if number is not None:
            self.number = number
        if uuid is not None:
            self.uuid = uuid
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if client_id is not None:
            self.client_id = client_id
        if client_name is not None:
            self.client_name = client_name
        if rfc is not None:
            self.rfc = rfc
        if cost is not None:
            self.cost = cost
        if subtotal is not None:
            self.subtotal = subtotal
        if discount is not None:
            self.discount = discount
        if vat is not None:
            self.vat = vat
        if ieps is not None:
            self.ieps = ieps
        if isr_ret is not None:
            self.isr_ret = isr_ret
        if vat_ret is not None:
            self.vat_ret = vat_ret
        if total is not None:
            self.total = total
        if payments is not None:
            self.payments = payments
        if credit_notes is not None:
            self.credit_notes = credit_notes
        if currency_id is not None:
            self.currency_id = currency_id
        if location_id is not None:
            self.location_id = location_id
        if warehouse_id is not None:
            self.warehouse_id = warehouse_id
        if price_list_id is not None:
            self.price_list_id = price_list_id
        if cfdiid is not None:
            self.cfdiid = cfdiid
        if cfdi_use is not None:
            self.cfdi_use = cfdi_use
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if vat_ret_rate is not None:
            self.vat_ret_rate = vat_ret_rate
        if comments is not None:
            self.comments = comments
        if vat_rate is not None:
            self.vat_rate = vat_rate
        if purchase_order is not None:
            self.purchase_order = purchase_order
        if is_fiscal_invoice is not None:
            self.is_fiscal_invoice = is_fiscal_invoice
        if show_ieps is not None:
            self.show_ieps = show_ieps
        if status is not None:
            self.status = status

    @property
    def serie(self):
        """Gets the serie of this InvoiceListItem.  # noqa: E501


        :return: The serie of this InvoiceListItem.  # noqa: E501
        :rtype: str
        """
        return self._serie

    @serie.setter
    def serie(self, serie):
        """Sets the serie of this InvoiceListItem.


        :param serie: The serie of this InvoiceListItem.  # noqa: E501
        :type: str
        """

        self._serie = serie

    @property
    def date(self):
        """Gets the date of this InvoiceListItem.  # noqa: E501


        :return: The date of this InvoiceListItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this InvoiceListItem.


        :param date: The date of this InvoiceListItem.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def number(self):
        """Gets the number of this InvoiceListItem.  # noqa: E501


        :return: The number of this InvoiceListItem.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InvoiceListItem.


        :param number: The number of this InvoiceListItem.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def uuid(self):
        """Gets the uuid of this InvoiceListItem.  # noqa: E501


        :return: The uuid of this InvoiceListItem.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InvoiceListItem.


        :param uuid: The uuid of this InvoiceListItem.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def expiration_date(self):
        """Gets the expiration_date of this InvoiceListItem.  # noqa: E501


        :return: The expiration_date of this InvoiceListItem.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this InvoiceListItem.


        :param expiration_date: The expiration_date of this InvoiceListItem.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def client_id(self):
        """Gets the client_id of this InvoiceListItem.  # noqa: E501


        :return: The client_id of this InvoiceListItem.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this InvoiceListItem.


        :param client_id: The client_id of this InvoiceListItem.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this InvoiceListItem.  # noqa: E501


        :return: The client_name of this InvoiceListItem.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this InvoiceListItem.


        :param client_name: The client_name of this InvoiceListItem.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def rfc(self):
        """Gets the rfc of this InvoiceListItem.  # noqa: E501


        :return: The rfc of this InvoiceListItem.  # noqa: E501
        :rtype: str
        """
        return self._rfc

    @rfc.setter
    def rfc(self, rfc):
        """Sets the rfc of this InvoiceListItem.


        :param rfc: The rfc of this InvoiceListItem.  # noqa: E501
        :type: str
        """

        self._rfc = rfc

    @property
    def cost(self):
        """Gets the cost of this InvoiceListItem.  # noqa: E501


        :return: The cost of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this InvoiceListItem.


        :param cost: The cost of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def subtotal(self):
        """Gets the subtotal of this InvoiceListItem.  # noqa: E501


        :return: The subtotal of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this InvoiceListItem.


        :param subtotal: The subtotal of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._subtotal = subtotal

    @property
    def discount(self):
        """Gets the discount of this InvoiceListItem.  # noqa: E501


        :return: The discount of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this InvoiceListItem.


        :param discount: The discount of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._discount = discount

    @property
    def vat(self):
        """Gets the vat of this InvoiceListItem.  # noqa: E501


        :return: The vat of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._vat

    @vat.setter
    def vat(self, vat):
        """Sets the vat of this InvoiceListItem.


        :param vat: The vat of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._vat = vat

    @property
    def ieps(self):
        """Gets the ieps of this InvoiceListItem.  # noqa: E501


        :return: The ieps of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._ieps

    @ieps.setter
    def ieps(self, ieps):
        """Sets the ieps of this InvoiceListItem.


        :param ieps: The ieps of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._ieps = ieps

    @property
    def isr_ret(self):
        """Gets the isr_ret of this InvoiceListItem.  # noqa: E501


        :return: The isr_ret of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._isr_ret

    @isr_ret.setter
    def isr_ret(self, isr_ret):
        """Sets the isr_ret of this InvoiceListItem.


        :param isr_ret: The isr_ret of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._isr_ret = isr_ret

    @property
    def vat_ret(self):
        """Gets the vat_ret of this InvoiceListItem.  # noqa: E501


        :return: The vat_ret of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._vat_ret

    @vat_ret.setter
    def vat_ret(self, vat_ret):
        """Sets the vat_ret of this InvoiceListItem.


        :param vat_ret: The vat_ret of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._vat_ret = vat_ret

    @property
    def total(self):
        """Gets the total of this InvoiceListItem.  # noqa: E501


        :return: The total of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InvoiceListItem.


        :param total: The total of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def payments(self):
        """Gets the payments of this InvoiceListItem.  # noqa: E501


        :return: The payments of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this InvoiceListItem.


        :param payments: The payments of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._payments = payments

    @property
    def credit_notes(self):
        """Gets the credit_notes of this InvoiceListItem.  # noqa: E501


        :return: The credit_notes of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._credit_notes

    @credit_notes.setter
    def credit_notes(self, credit_notes):
        """Sets the credit_notes of this InvoiceListItem.


        :param credit_notes: The credit_notes of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._credit_notes = credit_notes

    @property
    def currency_id(self):
        """Gets the currency_id of this InvoiceListItem.  # noqa: E501


        :return: The currency_id of this InvoiceListItem.  # noqa: E501
        :rtype: str
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this InvoiceListItem.


        :param currency_id: The currency_id of this InvoiceListItem.  # noqa: E501
        :type: str
        """

        self._currency_id = currency_id

    @property
    def location_id(self):
        """Gets the location_id of this InvoiceListItem.  # noqa: E501


        :return: The location_id of this InvoiceListItem.  # noqa: E501
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this InvoiceListItem.


        :param location_id: The location_id of this InvoiceListItem.  # noqa: E501
        :type: str
        """

        self._location_id = location_id

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this InvoiceListItem.  # noqa: E501


        :return: The warehouse_id of this InvoiceListItem.  # noqa: E501
        :rtype: str
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this InvoiceListItem.


        :param warehouse_id: The warehouse_id of this InvoiceListItem.  # noqa: E501
        :type: str
        """

        self._warehouse_id = warehouse_id

    @property
    def price_list_id(self):
        """Gets the price_list_id of this InvoiceListItem.  # noqa: E501


        :return: The price_list_id of this InvoiceListItem.  # noqa: E501
        :rtype: str
        """
        return self._price_list_id

    @price_list_id.setter
    def price_list_id(self, price_list_id):
        """Sets the price_list_id of this InvoiceListItem.


        :param price_list_id: The price_list_id of this InvoiceListItem.  # noqa: E501
        :type: str
        """

        self._price_list_id = price_list_id

    @property
    def cfdiid(self):
        """Gets the cfdiid of this InvoiceListItem.  # noqa: E501


        :return: The cfdiid of this InvoiceListItem.  # noqa: E501
        :rtype: str
        """
        return self._cfdiid

    @cfdiid.setter
    def cfdiid(self, cfdiid):
        """Sets the cfdiid of this InvoiceListItem.


        :param cfdiid: The cfdiid of this InvoiceListItem.  # noqa: E501
        :type: str
        """

        self._cfdiid = cfdiid

    @property
    def cfdi_use(self):
        """Gets the cfdi_use of this InvoiceListItem.  # noqa: E501


        :return: The cfdi_use of this InvoiceListItem.  # noqa: E501
        :rtype: int
        """
        return self._cfdi_use

    @cfdi_use.setter
    def cfdi_use(self, cfdi_use):
        """Sets the cfdi_use of this InvoiceListItem.


        :param cfdi_use: The cfdi_use of this InvoiceListItem.  # noqa: E501
        :type: int
        """

        self._cfdi_use = cfdi_use

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this InvoiceListItem.  # noqa: E501


        :return: The exchange_rate of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this InvoiceListItem.


        :param exchange_rate: The exchange_rate of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def vat_ret_rate(self):
        """Gets the vat_ret_rate of this InvoiceListItem.  # noqa: E501


        :return: The vat_ret_rate of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._vat_ret_rate

    @vat_ret_rate.setter
    def vat_ret_rate(self, vat_ret_rate):
        """Sets the vat_ret_rate of this InvoiceListItem.


        :param vat_ret_rate: The vat_ret_rate of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._vat_ret_rate = vat_ret_rate

    @property
    def comments(self):
        """Gets the comments of this InvoiceListItem.  # noqa: E501


        :return: The comments of this InvoiceListItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this InvoiceListItem.


        :param comments: The comments of this InvoiceListItem.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def vat_rate(self):
        """Gets the vat_rate of this InvoiceListItem.  # noqa: E501


        :return: The vat_rate of this InvoiceListItem.  # noqa: E501
        :rtype: float
        """
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, vat_rate):
        """Sets the vat_rate of this InvoiceListItem.


        :param vat_rate: The vat_rate of this InvoiceListItem.  # noqa: E501
        :type: float
        """

        self._vat_rate = vat_rate

    @property
    def purchase_order(self):
        """Gets the purchase_order of this InvoiceListItem.  # noqa: E501


        :return: The purchase_order of this InvoiceListItem.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """Sets the purchase_order of this InvoiceListItem.


        :param purchase_order: The purchase_order of this InvoiceListItem.  # noqa: E501
        :type: str
        """

        self._purchase_order = purchase_order

    @property
    def is_fiscal_invoice(self):
        """Gets the is_fiscal_invoice of this InvoiceListItem.  # noqa: E501


        :return: The is_fiscal_invoice of this InvoiceListItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_fiscal_invoice

    @is_fiscal_invoice.setter
    def is_fiscal_invoice(self, is_fiscal_invoice):
        """Sets the is_fiscal_invoice of this InvoiceListItem.


        :param is_fiscal_invoice: The is_fiscal_invoice of this InvoiceListItem.  # noqa: E501
        :type: bool
        """

        self._is_fiscal_invoice = is_fiscal_invoice

    @property
    def show_ieps(self):
        """Gets the show_ieps of this InvoiceListItem.  # noqa: E501


        :return: The show_ieps of this InvoiceListItem.  # noqa: E501
        :rtype: bool
        """
        return self._show_ieps

    @show_ieps.setter
    def show_ieps(self, show_ieps):
        """Sets the show_ieps of this InvoiceListItem.


        :param show_ieps: The show_ieps of this InvoiceListItem.  # noqa: E501
        :type: bool
        """

        self._show_ieps = show_ieps

    @property
    def status(self):
        """Gets the status of this InvoiceListItem.  # noqa: E501


        :return: The status of this InvoiceListItem.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InvoiceListItem.


        :param status: The status of this InvoiceListItem.  # noqa: E501
        :type: int
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InvoiceListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
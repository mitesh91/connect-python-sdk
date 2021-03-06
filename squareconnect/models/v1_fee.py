# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class V1Fee(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, rate=None, calculation_phase=None, adjustment_type=None, applies_to_custom_amounts=None, enabled=None, inclusion_type=None, type=None):
        """
        V1Fee - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'rate': 'str',
            'calculation_phase': 'str',
            'adjustment_type': 'str',
            'applies_to_custom_amounts': 'bool',
            'enabled': 'bool',
            'inclusion_type': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'rate': 'rate',
            'calculation_phase': 'calculation_phase',
            'adjustment_type': 'adjustment_type',
            'applies_to_custom_amounts': 'applies_to_custom_amounts',
            'enabled': 'enabled',
            'inclusion_type': 'inclusion_type',
            'type': 'type'
        }

        self._id = id
        self._name = name
        self._rate = rate
        self._calculation_phase = calculation_phase
        self._adjustment_type = adjustment_type
        self._applies_to_custom_amounts = applies_to_custom_amounts
        self._enabled = enabled
        self._inclusion_type = inclusion_type
        self._type = type

    @property
    def id(self):
        """
        Gets the id of this V1Fee.
        The fee's unique ID.

        :return: The id of this V1Fee.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this V1Fee.
        The fee's unique ID.

        :param id: The id of this V1Fee.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this V1Fee.
        The fee's name.

        :return: The name of this V1Fee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Fee.
        The fee's name.

        :param name: The name of this V1Fee.
        :type: str
        """

        self._name = name

    @property
    def rate(self):
        """
        Gets the rate of this V1Fee.
        The rate of the fee, as a string representation of a decimal number. A value of 0.07 corresponds to a rate of 7%.

        :return: The rate of this V1Fee.
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this V1Fee.
        The rate of the fee, as a string representation of a decimal number. A value of 0.07 corresponds to a rate of 7%.

        :param rate: The rate of this V1Fee.
        :type: str
        """

        self._rate = rate

    @property
    def calculation_phase(self):
        """
        Gets the calculation_phase of this V1Fee.
        Forthcoming

        :return: The calculation_phase of this V1Fee.
        :rtype: str
        """
        return self._calculation_phase

    @calculation_phase.setter
    def calculation_phase(self, calculation_phase):
        """
        Sets the calculation_phase of this V1Fee.
        Forthcoming

        :param calculation_phase: The calculation_phase of this V1Fee.
        :type: str
        """

        self._calculation_phase = calculation_phase

    @property
    def adjustment_type(self):
        """
        Gets the adjustment_type of this V1Fee.
        The type of adjustment the fee applies to a payment. Currently, this value is TAX for all fees.

        :return: The adjustment_type of this V1Fee.
        :rtype: str
        """
        return self._adjustment_type

    @adjustment_type.setter
    def adjustment_type(self, adjustment_type):
        """
        Sets the adjustment_type of this V1Fee.
        The type of adjustment the fee applies to a payment. Currently, this value is TAX for all fees.

        :param adjustment_type: The adjustment_type of this V1Fee.
        :type: str
        """

        self._adjustment_type = adjustment_type

    @property
    def applies_to_custom_amounts(self):
        """
        Gets the applies_to_custom_amounts of this V1Fee.
        If true, the fee applies to custom amounts entered into Square Register that are not associated with a particular item.

        :return: The applies_to_custom_amounts of this V1Fee.
        :rtype: bool
        """
        return self._applies_to_custom_amounts

    @applies_to_custom_amounts.setter
    def applies_to_custom_amounts(self, applies_to_custom_amounts):
        """
        Sets the applies_to_custom_amounts of this V1Fee.
        If true, the fee applies to custom amounts entered into Square Register that are not associated with a particular item.

        :param applies_to_custom_amounts: The applies_to_custom_amounts of this V1Fee.
        :type: bool
        """

        self._applies_to_custom_amounts = applies_to_custom_amounts

    @property
    def enabled(self):
        """
        Gets the enabled of this V1Fee.
        If true, the fee is applied to all appropriate items. If false, the fee is not applied at all.

        :return: The enabled of this V1Fee.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this V1Fee.
        If true, the fee is applied to all appropriate items. If false, the fee is not applied at all.

        :param enabled: The enabled of this V1Fee.
        :type: bool
        """

        self._enabled = enabled

    @property
    def inclusion_type(self):
        """
        Gets the inclusion_type of this V1Fee.
        Whether the fee is ADDITIVE or INCLUSIVE.

        :return: The inclusion_type of this V1Fee.
        :rtype: str
        """
        return self._inclusion_type

    @inclusion_type.setter
    def inclusion_type(self, inclusion_type):
        """
        Sets the inclusion_type of this V1Fee.
        Whether the fee is ADDITIVE or INCLUSIVE.

        :param inclusion_type: The inclusion_type of this V1Fee.
        :type: str
        """

        self._inclusion_type = inclusion_type

    @property
    def type(self):
        """
        Gets the type of this V1Fee.
        In countries with multiple classifications for sales taxes, indicates which classification the fee falls under. Currently relevant only to Canadian merchants.

        :return: The type of this V1Fee.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1Fee.
        In countries with multiple classifications for sales taxes, indicates which classification the fee falls under. Currently relevant only to Canadian merchants.

        :param type: The type of this V1Fee.
        :type: str
        """

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

from ValidationFunctions import ValidationFunctions

ob1 = ValidationFunctions()


class Validation(object):
    def f(self,AttributeValue,Attribute_type):

        if Attribute_type =='IPv4':
            return ob1.validIPAddress(AttributeValue,'IPv4')
        elif Attribute_type =='POSITIVE_NUMBER':
            return ob1.PositiveNumber(AttributeValue)
        elif Attribute_type == 'HOSTNAME':
            return ob1.is_valid_hostname(AttributeValue)



import re


class ValidationFunctions(object):
    def validIPAddress(self, IP, IPType):
        """
      :type IP: str
      :rtype: str
      """

        def isIPv4(s):
            try:
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False

        def isIPv6(s):
            if len(s) > 4:
                return False
            try:
                return int(s, 16) >= 0 and s[0] != '-'
            except:
                return False

        if IPType == 'IPv4' and IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
            return True
        if IPType == 'IPv6' and IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
            return True
        return False

    def PositiveNumber(self, AttributeValue):
        try:
            int(AttributeValue)
            return True
        except ValueError:
            return False

    def is_valid_hostname(self,hostname):
        if hostname[-1] == ".":
            # strip exactly one dot from the right, if present
            hostname = hostname[:-1]
        if len(hostname) > 253:
            return False

        labels = hostname.split(".")

        # the TLD must be not all-numeric
        if re.match(r"[0-9]+$", labels[-1]):
            return False

        allowed = re.compile(r"(?!-)[a-z0-9-]{1,63}(?<!-)$", re.IGNORECASE)
        return all(allowed.match(label) for label in labels)

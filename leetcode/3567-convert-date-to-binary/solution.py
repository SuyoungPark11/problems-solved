class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        year, month, day = date.split('-')
        return '-'.join([bin(int(comp))[2:] for comp in [year, month, day]])

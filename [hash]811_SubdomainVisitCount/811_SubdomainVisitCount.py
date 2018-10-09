"""
问题：
给定一组网站及其访问次数的列表，返回网站对应的所有子域名的访问次数
解法：
字符串处理加map
"""
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domins = {}
        for domin in cpdomains:
            cnt, dominNames = domin.split()
            dominName = dominNames.split('.')
            name = ""
            for j in dominName[::-1]:
                name = j + "." + name if len(name) > 0 else j
                domins[name] = domins.get(name, 0) + int(cnt)
        return ["{} {}".format(ct, dom) for dom, ct in domins.items()]
        """
        ret = []
        for k in domins.keys():
            ret.append(str(domins[k]) + " " + k)
        return ret
        """
solution = Solution()
input = ["9001 discuss.leetcode.com"]
print (solution.subdomainVisits(input))

input = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print (solution.subdomainVisits(input))

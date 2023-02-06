class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.upper()
        s = s.replace("-", "")
        output = ""

        output = s[:len(s) % k]

        for i in range(len(s) // k):
            if len(output) > 0:
                output += "-"
            output += s[len(s) % k + (i * k): len(s) % k + (i * k) + k]

        return output
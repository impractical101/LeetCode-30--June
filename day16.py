#Submitted by thr3sh0ld
#Logic : handle all basic differences b/w IPv4 and IPv6. Readable code.
class Solution:
    def IPv4(self,IP):
            collec = IP.split('.')
            if len(collec) != 4:  
                return False
            for i in collec:
                try:
                    if int(i) > 255: return False
                except ValueError:
                    return False
                if i[0] == '0' and len(i) > 1: return False
                if i[0] == '-': return False
            return True
    def IPv6(self, IP):
            collec = IP.split(':')
            if len(collec) != 8:
                return False
            for i in collec:
                try:
                    if int(i, 16) > int('ffff', 16): return False
                except ValueError:
                    return False
                if len(i) > 4: return False
                if i[0] == '-': return False
            return True
    def validIPAddress(self, IP: str) -> str:
        if self.IPv4(IP): return 'IPv4'
        elif self.IPv6(IP): return 'IPv6'
        else: return 'Neither'
class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        if '.' in IP:
            
            c = IP.count('.')
            if c != 3:
                return 'Neither'
            
            ip = IP.split('.')
            
            for num in ip:
                try:
                    flag = (str(int(num))==num and 0<=int(num)<=255)
                    if not flag:
                        return 'Neither'
                except:
                    return 'Neither'
            
            return 'IPv4'
        
        elif ':' in IP:
            
            c = IP.count(':')
            if c != 7:
                return 'Neither'
            
            ip = IP.split(':')
            
            for num in ip:
                try:
                    flag = (1<=len(num)<=4 and int(num,16)>=0 and num[0]!='-')
                    if not flag:
                        return 'Neither'
                except:
                    return 'Neither'
            
            return 'IPv6'
        
        else:
            return 'Neither'
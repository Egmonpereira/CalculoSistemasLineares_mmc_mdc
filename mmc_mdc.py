class MMC_MDC():
    def mmc(nums):
        n = []
        n.append(int(nums[0]))
        n.append(int(nums[1]))
        max_ = max(n)

        i = 1
        
        while True:
            mult = max_ * i
            if mult % n[0] == 0 and mult % n[1] == 0:
                return mult
            else:
                i += 1
            
    def mdc(nums):
        v = input('Visualizar cálculo MDC? [S/N]: ')
        
        n = []
        n.append(int(nums[0]))
        n.append(int(nums[1]))
        max_ = max(n)
        min_ = min(n)
        aux = 1
        d = 2
        print(int(max_),int(min_),d)

        while max_ != 1 and min_ != 1:
            if max_ % d == 0 and min_ % d == 0:
                aux = aux * d
                max_ = max_ / d
                min_ = min_ / d
                if v == 's' or v == 'S':
                    print(int(max_),int(min_),d)
            else:     
                if max_ % d == 0:
                    max_ = max_ / d
                if min_ % d == 0:
                    min_ = min_ / d
                d += 1
                if v == 's' or v == 'S':
                    print(int(max_),int(min_),d)
        return aux
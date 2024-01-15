def limit(arr,_min=None,_max=None):
    if _min!=None:
        for i in arr:
            if i<=_min:
                pass
            else:
                del i
    else:
        pass
    if _max!=None:
         for i in arr:
            if i>=_max:
                pass
            else:
                del i
    else:
        pass
print(limit([2,5,7,6,8,4,1],8))
aplhabets=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#Shifting Function
def ceaser_shift(sti,shift,cond="encode"):
    st=[]
    for j in sti:
        st.append(j.lower())
    st="".join(st)
    if(cond=="decode"):
        shift=(-shift)
    newwrd=[]
    
    for i in st:
        if(i==" "):
            newwrd.append(i)
        else:
            if(aplhabets.index(i)+shift>len(aplhabets)):
                ind=aplhabets.index(i)+shift-len(aplhabets)
            else:
                ind=aplhabets.index(i)+shift
            newwrd.append(aplhabets[ind])
    return("".join(newwrd))
list_A=[]

def list_sort(list_A): 
    list_of_even=[]
    list_of_odds=[]
    list_of_char=[]
    list_of_other=[]
    dict_A ={}
    for i in list_A:
        if isinstance (i,int):
            if (i%2==0):
                list_of_even.append(i)   
            else:
                list_of_odds.append(i)       
        elif isinstance (i,str):
            list_of_char.append(i)
        else:
            list_of_other.append(i)
            
    dict_A['chars']=sorted(list_of_char)
    dict_A['evens']=sorted(list_of_even) 
    dict_A['odds']=sorted(list_of_odds)
    dict_A['others']=sorted(list_of_other)

    print(dict_A)
list_sort(list_A)

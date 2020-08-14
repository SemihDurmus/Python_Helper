# Assignment_18_Most_Frequent_Element

"""Given a list, return the most frequent (repeating) element."""

def most_freq(given_list):
    rep = 0

    result = given_list[0]
    
    for i in given_list:
        
        live_rep = given_list.count(i)
        
        if live_rep > rep:
            rep = live_rep
            result = i    
            
    return result


# Shorter way
# def my_fact(n):
#    return 1 if n==0 else n*my_fact(n-1)

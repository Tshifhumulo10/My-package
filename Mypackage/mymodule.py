def Top_n(item, n):
    """the function returns the top n value in a descending order
    
    Args:
        items(array): List or array like object
        n(int): number of item to be returned
    
    return:
        array: return top n item, in descending order.

    EGs:
        Top_num([8,6,4,5,2,9], 3)
        (9,8,6)
     """
    item.sort(descending=True)
    Top_three=item[:n+1]
    return(Top_three)
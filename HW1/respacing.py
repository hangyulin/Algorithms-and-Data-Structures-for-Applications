# TODO: Hangyu Lin (John), hl2357
# TODO: Guanchen Zhang (James), gz256

# DO NOT CHANGE THIS CLASS
class RespaceTableCell:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.validate()

    # This function allows Python to print a representation of a RespaceTableCell
    def __repr__(self):
        return "(%s,%s)"%(str(self.value), str(self.index))

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.value) == bool), "Values in the respacing table should be booleans."
        assert(self.index == None or type(self.index) == int), "Indices in the respacing table should be None or int"

# Inputs: the dynamic programming table, indices i, j into the dynamic programming table, the string being respaced, and an "is_word" function.
# Returns a RespaceTableCell to put at position (i,j)
def fill_cell(T, i, j, string, is_word):
    #TODO: YOUR CODE HERE
    length = j - i
    is_word_bool = False
    break_index = None
    if length == 0:
        is_word_bool = is_word(string[i])
        if is_word_bool:
            break_index = i
    elif is_word(string[i:j + 1]):
        is_word_bool = True
        break_index = i
    else:
        while is_word_bool == False and length >= 1:
            left_bool, left_index = T.get(i, j - length).value, T.get(i, j - length).index  
            if left_bool:
                is_word_bool = True
                new_j = j - length + 1
                
                left_bool_temp, left_index_temp = T.get(new_j, j).value, T.get(new_j, j).index
                if left_bool_temp:
                    is_word_bool = True
                    break_index = left_index_temp
                else:
                    is_word_bool = False
                    break_index = None
            length -= 1
    return RespaceTableCell(is_word_bool, break_index)
                  
# Inputs: N, the size of the list being respaced
# Outputs: a list of (i,j) tuples indicating the order in which the table should be filled.
def cell_ordering(N):
    order_list = []
    for i in range(N):
        for j in range(N - i):
            order_list.append((j, i + j))
    return order_list

# Input: a filled dynamic programming table.
# (See instructions.pdf for more on the dynamic programming skeleton)
# Return the respaced string, or None if there is no respacing.
def respace_from_table(s, table):
    check_order = (0, len(s)-1)
    which_i = None
    which_j = None
    i, j = check_order
    
    if table.get(i, j).value:
        which_i, which_j = i, j
        
    if which_i == None and which_j == None:
        return None
    store_list = []
    store_list_2 = []
    for k in range(which_i, which_j + 1):
        if table.get(which_i, k).value:
            if len(store_list) > 0:
                if store_list_2[-1] == table.get(which_i, k).index:
                    store_list[-1] = k
                else:
                    store_list.append(k)
                    store_list_2.append(table.get(which_i, k).index)
            else:
                store_list.append(k)
                store_list_2.append(table.get(which_i, k).index)
    if len(store_list) != 1:
        respaced_string = s[:store_list_2[1]]

        for m in range(2, len(store_list_2)):
            respaced_string = respaced_string + " " + s[store_list_2[m - 1]:store_list_2[m]]
        respaced_string = respaced_string + " " + s[store_list_2[-1]:store_list[-1] + 1]
    else:
        respaced_string = None
    return respaced_string

if __name__ == "__main__":
    # Example usage.
    from dynamic_programming import DynamicProgramTable
    s = "itwasthebestoftimes"
    wordlist = ["of", "it", "the", "best", "times", "was"]
    D = DynamicProgramTable(len(s) + 1, len(s) + 1, cell_ordering(len(s)), fill_cell)
    D.fill(string=s, is_word=lambda w:w in wordlist)
    print respace_from_table(s, D)

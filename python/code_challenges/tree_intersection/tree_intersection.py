from code_challenges.tree.tree import BinaryTree

def tree_intersection(bt1, bt2):
    common_val = []

    if not bt1.root or not bt2.root: 
        raise ValueError('cannot operate on an empty tree')

    
    bt1_vals = bt1.pre_order()
    bt2_vals = bt2.pre_order()
   

    for val in bt1_vals:
        for num in bt2_vals:
            if val == num:
                common_val.append(val)
                print(common_val)
                
            else:
                continue
    common_val.sort()
    return common_val

        
def delete(list_, index=None):
    if isinstance(index,  int) and index != -1:
        if not index:
            index = 0
            result = list_[1:]
        elif index > 0:
            result = list_[0:index] + list_[index + 1:]
        else:
            len_ = len(list_)
            new_index = len_ + index
            result = list_[0:index] + list_[index + 1:]
    else:
         result = list_[:-1]
    return result


print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))
print(delete([0, 1, 2, 3, 4], index=-1))
print(delete([0, 1, 2, 3, 4], index=-3))

def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open('txt_file\data01.txt')
    txt=[f.read()]
   # txt=[txt]
    return txt
print(main('data01.txt'))
# Read data from file
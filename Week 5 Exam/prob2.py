""" Center Allign """
def center_alligning(file_name):
    centered_line_list=[]
    with open(file_name, 'r') as file:
        lines=file.readlines()
    file.close()
    
    for line in lines:
        strip_line=line.strip()
        center_line=strip_line.center(50)
        center_line=center_line + '\n'
        centered_line_list.append(center_line)

    with open(file_name, 'w') as file:
        file.writelines(centered_line_list)
    file.close()

file_name="center_allign.txt"
center_alligning(file_name)
import os

sample_txt = "/home/sef/Desktop/Ayvos_Staj/txtfile_edit" #path_directory
modified = []

def count_index(modified):
    x = 0
    for x in modified[:0]:
        return modified.count(modified[x])

for txt_file in os.listdir(sample_txt):
    if txt_file.endswith(".txt"):
        line = os.open(sample_txt,'r')
        read = line.readlines()
        i = 0
        for line in read:
            if line[i] != '\0':
                modified.append()
                print(modified)
                i += 1
                break
            else:
                break

print(count_index(modified))
        
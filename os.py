import os 

if not os.path.exists("data"):

 for i in range(0,10): 
    os.mkdir(f"data/day{i+1}")

def create_file(folder_path,file_name,content=""):
    file_path = os.path.join(folder_path,file_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(file_path,'w') as file:
        file.write(content)

folder_path =r'C:\Users\Developer.DEV_HIMANSHU_SR\Desktop\Python_module'
file_name="name.txt"
content= "Hello,this is Himanshu Srivastava"

create_file(folder_path,file_name,content)
       
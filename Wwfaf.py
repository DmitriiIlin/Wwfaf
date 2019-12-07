import os.path, datetime, random

def all_files_and_folders_in_current_folder():
    all_files = []
    all_directories = []
    all_roots=[]
    res = {}
    for root, dirs , files in os.walk('.') :
        all_roots.append(root)
        all_directories.append(dirs)
        all_files.append(files)
    res['all_roots']=all_roots    
    res['all_files'] = all_files
    res['all_directories'] = all_directories
    return res    

#print(all_files_and_folders_in_current_folder())

def create_folder(folder_name):
    #Ф-ция создает папку с именем folder_name
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)

def create_files(folder_path):
    current_working_directory=os.getcwd()
    os.chdir(folder_path)
    for i in range(1,11):
        file=open(str(i)+".txt",'wt')
        for _ in range(0,3):
            file.write(str(random.randint(1,100))+'\n')
        file.close()
    os.chdir(current_working_directory)

def delete_folder(flag = False , folder_name = None):
    # Ф-ция удаляет каталог и все файлы внутри него. Если есть подкаталоги нечего не удаляется.
    # Перед тем как удалить каталог, создается папка, 10 файлов внутри каталога и в зависимости от flag создается подкаталог.
    path = 'C:/Users/Дмитрий/AppData/Local/Programs/Python/Python37-32/'
    folder_name = str(folder_name)
    now = datetime.datetime.now()
    day = now.day
    month = now.month
    year = now.year
    full_folder_path = str(path) + str(folder_name) + str("-") + str(day) + str("-") + str(month) + str("-") + str(year)
    #print(full_folder_path)
    create_folder(full_folder_path)
    #relative_path=os.path.join(os.getcwd() , os.path.normpath(full_folder_path))
    #print(relative_path)
    if flag == True :
        create_files(full_folder_path) 
        current_working_directory=os.getcwd()
        os.chdir(full_folder_path)
        if not os.path.isdir(str(day)):
           os.makedirs(str(day))
        os.chdir(current_working_directory)
        res=all_files_and_folders_in_current_folder()
        for every_directories in range(len(res['all_directories'])):
            for every_folder in range(len(res['all_directories'][every_directories])):
                if str(day) == res['all_directories'][every_directories][every_folder]:
                    print(res['all_directories'][every_directories][every_folder])
                    break
            break
    else:   
        os.rmdir(full_folder_path)


    

           
delete_folder(False)

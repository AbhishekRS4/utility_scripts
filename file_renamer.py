import os

def file_renamer(dir_data="sift_features/", str_source="kmeans", str_target="sift"):
    list_files = sorted([file_ for file_ in os.listdir(dir_data) if str_source in file_])
    print("Num files to be renamed : {len(list_files)}")
    for file_ in list_files:
        os.rename(os.path.join(dir_data, file_), os.path.join(dir_data, file_.replace(str_source, str_target)))
    print("All files renamed successfully")

def main():
    file_renamer()

main()

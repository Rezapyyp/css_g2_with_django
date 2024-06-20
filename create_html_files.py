from config.settings import BASE_DIR
from os import listdir
from pprint import pprint
PATH_GENERATED_FILES = BASE_DIR / "GeneratedFiles"


class Genrator :
        
    def craete_css_file(self,css_file_name):
        file_name = f"{css_file_name}.css"
        if file_name in listdir(PATH_GENERATED_FILES):
            print("Warning : This file already exsits!")
        else :
            fn = PATH_GENERATED_FILES / file_name
            with open(fn,"w"):
                print(f"Created a new file on {fn} ")
    
    def craete_html_file(self,html_file_name):
        file_name = f"{html_file_name}.html"
        if file_name in listdir(PATH_GENERATED_FILES):
            print("Warning : This file already exsits!")
        else :
            fn = PATH_GENERATED_FILES / file_name
            with open(fn,"w"):
                print(f"Created a new file on {fn} ")
    
    def read_html_file(self,html_file_name):
        file_name = f"{html_file_name}.html"
        fn = PATH_GENERATED_FILES / file_name
        with open(fn , "r") as f :
            # print(f.read())
            return f.read()

    def node_of_html_file(self,html_file_name):
        file = self.read_html_file(html_file_name)
        # print(file.splitlines())
        # pprint(file.split())
        # print(file.strip())
        # print(file.partition())
        
        # for s in file.split():
        #     print(s)
        #     print("\n")
        


obj = Genrator().node_of_html_file("my_new_file")






import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.gz': 
                    print(full_filename)
                text = os.path.splitext(full_filename)[-2]		
                #print(text)
                text2 = os.path.splitext(text)[-2]
                #print(text2)
                text3 = os.path.basename(text2)
                #print(text3)	
                if "_1" in text3:
                    text4=text3
                    print(text4)

    except PermissionError:
        pass

search("/home/bike/rna-seq/chrX_data/samples/")

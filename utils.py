import os
import unidecode



def get_file_number(dir_path):
    count = 0

    try:

        for path in os.listdir(dir_path):
            
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1

        return count + 1
    except:
        return count
    


def cleanAllPaths(theme):
    
    try:
        cleanPath(f"projects/images/{unidecode(theme.replace(' ', '-'))}")
        cleanPath(f"projects/audios/{unidecode(theme.replace(' ', '-'))}")
        cleanPath(f"projects/videos/{unidecode(theme.replace(' ', '-'))}")
    except:
        pass



def cleanPath(path):

   for filename in os.listdir(path):

       file_path = os.path.join(path, filename)

       try:
           if os.path.isfile(file_path) or os.path.islink(file_path):
               os.unlink(file_path)

       except Exception as e:
           print('Failed to delete %s. Reason: %s' % (file_path, e))
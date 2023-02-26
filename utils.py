import os


def get_file_number(dir_path):
    count = 0

    try:

        for path in os.listdir(dir_path):
            
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1

        return count + 1
    except:
        return count
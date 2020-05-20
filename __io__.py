import os
import pickle
STORAGE_FOLDER = "./data/"
STUDENTS_FILE = "students.p"
GROUPS_FILE = "groups.p"
EMAILS_FILE = "emails.p"
NOTES_FILE = "notes.p"
UIDS_FILE = "uids.p"
FILES = [STUDENTS_FILE, GROUPS_FILE, EMAILS_FILE, NOTES_FILE, UIDS_FILE]


def _check_if_files_and_storage_exist():
    """Checks whether the files are initialised in their respective folder"""

    def _check_if_folder_exists():
        """Checks if the folder for storing data exists. If not, it creates a folder."""
        if not os.path.isdir(STORAGE_FOLDER):
            os.mkdir(STORAGE_FOLDER)

    _check_if_folder_exists()

    def _check_if_files_exist():
        """Checks if the .json files exist. Initialises the files if not."""
        for i in FILES:
            if os.path.exists(STORAGE_FOLDER + i):
                continue
            else:
                with open(STORAGE_FOLDER + i, "x") as the_file:
                    pass
    
    _check_if_files_exist()

_check_if_files_and_storage_exist()

def load_file(to_load):
    """Loads the content of a file and returns it"""
    with open(STORAGE_FOLDER + to_load, "rb") as the_file:
        # NOTE(tnebes) a dumb way to handle exceptions
        # NOTE(tnebes) unpickling needs to be done until there is no pickled data left.
        #       In essence, each group of bytes is pickled seperately,
        #       thus it is needed to unpickle until we hit EOFError.
        # NOTE(tnebes) this is not the case here LOL. why.
        # TODO:(tnebes) remove the while True since there is no reason for it to be there.
        the_data = None
        while True:
            try:
                the_data = pickle.loads(the_file.read())
            except EOFError:
                break
        if type(the_data) is dict:
            return the_data
        elif not the_data:
            return None
        else:
            return {the_data.uid: the_data}
    
def write_file(data, to_write, load=True):
    """Writes the data to the file (to_write). If load is set to False, it will not load the previous file and append it with the data to be written."""

    if load:
        loaded_file = load_file(to_write)
        if loaded_file:
            loaded_file[data.uid] = data
            # NOTE(tnebes) swapping variables so that the code below works. This is dumb.
            (loaded_file, data) = (data, loaded_file)
        del loaded_file

    with open(STORAGE_FOLDER + to_write, "wb") as the_file:
       the_file.write(pickle.dumps(data, pickle.HIGHEST_PROTOCOL))


import tkinter as tk
from tkinter import ttk
from classes import *
import __io__ as io
import gui


DEFAULT_UIDS = {
    "student_uid": 0,
    "group_uid": 10000,
    "email_uid": 20000,
    "notes_uid": 30000,
    }

def load_uids_from_file():
    """Loads the uid counters from a file"""
    uids = io.load_file(io.UIDS_FILE)
    if not uids:
        save_uids_to_file(DEFAULT_UIDS)
        return load_uids_from_file()
    return uids

def save_uids_to_file(uids, **load):
    """Saves the UID counters to a file"""
    io.write_file(uids, io.UIDS_FILE, load)

# NOTE(tnebes): loading uids into memory and setting the run_loop() function up that will be used in main()
# TODO: there has to be a better way of initialising the gui and the loop.
#   this just seems dumb.
current_uids = load_uids_from_file()
the_gui = gui._create_tabs()
run_loop = gui.main_window.mainloop

# TODO:
    # here are listed all the things that need to be done in order for
    # the student tab to work properly. This list will include functions
    # for the student tab.

    # the gui needs to load a student load_student()
        # the first student will be loaded according to the smallest UID
        # within the range of student_uid to group_uid.
            # if no student is found, then prompt the user to enter the data
            # for the first student whose uid will be 0
            # the user will enter the data for the first student and save it.
    # once the uid is loaded, the logic will populate the first and last name
    # and populate the full name as well.
        # and all the other things as well.
        # populate_student_fields()

    # apply will use save_student() and will retrieve data from the entryboxes
    # and listboxes and such and save them to file.
    # The UID will be allocated automatically if ''add'' was pressed or inherited
    # from the current student
        # for now let's use the uids incrementally. There is no reason
        # to fill in the gaps in the uids should a student be removed.
    
    # remove will delete a student from the file
    
    # UID:
    # currently selected UID will be in the entrybox.
    # User can write their own UID and go there. Should the UID be nonexistant,
    # the goto button should blink red? Need to find a way to give feedback.
    # clicking on the arrow buttons will go to (uid-1) or (uid+1) respectively. If
    # such an UID was not found, continue (uid +- 1) until a valid uid has been found.

    # The students listbox will show all students sorted by their UID.

    



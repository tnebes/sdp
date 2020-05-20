import tkinter as tk
from tkinter import ttk
from classes import *


SCREEN_RESOLUTION = "800x600"
VERSION = "0.2"

main_window = tk.Tk()
main_window.title("Student Data Programme " + VERSION)
main_window.resizable(False, False)
main_window.geometry(SCREEN_RESOLUTION)
main_window_tab_notebook = ttk.Notebook(main_window)

def _create_tabs():
    """Creates all the tabs necessary for the program to work.
    Function returns all the tabs which contain all the GUI elements"""

    all_tabs = {}

    def _create_student_tab():
        """creates all the elements of the student tab and returns the elements which are storied in the My_Tab class"""
        # NOTE(tnebes) All the frames in this tab
        this_tab = My_Tab("students")
        this_tab.frame = tk.Frame(main_window)
        this_tab.student_info_frame = tk.Frame(this_tab.frame)
        this_tab.all_students_frame = tk.Frame(this_tab.frame)
        this_tab.uid_frame = tk.Frame(this_tab.frame)

        this_tab.name_label = My_Label(
                this_tab.student_info_frame,
                text="Name:",
                column=0, row=0)
        this_tab.first_name_label = My_Label(
                this_tab.student_info_frame,
                text="First name:",
                column=0, row=1, pady=8)
        this_tab.last_name_label = My_Label(
                this_tab.student_info_frame,
                text="Last Name:",
                column=0, row=2, pady=9)
        this_tab.first_name_entry = My_Entry(
                this_tab.student_info_frame,
                width=32, column=1,
                row=1, pady=8)
        this_tab.last_name_entry = My_Entry(
                this_tab.student_info_frame,
                width=32,
                column=1, row=2,
                pady=8)
        this_tab.student_groups_label = My_Label(
                this_tab.student_info_frame,
                text="Groups:",
                column=0, row=3)
        this_tab.student_groups = My_Listbox(
                this_tab.student_info_frame,
                height=4, width=32,
                column=1, row=3)
        this_tab.student_emails_label = My_Label(
                this_tab.student_info_frame,
                text="E-mails:", column=0,
                row=4)
        this_tab.student_emails = My_Listbox(
                this_tab.student_info_frame,
                height=4, width=32,
                column=1, row=4)
        this_tab.student_notes_label = My_Label(
                this_tab.student_info_frame,
                text="Notes:", column=0,
                row=5)
        this_tab.student_notes = My_Listbox(
                this_tab.student_info_frame,
                height=10, width=32,
                column=1, row=5)
        this_tab.change_data_button = My_Button(
                this_tab.student_info_frame,
                text="Apply", column=1,
                row=6, sticky="W")
        this_tab.add_student_button = My_Button(
                this_tab.student_info_frame,
                text="Add", column=1,
                row=6, sticky="N")
        this_tab.remove_student_button = My_Button(
                this_tab.student_info_frame,
                text="Remove", column=1,
                row=6, sticky="E")

        this_tab.all_students_label = My_Label(
                this_tab.all_students_frame,
                text="Students:", column=0,
                row=0, sticky="W")
        this_tab.all_students_listbox = My_Listbox(
                this_tab.all_students_frame,
                height=20,width=32,
                column=0, row=1)

        this_tab.student_uid_label = My_Label(
                this_tab.uid_frame,
                text="UID:", column=0,
                row=0)
        this_tab.student_uid_entry = My_Entry(
                this_tab.uid_frame,
                width=32, column=1,
                row=0)
        this_tab.student_uid_goto_button = My_Button(
                this_tab.uid_frame,
                text="goto", column=1,
                row=1)
        this_tab.student_uid_previous_button = My_Button(
                this_tab.uid_frame,
                text="<", column=0, row=1)
        this_tab.student_uid_next_button = My_Button(
                this_tab.uid_frame,
                text=">", column=2, row=1)

        main_window_tab_notebook.add(
                this_tab.frame,
                text="Student")
        main_window_tab_notebook.pack(
                expand=1,
                fill="both",
                side="left")

        def _organise_student_tab(the_tab):
            """organises the elements in the student tab"""
            #NOTE(tnebes) this is dumb. don't do this
            the_tab.frame.pack()
            the_tab.student_info_frame.pack(side=tk.LEFT)
            the_tab.all_students_frame.pack(side=tk.RIGHT)
            the_tab.uid_frame.pack(side=tk.BOTTOM)

        _organise_student_tab(this_tab)
        main_window_tab_notebook.add(
                this_tab.frame,
                text="Student")
        main_window_tab_notebook.pack(
                expand=1, fill="both",
                side="left")

        return this_tab
    
    all_tabs["students"] = _create_student_tab()

    def _create_groups_tab():

        this_tab = My_Tab("groups")

        this_tab.frame = tk.Frame(main_window)
        this_tab.frame.pack()
        this_tab.groups_frame = tk.Frame(this_tab.frame)
        this_tab.groups_frame.pack(side="left")

        this_tab.groups_label = My_Label(
                this_tab.groups_frame, text="Groups:",
                column=0, row=0, sticky="W")
        this_tab.groups_listbox = My_Listbox(
                this_tab.groups_frame,
                height=16, width=32,
                column=0, row=1)
        this_tab.add_group_button = My_Button(
                this_tab.groups_frame, text="Add",
                column=0, row=2, sticky="W")
        this_tab.change_group_button = My_Button(
                this_tab.groups_frame, text="Change",
                column=0, row=2, sticky="W")
        this_tab.remove_group_button = My_Button(
                this_tab.groups_frame, text="Remove",
                column=0, row=2, sticky="E")

        this_tab.students_group_frame = tk.Frame(this_tab.frame)
        this_tab.students_group_frame.pack(side="right")
        this_tab.students_group_label = My_Label(
                this_tab.students_group_frame,
                text="Students in group:",
                column=0, row=0, sticky="W")
        this_tab.students_group_listbox = My_Listbox(
                this_tab.students_group_frame,
                height=32, width=24,
                column=0, row=1)
        this_tab.students_add_button = My_Button(
                this_tab.students_group_frame,
                text="Add", column=0, row=2,
                sticky="W")
        this_tab.students_remove_button = My_Button(
                this_tab.students_group_frame,
                text="Remove", column=0, row=2,
                sticky="E")

        main_window_tab_notebook.add(
                this_tab.frame, text="Groups")
        main_window_tab_notebook.pack(
                expand=1, fill="both",
                side="left")

        return this_tab
        
    all_tabs["groups"] = _create_groups_tab()

    def _create_emails_tab():

        this_tab = My_Tab("emails")

        this_tab.frame = tk.Frame(main_window)
        this_tab.frame.pack()
        this_tab.email_filter_frame = tk.Frame(this_tab.frame)
        this_tab.email_filter_frame.pack(side="left")
        this_tab.email_list_frame = tk.Frame(this_tab.frame)
        this_tab.email_list_frame.pack(side="right")
        
        this_tab.check_students_emails = My_Checkbutton(
                this_tab.email_filter_frame, "Students",
                column=0, row=0, sticky="W")
        this_tab.check_group_emails = My_Checkbutton(
                this_tab.email_filter_frame, "Groups",
                column=0, row=0, sticky="E")
        this_tab.emails_listbox = My_Listbox(
                this_tab.email_filter_frame,
                height=28, width=32,
                column=0, row=1)
        
        this_tab.emails_label = My_Label(
                this_tab.email_list_frame, text="Emails:",
                column=0, row=0,
                sticky="W")
        this_tab.emails_listbox = My_Listbox(
                this_tab.email_list_frame,
                height=28, width=32,
                column=0, row=1)
        this_tab.add_email_button = My_Button(
                this_tab.email_list_frame,
                text="Add",
                column=0, row=2,
                sticky="W")
        this_tab.remove_email_button = My_Button(
                this_tab.email_list_frame,
                text="Remove",
                column=0, row=2,
                sticky="W")

        main_window_tab_notebook.add(
                this_tab.frame, text="E-mails")
        main_window_tab_notebook.pack(
                expand=1, fill="both",
                side="left")

        return this_tab

    all_tabs["emails"] = _create_emails_tab()

    def _create_notes_tab():

        this_tab = My_Tab("notes")

        this_tab.frame = tk.Frame(main_window)
        this_tab.frame.pack()

        this_tab.students_frame = tk.Frame(this_tab.frame)
        this_tab.students_frame.pack(side="left")
        this_tab.student_notes_frame = tk.Frame(this_tab.frame)
        this_tab.student_notes_frame.pack(side="left")
        this_tab.note_frame = tk.Frame(this_tab.frame)
        this_tab.note_frame.pack(side="right")

        this_tab.students_listbox_label = My_Label(
                this_tab.students_frame, text="Students:",
                column=0, row=0,
                sticky="W")
        this_tab.students_listbox = My_Listbox(
                this_tab.students_frame,
                height=28, width=32,
                column=0, row=1)

        this_tab.student_notes_label = My_Label(
                this_tab.student_notes_frame, text="Notes:",
                column=0, row=0,
                sticky="W")
        this_tab.student_notes_listbox = My_Listbox(
                this_tab.student_notes_frame,
                height=10, width=32,
                column=0, row=1)
        this_tab.student_add_note_button = My_Button(
                this_tab.student_notes_frame,
                text="Add",
                column=0, row=2,
                sticky="W")
        this_tab.student_remove_note_button = My_Button(
                this_tab.student_notes_frame,
                text="Remove",
                column=0, row=2,
                sticky="E")

        this_tab.student_note_label = My_Label(
                this_tab.note_frame, text="Note:",
                column=0, row=0,
                sticky="W")
        this_tab.student_note_box = My_Text(
                this_tab.note_frame,
                width=32, height=20,
                column=0, row=1)
        this_tab.student_note_apply = My_Button(
                this_tab.note_frame, text="Apply",
                column=0, row=2,
                sticky="N")
     
        main_window_tab_notebook.add(
                this_tab.frame, text="Notes")
        main_window_tab_notebook.pack(
                expand=1, fill="both",
                side="left")

        return this_tab

    all_tabs["notes"] = _create_notes_tab()

    return all_tabs




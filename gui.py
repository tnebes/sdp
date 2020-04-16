import tkinter as tk
from tkinter import ttk
from classes import *

main_window = tk.Tk()
main_window.title("Student Data Programme 0.1")
main_window.resizable(False, False)
main_window.geometry("800x600")
main_window_tab_notebook = ttk.Notebook(main_window)

def create_tabs():

    tab_contents = {}

    def create_student_tab():

        # placing all these in a dictionary so that we can use them outside the function.
        student_gui_objects = {}
        
        this_tab_frame = tk.Frame(main_window)
        this_tab_frame.pack()
        student_info_frame = tk.Frame(this_tab_frame)
        student_info_frame.pack(side=tk.LEFT)
        all_students_frame = tk.Frame(this_tab_frame)
        all_students_frame.pack(side=tk.RIGHT)
        uid_frame = tk.Frame(this_tab_frame)
        uid_frame.pack(side=tk.BOTTOM)
        student_gui_objects["this_tab_frame"] = this_tab_frame
        student_gui_objects["student_info_frame"] = student_info_frame
        student_gui_objects["all_students_frame"] = all_students_frame
        student_gui_objects["uid_frame"] = uid_frame

        first_name_entry_var = tk.StringVar()
        last_name_entry_var = tk.StringVar()
        name_label = ttk.Label(student_info_frame, text="Name:")
        first_name_label = ttk.Label(student_info_frame, text="First name:")
        last_name_label = ttk.Label(student_info_frame, text="Last Name:")
        first_name_entry = ttk.Entry(student_info_frame, width=32, textvariable=first_name_entry_var)
        last_name_entry = ttk.Entry(student_info_frame, width=32, textvariable=last_name_entry_var)
        student_gui_objects["first_name_entry_var"] = first_name_entry_var
        student_gui_objects["last_name_entry_var"] = last_name_entry
        student_gui_objects["name_label"] = name_label
        student_gui_objects["first_name_label"] = first_name_label
        student_gui_objects["last_name_label"] = last_name_label
        student_gui_objects["first_name_entry"] = first_name_entry
        student_gui_objects["last_name_entry"] = last_name_entry

        name_label.grid(column=0, row=0)
        first_name_label.grid(column=0, row=1, pady=8)
        first_name_entry.grid(column=1, row=1, pady=8)
        last_name_label.grid(column=0, row=2, pady=8)
        last_name_entry.grid(column=1, row=2, pady=8)
        
        student_groups_label = ttk.Label(student_info_frame, text="Groups:")
        student_groups = tk.Listbox(student_info_frame, height=4, width=32)
        student_emails_label = ttk.Label(student_info_frame, text="E-mails:")
        student_emails = tk.Listbox(student_info_frame, height=4, width=32)
        student_notes_label = ttk.Label(student_info_frame, text="Notes:")
        student_notes = tk.Listbox(student_info_frame, height=10, width=32)
        change_data_button = tk.Button(student_info_frame, text="Apply")
        add_student_button = tk.Button(student_info_frame, text="Add")
        remove_student_button = tk.Button(student_info_frame, text="Remove")
        student_gui_objects["student_groups_label"] = student_groups_label
        student_gui_objects["student_groups"] = student_groups
        student_gui_objects["student_emails_label"] = student_emails_label
        student_gui_objects["student_emails"] = student_emails
        student_gui_objects["student_notes_label"] = student_notes_label
        student_gui_objects["student_notes"] = student_notes
        student_gui_objects["change_data_button"] = change_data_button
        student_gui_objects["add_student_button"] = add_student_button
        student_gui_objects["remove_student_button"] = remove_student_button

        student_groups_label.grid(column=0, row=3)
        student_groups.grid(column=1, row=3)
        student_emails_label.grid(column=0, row=4)
        student_emails.grid(column=1, row=4)
        student_notes_label.grid(column=0, row=5)
        student_notes.grid(column=1, row=5)
        change_data_button.grid(column=1, row=6, sticky="W")
        add_student_button.grid(column=1, row=6, sticky="N")
        remove_student_button.grid(column=1, row=6, sticky="E")

        all_students_label = tk.Label(all_students_frame, text="Students:")
        all_students_label.grid(column=0, row=0, sticky="W")
        all_students_listbox = tk.Listbox(all_students_frame, height=20, width=32)
        all_students_listbox.grid(column=0, row=1)
        student_gui_objects["all_students_label"] = all_students_label
        student_gui_objects["all_students_listbox"] = all_students_listbox

        student_uid_label = tk.Label(uid_frame, text="UID:")
        student_uid_entry_var = tk.StringVar()
        student_uid_entry = ttk.Entry(uid_frame, width=32, textvariable=student_uid_entry_var)
        student_uid_goto_button = ttk.Button(uid_frame, text="goto")
        student_uid_previous_button = ttk.Button(uid_frame, text="<")
        student_uid_next_button = ttk.Button(uid_frame, text=">")
        student_gui_objects["student_uid_label"] = student_uid_label
        student_gui_objects["student_uid_entry_var"] = student_uid_entry_var
        student_gui_objects["student_uid_entry"] = student_uid_entry
        student_gui_objects["student_uid_goto_button"] = student_uid_goto_button
        student_gui_objects["student_uid_previous_button"] = student_uid_previous_button
        student_gui_objects["student_uid_next_button"] = student_uid_next_button

        student_uid_label.grid(column=0, row=0)
        student_uid_entry.grid(column=1, row=0)
        student_uid_goto_button.grid(column=1, row=1)
        student_uid_previous_button.grid(column=0, row=1)
        student_uid_next_button.grid(column=2, row=1)

        main_window_tab_notebook.add(this_tab_frame, text="Student")
        main_window_tab_notebook.pack(expand=1, fill="both", side="left")

        return student_gui_objects
   
    tab_contents["students"] = create_student_tab()

    def create_groups_tab():
        
        group_ui_objects = {}

        group_ui_objects["this_tab_frame"] = tk.Frame(main_window)
        this_tab_frame = group_ui_objects["this_tab_frame"]
        this_tab_frame.pack()
        group_ui_objects["groups_frame"] = tk.Frame(this_tab_frame)
        groups_frame = group_ui_objects["groups_frame"]
        groups_frame.pack(side="left")

        group_ui_objects["groups_label"] = groups_label = tk.Label(groups_frame, text="Groups:")
        groups_label.grid(column=0, row=0, sticky="W")
        group_ui_objects["groups_listbox"] = groups_listbox = tk.Listbox(groups_frame, height=16, width=32)
        groups_listbox.grid(column=0, row=1)
        group_ui_objects["add_group_button"] = add_group_button = tk.Button(groups_frame, text="Add")
        add_group_button.grid(column=0, row=2, sticky="W")
        group_ui_objects["change_group_button"] = change_group_button = tk.Button(groups_frame, text="Change")
        change_group_button.grid(column=0, row=2, sticky="N")
        group_ui_objects["remove_group_button"] = remove_group_button = tk.Button(groups_frame, text="Remove")
        remove_group_button.grid(column=0, row=2, sticky="E")

        group_ui_objects["students_group_frame"] = tk.Frame(this_tab_frame)
        students_group_frame = group_ui_objects["students_group_frame"]
        students_group_frame.pack(side="right")
        group_ui_objects["students_group_label"] = students_group_label = tk.Label(students_group_frame, text="Students in group:")
        students_group_label.grid(column=0, row=0, sticky="W")
        group_ui_objects["students_group_listbox"] = students_group_listbox = tk.Listbox(students_group_frame, height=32, width=24)
        students_group_listbox.grid(column=0, row=1)
        group_ui_objects["students_add_button"] = students_add_button = tk.Button(students_group_frame, text="Add")
        students_add_button.grid(column=0, row=2, sticky="W")
        group_ui_objects["students_remove_button"] = students_remove_button = tk.Button(students_group_frame, text="Remove")
        students_remove_button.grid(column=0, row=2, sticky="E")

        main_window_tab_notebook.add(this_tab_frame, text="Groups")
        main_window_tab_notebook.pack(expand=1, fill="both", side="left")

        return group_ui_objects

    tab_contents["groups"] = create_groups_tab()

    def create_emails_tab():

        email_ui_objects = {}

        email_ui_objects["this_tab_frame"] = this_tab_frame = tk.Frame(main_window)
        this_tab_frame.pack()
        email_ui_objects["email_filter_frame"] = email_filter_tab = tk.Frame(this_tab_frame)
        email_filter_tab.pack(side="left")
        email_ui_objects["email_list_frame"] = email_list_frame = tk.Frame(this_tab_frame)
        email_list_frame.pack(side="right")
        
        email_ui_objects["check_students_emails"] = check_students_emails = My_Checkbutton(email_filter_tab, "Students")
        email_ui_objects["check_group_emails"] = check_group_emails = My_Checkbutton(email_filter_tab, "Groups")
        check_students_emails.the_button.grid(column=0, row=0, sticky="W")
        check_group_emails.the_button.grid(column=0, row=0, sticky="E")
        email_ui_objects["emails_listbox"] = emails_listbox = tk.Listbox(email_filter_tab, height=28, width=32)
        emails_listbox.grid(column=0, row=1)
        
        email_ui_objects["emails_label"] = emails_label = tk.Label(email_list_frame, text="Emails:")
        emails_label.grid(column=0, row=0, sticky="W")
        email_ui_objects["emails_listbox"] = emails_listbox = tk.Listbox(email_list_frame, height=28, width=32)
        emails_listbox.grid(column=0, row=1)
        email_ui_objects["add_email_button"] = add_email_button = tk.Button(email_list_frame, text="Add")
        email_ui_objects["remove_email_button"] = remove_email_button = tk.Button(email_list_frame, text="Remove")
        add_email_button.grid(column=0, row=2, sticky="W")
        remove_email_button.grid(column=0, row=2, sticky="E")

        main_window_tab_notebook.add(this_tab_frame, text="E-mails")
        main_window_tab_notebook.pack(expand=1, fill="both", side="left")

        return email_ui_objects

    tab_contents["emails"] = create_emails_tab()

    def create_notes_tab():

        notes_ui_objects = {}

        notes_ui_objects["this_tab_frame"] = this_tab_frame = tk.Frame(main_window)
        this_tab_frame.pack()

        notes_ui_objects["students_frame"] = students_frame = tk.Frame(this_tab_frame)
        students_frame.pack(side="left")
        notes_ui_objects["student_notes_frame"] = student_notes_frame = tk.Frame(this_tab_frame)
        student_notes_frame.pack(side="left")
        notes_ui_objects["note_frame"] = note_frame = tk.Frame(this_tab_frame)
        note_frame.pack(side="right")

        notes_ui_objects["students_listbox_label"] = students_listbox = tk.Label(students_frame, text="Students:")
        students_listbox.grid(column=0, row=0, sticky="W")
        notes_ui_objects["students_listbox"] = students_listbox = tk.Listbox(students_frame, height=28, width=32)
        students_listbox.grid(column=0, row=1)

        notes_ui_objects["student_notes_label"] = student_notes_label = tk.Label(student_notes_frame, text="Notes:")
        student_notes_label.grid(column=0, row=0, sticky="W")
        notes_ui_objects["student_notes_listbox"] = student_notes_listbox = tk.Listbox(student_notes_frame, height=10, width=32)
        student_notes_listbox.grid(column=0, row=1)
        notes_ui_objects["student_add_note_button"] = student_add_note_button = tk.Button(student_notes_frame, text="Add")
        student_add_note_button.grid(column=0, row=2, sticky="W")
        notes_ui_objects["student_remove_note_button"] = student_remove_note_button = tk.Button(student_notes_frame, text="Remove")
        student_remove_note_button.grid(column=0, row=2, sticky="E")

        notes_ui_objects["student_note_label"] = student_note_label = tk.Label(note_frame, text="Note:")
        student_note_label.grid(column=0, row=0, sticky="W")
        notes_ui_objects["student_note_box"] = student_note_box = tk.Text(note_frame, width=32, height=20)
        student_note_box.grid(column=0, row=1)
        notes_ui_objects["student_note_apply"] = student_note_apply = tk.Button(note_frame, text="Apply")
        student_note_apply.grid(column=0, row=2, sticky="N")
     
        main_window_tab_notebook.add(this_tab_frame, text="Notes")
        main_window_tab_notebook.pack(expand=1, fill="both", side="left")

        return notes_ui_objects

    tab_contents["notes"] = create_notes_tab()

    return tab_contents

print(create_tabs())


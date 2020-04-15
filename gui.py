import tkinter as tk
from tkinter import ttk

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
        student_gui_objects["student_groups_label"] = student_groups_label
        student_gui_objects["student_groups"] = student_groups
        student_gui_objects["student_emails_label"] = student_emails_label
        student_gui_objects["student_emails"] = student_emails
        student_gui_objects["student_notes_label"] = student_notes_label
        student_gui_objects["student_notes"] = student_notes

        student_groups_label.grid(column=0, row=3)
        student_groups.grid(column=1, row=3)
        student_emails_label.grid(column=0, row=4)
        student_emails.grid(column=1, row=4)
        student_notes_label.grid(column=0, row=5)
        student_notes.grid(column=1, row=5)
        
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
        
        this_tab_frame = tk.Frame(main_window)
        this_tab_frame.pack()


        main_window_tab_notebook.add(this_tab_frame, text="Groups")
        main_window_tab_notebook.pack(expand=1, fill="both", side="left")

        group_ui_objects = {}
        return group_ui_objects

    tab_contents["groups"] = create_groups_tab()

    def create_emails_tab():

        this_tab_frame = tk.Frame(main_window)
        this_tab_frame.pack()

        
        main_window_tab_notebook.add(this_tab_frame, text="E-mails")
        main_window_tab_notebook.pack(expand=1, fill="both", side="left")

        email_ui_objects = {}
        return email_ui_objects

    tab_contents["emails"] = create_emails_tab()

    def create_notes_tab():

        this_tab_frame = tk.Frame(main_window)
        this_tab_frame.pack()

        
        main_window_tab_notebook.add(this_tab_frame, text="Notes")
        main_window_tab_notebook.pack(expand=1, fill="both", side="left")

        notes_ui_objects = {}
        return notes_ui_objects

    tab_contents["notes"] = create_notes_tab()

    return tab_contents

print(create_tabs())


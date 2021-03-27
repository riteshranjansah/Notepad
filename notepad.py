#Notepad

import tkinter as tk       #for window creation
from tkinter import ttk     #for label
from tkinter import font,colorchooser,filedialog,messagebox
import os        #for file menu

main_application=tk.Tk()
main_application.geometry("700x600")
main_application.title("Notepad")
main_application.iconbitmap("nicon.ico")   #adding icon
main_menu=tk.Menu()               #menu creation

#file Functions
f_url=None
def new_fun():
    global f_url
    main_application.title("Untitled - Notepad")
    f_url = None
    text_editor.delete(1.0,tk.END)

def open_fun():
    global f_url
    f_url = filedialog.askopenfilename(defaultextension=".txt",
                           filetypes=[("Text Documents", "*.txt"),("All Files", "*.*")])
    try:
        with open(f_url,"r") as f_read:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, f_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(f_url+" - Notepad"))

def save_fun():
    global f_url
    try:
        if f_url == None:
            f_url = filedialog.asksaveasfilename(initialfile = 'Untitled.txt',defaultextension=".txt",
                           filetypes=[("Text Documents", "*.txt"),("All Files", "*.*")])
            if f_url =="":
                f_url = None

            else:
                #Save as a new file
                f = open(f_url, "w")
                f.write(text_editor.get(1.0, tk.END))
                f.close()
                main_application.title(os.path.basename(f_url) + " - Notepad")
        else:
            # Save the file
            f = open(f_url, "w")
            f.write(text_editor.get(1.0, tk.END))
            f.close()
    except:
        return

def save_as_fun():
    global f_url
    try:
        f_url = filedialog.asksaveasfilename(initialfile = 'Untitled.txt',defaultextension=".txt",
                           filetypes=[("Text Documents", "*.txt"),("All Files", "*.*")])
        if f_url =="":
            f_url = None
        else:
            #Save as a new file
            f = open(f_url, "w")
            f.write(text_editor.get(1.0, tk.END))
            f.close()
            main_application.title(os.path.basename(f_url) + " - Notepad")
    except:
        return
def exit_fun():
    global f_url,text_change
    try:
        if text_change:
            mbox=messagebox.askyesnocancel("Warning","Do you want to save the file")
            if mbox is True:
                save_as_fun()
                main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

#file menu icon
new_icon=tk.PhotoImage(file="icon/new.png")
open_icon=tk.PhotoImage(file="icon/open.png")
save_icon=tk.PhotoImage(file="icon/save.png")
save_as_icon=tk.PhotoImage(file="icon/save_as.png")
exit_icon=tk.PhotoImage(file="icon/exit.png")

#File Menu
file=tk.Menu(main_menu,tearoff=False)     #tearoff for not to come out menu
file.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator="Ctrl+n",command=new_fun)
file.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator="Ctrl+o",command=open_fun)
file.add_command(label="Save",image=save_icon,compound=tk.LEFT,accelerator="Ctrl+s",command=save_fun)
file.add_command(label="Save as",image=save_as_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+s",command=save_as_fun)
file.add_separator()
file.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,command=exit_fun)

#Edit Function
def find_fun():
    def find():
        word=find_input.get()
        text_editor.tag_remove("match","1.0",tk.END)
        matches=0
        if word:
            start_pos="1.0"
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match",start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config("match",foreground="red",background="yellow")
    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_popup=tk.Toplevel()
    find_popup.geometry("350x150")
    find_popup.title("Find and Replace Word")
    find_popup.resizable(0,0)

    #frame for find
    find_frame=ttk.LabelFrame(find_popup,text="Find Word")
    find_frame.pack(pady=20)

    #label
    text_find=ttk.Label(find_frame,text="Find")
    text_replace=ttk.Label(find_frame,text="Replace")

    #Entry Box
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)
    
    #Button
    find_btn=ttk.Button(find_frame,text="Find",command=find)
    replace_btn=ttk.Button(find_frame,text="Replace",command=replace)
    
    #Text Label Grid 
    text_find.grid(row=0,column=0,padx=4,pady=4)
    text_replace.grid(row=1,column=0,padx=4,pady=4)

    #Entry Grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    #Button Grid
    find_btn.grid(row=2,column=0,padx=8,pady=4)
    replace_btn.grid(row=2,column=1,padx=8,pady=4)

#Edit menu icon
cut_icon=tk.PhotoImage(file="icon/cut.png")
copy_icon=tk.PhotoImage(file="icon/copy.png")
paste_icon=tk.PhotoImage(file="icon/paste.png")
clear_icon=tk.PhotoImage(file="icon/clear_all.png")
find_icon=tk.PhotoImage(file="icon/find.png")

#Edit menu
edit=tk.Menu(main_menu,tearoff=False)
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator="Ctrl+x",command=lambda:text_editor.event_generate("<<Cut>>"))
edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator="Ctrl+c",command=lambda:text_editor.event_generate("<<Copy>>"))
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator="Ctrl+v",command=lambda:text_editor.event_generate("<<Paste>>"))
edit.add_command(label="Clear All",image=clear_icon,compound=tk.LEFT,accelerator="Ctrl+Atl+x",command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label="Find",image=find_icon,compound=tk.LEFT,accelerator="Ctrl+f",command=find_fun)

#View Function
show_status_bar=tk.BooleanVar()
show_status_bar.set(True)
show_tool_bar=tk.BooleanVar()
show_tool_bar.set(True)

def hide_tool_bar():
    global show_tool_bar
    if show_tool_bar:
        tool_bar.pack_forget()
        show_tool_bar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_tool_bar=True

def hide_status_bar():
    global show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status_bar=True

#view bar icon
tool_icon=tk.PhotoImage(file="icon/tool.png")
status_icon=tk.PhotoImage(file="icon/status.png")

#View Bar 
view=tk.Menu(main_menu,tearoff=False)
view.add_checkbutton(label="Tool Bar",image=tool_icon,compound=tk.LEFT,onvalue=True,offvalue=False,variable=show_tool_bar,command=hide_tool_bar)
view.add_checkbutton(label="Status Bar",image=status_icon,compound=tk.LEFT,onvalue=True,offvalue=False,variable=show_status_bar,command=hide_status_bar)

#Theme icon
light_icon=tk.PhotoImage(file="icon/light.png")
light_plus_icon=tk.PhotoImage(file="icon/light_plus.png")
dark_icon=tk.PhotoImage(file="icon/dark.png")
blue_icon=tk.PhotoImage(file="icon/blue.png")

#Theme menu
theme=tk.Menu(main_menu,tearoff=False)
theme_choose=tk.StringVar()
color_icon=(light_icon,light_plus_icon,dark_icon,blue_icon)   #to use in for loop

color_dict={
    'Light Deafult':('#000000','#ffffff'),
    'Light plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Night Blue':('#ededed','#62b4c9')
}

#Theme Function
def change_theme():
    get_theme=theme_choose.get()
    colour_tuple=color_dict.get(get_theme)
    fg_color,bg_color=colour_tuple[0],colour_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)

count=0
for i in color_dict:
    theme.add_radiobutton(label=i,image=color_icon[count],compound=tk.LEFT,variable=theme_choose,command=change_theme)   #radiobutton is used to select only one
    count+=1

#Help menu
def about():
    messagebox.showinfo("About","This Notepad is made by Ritesh")
def help_view():
    messagebox.showinfo("Help","Mail to: vtu14607@veltech.edu.in")

help=tk.Menu(main_menu,tearoff=False)
view_help_icon=tk.PhotoImage(file="icon/info.png")
about_icon=tk.PhotoImage(file="icon/about.png")
help.add_command(label="Need Help",image=view_help_icon,compound=tk.LEFT,command=help_view)
help.add_command(label="About",image=about_icon,compound=tk.LEFT,command=about)

#Adding Menu bars
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Theme",menu=theme)
main_menu.add_cascade(label="Help",menu=help)

#Tool Bar FOR font,size,bold...
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

#Font
font_design=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state="readonly")
font_box["values"]=font_design
font_box.current(font_design.index("Times New Roman"))
font_box.grid(row=0,column=0,padx=5,pady=5)

#Font size
f_size=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=10,textvariable=f_size,state="readonly")
font_size["values"]=tuple(range(6,100,4))
font_size.current(1)
font_size.grid(row=0,column=1,padx=5)

#Bold 
bold_icon=tk.PhotoImage(file="icon/bold.png")
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

#Italic
italic_icon=tk.PhotoImage(file="icon/italic.png")
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

#underline
un_icon=tk.PhotoImage(file="icon/underline.png")
underline_btn=ttk.Button(tool_bar,image=un_icon)
underline_btn.grid(row=0,column=4,padx=5)

#text color
text_color_icon=tk.PhotoImage(file="icon/color_wheel.png")
text_color_btn=ttk.Button(tool_bar,image=text_color_icon)
text_color_btn.grid(row=0,column=5,padx=5)

#Allign Left
al_l=tk.PhotoImage(file="icon/align-left.png")
allign_left_btn=ttk.Button(tool_bar,image=al_l)
allign_left_btn.grid(row=0,column=6,padx=5)

#Allign Center
al_c=tk.PhotoImage(file="icon/align-center.png")
allign_center_btn=ttk.Button(tool_bar,image=al_c)
allign_center_btn.grid(row=0,column=7,padx=5)

#Allign Right
al_r=tk.PhotoImage(file="icon/align-right.png")
allign_right_btn=ttk.Button(tool_bar,image=al_r)
allign_right_btn.grid(row=0,column=8,padx=5)

#Scroll Bar and Text editor
scroll_bar=tk.Scrollbar(main_application)      #for scroll creation
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)       #to pack scroll in Right
text_editor=tk.Text(main_application)          #text editor creation
text_editor.pack(fill=tk.BOTH,expand=True)
text_editor.focus_set()                         #making cursor on focus
text_editor.config(wrap="word",relief=tk.FLAT,yscrollcommand=scroll_bar.set)   #combining text and scroll
scroll_bar.config(command=text_editor.yview)    #combining sroll and text

#Setting font style and size
font_now="Times New Roman"
font_size_now=10

def change_font(main_application):
    global font_now
    font_now=font_family.get()
    text_editor.configure(font=(font_now,font_size_now))

def change_size(main_application):
    global font_size_now
    font_size_now=f_size.get()
    text_editor.configure(font=(font_now,font_size_now))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)

#setting Bold
#print(tk.font.Font(font=text_editor["font"]).actual())
def bold_fun():
    text_get=tk.font.Font(font=text_editor["font"])
    if text_get.actual()["weight"]=='normal':
        text_editor.configure(font=(font_now,font_size_now,"bold"))
    if text_get.actual()["weight"]=='bold':
        text_editor.configure(font=(font_now,font_size_now,"normal"))

#binding function with button
bold_btn.configure(command=bold_fun)

#setting italic
def italic_fun():
    text_get=tk.font.Font(font=text_editor["font"])
    if text_get.actual()["slant"]=='roman':
        text_editor.configure(font=(font_now,font_size_now,"italic"))
    if text_get.actual()["slant"]=='italic':
        text_editor.configure(font=(font_now,font_size_now,"roman"))
#binding
italic_btn.configure(command=italic_fun)

#setting underline
def underline_fun():
    text_get=tk.font.Font(font=text_editor["font"])
    if text_get.actual()["underline"]==0:
        text_editor.configure(font=(font_now,font_size_now,"underline"))
    if text_get.actual()["underline"]==1:
        text_editor.configure(font=(font_now,font_size_now,"normal"))
#binding
underline_btn.configure(command=underline_fun)

#font color function
def color_chooser():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
#binding
text_color_btn.configure(command=color_chooser)

#left allignment function
def allign_left():
    text_get_all=text_editor.get(1.0,"end")
    text_editor.tag_config("left",justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"left")
allign_left_btn.configure(command=allign_left)

#left allignment function
def allign_center():
    text_get_all=text_editor.get(1.0,"end")
    text_editor.tag_config("center",justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"center")
allign_center_btn.configure(command=allign_center)
#left allignment function
def allign_right():
    text_get_all=text_editor.get(1.0,"end")
    text_editor.tag_config("right",justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"right")
allign_right_btn.configure(command=allign_right)

#status Bar     word and character count
status_bar=ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)
text_change=False
def change_status(event=None):
    global text_change
    if text_editor.edit_modified():
        text_change=True
        word=len(text_editor.get(1.0,"end-1c").split())
        ch=len(text_editor.get(1.0,"end-1c").replace(" ","").replace("\n",""))
        status_bar.config(text=f"Word:{word} \t Character:{ch}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",change_status)

main_application.config(menu=main_menu)
main_application.mainloop()
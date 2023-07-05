#streamlit run web.py
#pip freeze > requirements.txt
import streamlit as st
import functions
import webbrowser

def open_link():
    webbrowser.open('https://www.mediafire.com/file/mail6xu8kgh3s6f/To-do+app.rar/file')

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo.capitalize()+ '\n')
    functions.write_todos(todos)

st.title('To-Do')
st.subheader("This app is to increase your productivity.")
st.text("Stay organized and don't forget what you have to do")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='',placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')


st.button('Download the todo-app', on_click=open_link)
st.text('by Faelzxd')

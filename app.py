import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gym Planner", layout="centered")

if "exercicios" not in st.session_state:
    st.session_state["exercicios"] = []

st.title("Gym Planner")
st.write("Welcome! Use the sidebar to manage your training program.")

st.sidebar.title("Menu")
menu = st.sidebar.radio("Go to:",[
    "View workout plan",
    "Add Exercise",
    "Edit Exercise",
    "Remove Exercise",
    "Statistics",
    "Export",
    "Import",
    "Clear Workout Plan",
    ])

def mostrar_exercicios():
    st.subheader("Current training program")
    if st.session_state.exercicios:
        df = pd.DataFrame(st.session_state.exercicios)
        st.dataframe(df, use_container_width=True)
        return True
    else:
        st.info("You haven't added any exercises.")
        return False

def adicionar_exercicio(nome, sets, reps, rest, weight):
    st.session_state.exercicios.append({
        "Exercise": nome,
        "Sets": sets,
        "Reps": reps,
        "Rest": rest,
        "Weight": weight
    })

if menu == "View workout plan":
    mostrar_exercicios()

elif menu == "Add Exercise":
    mostrar_exercicios()

    with st.form("formulario_exercicio"):
        st.subheader("Add exercise")
        nome = st.text_input("Name")
        sets = st.number_input("Sets", min_value=1, max_value=10, step=1)
        reps = st.number_input("Reps", min_value=1, max_value=100, step=1)
        rest = st.number_input("Rest (in seconds)", min_value=1, max_value=600, step=1)
        weight = st.number_input("Weight", min_value=1, max_value=500, step=1)
        enviado = st.form_submit_button("Adicionar")

        if enviado:
            if nome.strip():
                adicionar_exercicio(nome.strip(), sets, reps, rest, weight)
                st.success(f"Exercise '{nome}' added successfully.")
                st.rerun()
            else:
                st.warning("Please, enter a valid exercise name.")

elif menu == "Edit Exercise":
    st.subheader("Edit an Existing Exercise")
    st.info("Feature under development.")

elif menu == "Remove Exercise":
    if mostrar_exercicios():

        indices_para_remover = []

        st.subheader("Select one or more exercises to remove:")
        for i, ex in enumerate(st.session_state.exercicios):
            label = f"{ex['Exercise']} (Sets: {ex['Sets']}), (Reps: {ex['Reps']}), (Rest: {ex['Rest']}), (Weight: {ex['Weight']})."
            if st.checkbox(label, key=f"remove_{i}"):
                indices_para_remover.append(i)

        if indices_para_remover:
            confirm = st.checkbox("Remove selected exercise(s)?")
            if confirm:
                if st.button("Remove selected exercises"):
                    for i in sorted(indices_para_remover, reverse=True):
                        st.session_state.exercicios.pop(i)
                    st.success(f"{len(indices_para_remover)} exercise(s) removed successfully.")
                    st.rerun()
        else:
            st.info("No exercises selected.")

elif menu == "Statistics":
    st.subheader("Workout Statistics")
    st.info("Feature under development.")

elif menu == "Export":
    st.subheader("Export Workout Plan")
    st.info("Feature under development.")

elif menu == "Import":
    st.subheader("Import Workout Plan")
    st.info("Feature under development.")

elif menu == "Clear Workout Plan":
    st.subheader("Clear Workout Plan")
    if st.button("Clear Workout Plan"):
        st.session_state.exercicios.clear()
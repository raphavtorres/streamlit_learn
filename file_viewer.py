import streamlit as st
from json import loads
from pandas import read_csv


def main():
    st.markdown(
        '''
        # Exibidor de arquivos
        
        ## Suba um arquivo para vermos o que acontece 🐱‍🚀🐱‍💻
        ''')
    file = st.file_uploader('Suba aqui o seu arquivo!', type=['jpg', 'png', 'py', 'wav', 'csv', 'json', 'mp4'])

    st.text_input("Email", max_chars=20)
    st.text_input("Senha", type='password')

    if file:
        print(file.type)
        match file.type.split('/'):
            case 'application', 'json':
                st.json(loads(file.read()))
            case 'image', _:
                st.image(file)
            case 'text', 'csv':
                df = read_csv(file)
                # df = read_csv(file).transpose()
                st.dataframe(df)
                st.line_chart(df)
            case 'text', 'x-python':
                st.code(file.read().decode())
            case 'audio', _:
                st.audio(file)
            case 'video', _:
                st.video(file)
    else:
        st.error("Ainda não tenho arquivo")

if __name__ == "__main__":
    main()

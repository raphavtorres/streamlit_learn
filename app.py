import streamlit as st


def main():
    st.title("1º Title")

    st.markdown(
        '''
        # 2º Title but with markdown
        
        **bold**, *Italic*

        ## Subtitle
        ''')
    st.write("Message with write")
    st.image('https://via.placeholder.com/500x450')

if __name__ == "__main__":
    main()

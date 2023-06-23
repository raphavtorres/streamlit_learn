import streamlit as st
from PIL import Image, ImageFont, ImageDraw

def text_on_image(image, text, font_size, color):
    img = Image.open(image)
    font = ImageFont.truetype('arial.ttf', font_size)
    draw = ImageDraw.Draw(img)

    # image and font width and heigth
    iw, ih = img.size
    fw, fh = font.getsize(text)

    draw.text(
       ( (iw - fw) / 2, (ih - fh) / 2),
        text,
        fill=color,
        font=font
    )

    img.save("last_img.jpg")


def main():
    image = st.file_uploader("Uma imagem", type=['jpg', 'png'])
    text = st.text_input("Sua marca d'água")
    # color = st.selectbox(
    #     'Cor da sua marca', ['black', 'white', 'red', 'green']
    # )
    color = st.color_picker("Escolha sua cor")
    font_size = st.number_input("Tamanho da fonte", min_value=50)

    if image:
        result = st.button("Aplicar", type='primary', on_click=text_on_image, args=(image, text, font_size, color))
        if result:
            st.image('last_img.jpg')
            with open('last_img.jpg', 'rb') as file:
                st.download_button(
                    "Baixe sua imagem com marca",
                    file_name="imagem_dowload.jpg",
                    data=file,
                    mime='image/jpg'
                )
    else:
        st.warning("Ainda não temos imagem...")


if __name__ == "__main__":
    main()
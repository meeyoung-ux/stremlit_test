import streamlit as st
from PIL import Image

# st.title("안녕하세요!")
# st.header("오미영")

# 사이드바 화면
st.sidebar.header("로그인")
user_id = st.sidebar.text_input("아이디 입력",value='',max_chars=15)
user_password = st.sidebar.text_input("패스워드 입력",value="",type='password')


if user_id == "kosinme" and user_password == '1234':

    st.sidebar.header("그림 목록")
    sel_options=["",'진주 귀걸이를 한 소녀','별이 빛나는 밤','생명의 나무','월하정인']
    user_opt = st.sidebar.selectbox("좋아하는 작품은?",sel_options,index=0)
    st.sidebar.write("**선택한 그림은?",user_opt)


    # 메인 화면
    st.subheader("메인 화면")
    image_files=['welcom.png','Vermeer.png','Gogh.png','Munch.png','Klimt.jpg','ShinYoonbok.png']
    sel_index =  sel_options.index(user_opt)
    img_file = image_files[sel_index]
    img_local = Image.open(f"{img_file}")
    st.image(img_local,caption=user_opt)



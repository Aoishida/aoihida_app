#ホテルホームページ

import streamlit as st
import datetime
from PIL import Image

#テキスト関連
st.title('アプリ')
st.caption('これはテストアプリです')
st.subheader('紹介')
st.text('python')

# code = '''
# import streamlit as st

# st.title('アプリ')
# '''
# st.code(code, language='python')

#画像
image = Image.open('download.png')
st.image(image, width = 200)

with st.form(key='profile_from'):


    #テキスト
    name = st.text_input('名前')
    adress = st.text_input('住所')
    # print(name)

    #ラジオボタン
    age_category = st.radio(
        '年齢層',
        ('子ども(18歳未満)','小学生以下','中学生以上' , '大人(18歳以上)')
    )

    #複数選択
    hobby = st.multiselect(
        '趣味',
        ('スポーツ', '読書', '音楽', 'プログラミング', 'アニメ・映画鑑賞', '釣り', '料理')
    )

    #日付
    start_date = st.date_input(
        '開始日',
        datetime.date(2022, 7, 14)
    )

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    
    if submit_btn:
        st.text(f'ようこそ!{name}さん {adress}に書類を送りました！')
        st.text(f'年齢層: {age_category}')
        st.text(f'趣味: {",".join(hobby)}')
    # print(f'submit_btn: {submit_btn}')
    # print(f'cancel_btn: {cancel_btn}')




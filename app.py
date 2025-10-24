import streamlit as st
import random

# 제목
st.title("🍽️ 랜덤 메뉴 추천기")

# 메뉴 리스트
menu_list = [
    "김치찌개", "된장찌개", "불고기", "비빔밥", "떡볶이",
    "라면", "치킨", "피자", "햄버거", "샌드위치",
    "스파게티", "짜장면", "짬뽕", "초밥", "샐러드"
]

st.write("오늘 뭐 먹을지 고민되나요? 버튼을 눌러 랜덤 메뉴를 추천받아보세요!")

# 버튼 클릭 시 메뉴 추천
if st.button("추천받기"):
    selected_menu = random.choice(menu_list)
    st.success(f"오늘의 메뉴는: {selected_menu} 🍽️")

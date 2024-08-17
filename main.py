#from dotenv import load_dotenv
#load_dotenv() #env 파일 활용을 위함(open ai key 사용)

# from langchain.llms import OpenAI

#complete < llm 
#일반적인 open ai model
# llm = OpenAI()
# # result = llm.predict("hi!")

# result = llm.predict("내가 좋아하는 동물은? ") #저는 고양이를 좋아합니다.

# print(result) #good morning! how are you today 

#chat mode : 챗봇과 채팅하는 형태로 씀
from langchain.chat_models import ChatOpenAI
#웹사이트 만들기 streamlit사용하여
import streamlit as st

chat_model = ChatOpenAI()

st.title("인공지능 시인: Connected Spear")

content = st.text_input("시의 주제를 제시해주세요! ")


st.write("시의 주제 : ", content)

if st.button("시적 영감이 떠오른다...!"): 
    with st.spinner("온다..온다...시가온다..!"):
        result2 = chat_model.predict(content + "에 대한 시를 써줘") #Hello! How can I assist you today? : 질문형
        st.write(result2)


#인공지능 시인 만들기 !


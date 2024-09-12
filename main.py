import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# OpenAI API 키 설정
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

# LLM 모델 초기화
llm = OpenAI(temperature=0.7)

# 프롬프트 템플릿 정의
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="다음 질문에 답변해주세요: {question}"
)

# LLMChain 생성
chain = LLMChain(llm=llm, prompt=prompt_template)

# 사용자 입력 받기
user_question = input("질문을 입력하세요: ")

# 응답 생성
response = chain.run(user_question)

print(f"답변: {response}")
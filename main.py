from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ipa_converter import ipa_converter
from translater import convert_to_kor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transliterate")
def transliterate(word: str, language: str):
    # 1단계: 단어 → IPA
    ipa = ipa_converter(word, language)
    # 2단계: IPA → 한글
    result = convert_to_kor(ipa, language)
    return {"result": result}
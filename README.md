# Free-Honor
Free-Honor project
<br>
<br>
<br>

*중복되어 사용된 Used Library는 작성하지 않음*

<br>
<br>

## [Data Collecting](https://github.com/datacampus-team2/project/tree/master/data_collecting)
Code | Explanation | Used Library
-----|------|---------------
[00_check_one_page_two_files](https://github.com/datacampus-team2/project/blob/master/data_collecting/00_check_one_page_two_files.ipynb) | 한 게시판에 두 개의 파일이 존재하는 경우 분석 | os <br>re <br>pandas <br>requests <br>BeautifulSoup
[01_pgm_crawling](https://github.com/datacampus-team2/project/blob/master/data_collecting/01_pgm_crawling.ipynb) | 대법원 사이트에서 공개된 판결문 크롤링 | time <br>pathvalidate
[02_pdf2xlsx](https://github.com/datacampus-team2/project/blob/master/data_collecting/02_pdf2xlsx.ipynb) | 텍스트 혹은 이미지로 구성된 판결문 PDF를 텍스트로 전환 | fitz <br>sys <br> pdftotext <br>glob <br>PIL <br>PyPDF2 <br>pdf2image <br>pathos <br>cv2 <br>pytesseract
[03_columnize](https://github.com/datacampus-team2/project/blob/master/data_collecting/03_columnize.ipynb) | 텍스트 대분류 | 
[04_condition_crawling](https://github.com/datacampus-team2/project/blob/master/data_collecting/04_condition_crawling.ipynb) | 대법원 사이트의 양형기준 정보 크롤링 | 

<br>
<br>

## [Data Processing](https://github.com/datacampus-team2/project/tree/master/data_processing)
Code | Explanation | Used Library
-----|------|---------------
[01_columnize](https://github.com/datacampus-team2/project/blob/master/data_processing/01_columnize.ipynb) | 텍스트 소분류 | 
[02_spell_space](https://github.com/datacampus-team2/project/blob/master/data_processing/02_spell_space.ipynb) | 띄어쓰기 교정 | soyspacing
[03_extract_law](https://github.com/datacampus-team2/project/blob/master/data_processing/03_extract_law.ipynb) | 법 정보 추출 | openpyxl
[04_arrange](https://github.com/datacampus-team2/project/blob/master/data_processing/04_arrange.ipynb) | 징역, 집행유예, 벌금, 항소 정보 추출 |
[05_clean_text](https://github.com/datacampus-team2/project/blob/master/data_processing/05_clean_text.ipynb) | 불용어 제거, 자주 언급되어 변별력 없는 단어 제거, 명사만 남김 | eunjeon 
[06_tf_idf](https://github.com/datacampus-team2/project/blob/master/data_processing/06_tf_idf.ipynb) | tf-idf를 활용해 판결문 요약 | sklearn <br>collections <br>nltk <br>ast
[07_0_w2v](https://github.com/datacampus-team2/project/blob/master/data_processing/07_0_w2v.ipynb) | 임베딩을 위한 Word2Vec 모델 생성 | logging <br>konlpy <br>gensim <br>pathlib
[07_1_fasttext](https://github.com/datacampus-team2/project/blob/master/data_processing/07_1_fasttext.ipynb) | 임베딩을 위한 FastText 모델 생성 | 
[08_d2v](https://github.com/datacampus-team2/project/blob/master/data_processing/08_d2v.ipynb) | 비슷한 판결문 제공을 위한 Doc2Vec 모델 생성 | 
[09_case_law](https://github.com/datacampus-team2/project/blob/master/data_processing/09_case_law.ipynb) | 추출한 사건명, 법명으로 bag of words 생성 | difflib 
[10_eda](https://github.com/pre-honor/pre-honor/blob/master/data_processing/us_probation.ipynb) | 데이터 분포 분석 | matplotlib <br>seaborn <br>numpy <br>datetime <br>wordcloud

<br>
<br>

## [Data Modelling](https://github.com/datacampus-team2/project/tree/master/data_modeling)
Code | Explanation | Used Library
-----|------|---------------
[01_0_sentence](https://github.com/datacampus-team2/project/blob/master/data_modeling/01_0_sentence.ipynb) | 징역 예측 모델 생성 | tensorflow <br>random <br>sys
[02_0_probation](https://github.com/datacampus-team2/project/blob/master/data_modeling/02_0_probation.ipynb) | 집행유예 예측 모델 생성 |
[03_0_appeal](https://github.com/datacampus-team2/project/blob/master/data_modeling/03_0_appeal.ipynb) | 항소 예측 모델 생성 |
[04_0_fine](https://github.com/datacampus-team2/project/blob/master/data_modeling/04_0_fine.ipynb) | 벌금 예측 모델 생성 |

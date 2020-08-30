import pandas as pd
import os
import gensim.models

def find_similar_pgm(input_list):
    df_name = os.path.join(os.path.dirname(os.getcwd()), 'xlsx_data', 'xlsx_#7_dropped.xlsx')
    df = pd.read_excel(df_name)
    model = gensim.models.Doc2Vec.load('d2v_0825.model')
    tokens = input_list.split()
    new_vector = model.infer_vector(tokens)
    sims = model.docvecs.most_similar([new_vector])
    sims = [s[0].replace('CID_', '') for s in sims]
    url = [df[df['cid'] == s]['url'].to_string(index=False) for s in sims]
    title = [df[df['cid'] == s]['title'].to_string(index=False) for s in sims]
    return url, title

import pandas as pd
def extract_node(state):
    df2 = pd.read_excel(state['file_path_v2'])
    data_to_verify = df2.to_dict('records')
    return {"diff_data": data_to_verify}
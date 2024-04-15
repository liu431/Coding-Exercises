import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame({'student_id': [i[0] for i in student_data],
                        'age': [i[1] for i in student_data]})
    return df

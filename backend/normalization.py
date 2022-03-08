from segmentation import Segmentation
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def Normalization(dataFrame):
    
    data_frame = dataFrame.drop(['classe','imagem'], axis=1)
    print(dataFrame)
    dados_normalizados = MinMaxScaler().fit(data_frame)
    normalizados = dados_normalizados.transform(data_frame)
    df_normalizado = pd.DataFrame(normalizados)
    df_normalizado.columns = ['Area','Perimetro','m00','m10','m01','m20','m11','m02','m30','m21','m12','m03','mu20','mu11','mu02','mu30','mu21','mu12','mu03','nu20','nu11','nu02','nu30','nu21','nu12','nu03','cx','cy','B','G','R','H','S','V','L','A','D','LBP','I1','I2','I3','b','g','r','h','s','v','l','a','d','lbp','i1','i2','i3']
    #df_normalizado["classe"] = dataFrame["classe"]
    #df_normalizado["imagem"] = dataFrame["imagem"]
    
    return df_normalizado   


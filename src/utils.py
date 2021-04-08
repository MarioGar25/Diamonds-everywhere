import zipfile
import pandas as pd
def unzip_zip(zip, csv):
    '''
    Unzip .zip file, obtains a .csv file from the .zip, and returns like DataFrame

    Input: str (.zip file), str (.csv file)
    Return: Dataframe from .csv file in .zip file

    '''

    #unzip the file
    zf = zipfile.ZipFile(zip)
    #read csv and read like a pandas DataFrame
    df = pd.read_csv(zf.open(csv))
    #close zipfile
    zf.close()
    #returns DataFrame
    return df



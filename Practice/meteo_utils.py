import pandas as pd
import glob
import re

def read_weaclim_html (path):
    
    file = open(path, 'r', encoding="utf-8")
    
    while True:
        line = file.readline()
        
        if '<meta name="description" content="' in line:
            break
        
        if not line:
            break
            
    file.close()
            
    year_str = re.search('за (.*) года', line).group(1).split()[1]
    
    df0 = pd.read_html(path)[0]     
    df1 = pd.read_html(path)[1]

    heads = df1.loc[0,:]
    df1 = df1.loc[1:,:]
    df1.columns = heads

    df0 = df0.loc[1:,:]
    time_str = df0.loc[:,1] + '.' + year_str + ' ' + df0.loc[:,0]
    time = pd.to_datetime (time_str, format = "%d.%m.%Y %H")
    
    df1['UTC time'] = time
    df1 = df1.set_index('UTC time')
    
    return df1

def read_weaclim_dir (path):
    if '.html' not in path:
        path += '*.html'
        
    df = pd.DataFrame()    
    files = glob.glob (path)
        
    for i_file, file in enumerate (files):
        print ('reading %s'%file)
        df_new = read_weaclim_html (file)
        df = df.append(df_new) 
    return df

def read_rp5 (path):
    df = pd.read_excel (path, skiprows=6)  
    
    df['local time'] = pd.to_datetime (df[df.columns[0]], format = "%d.%m.%Y %H:%M")
    
    df = df.set_index ('local time')
    return df


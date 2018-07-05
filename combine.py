import pandas as pd
import sys, os, shutil

# TOUCH FILE
if not os.path.exists('./cascade'):
   os.mkdir('./cascade/')

if len(sys.argv) < 2:
    print('you need to put second argument!')
else:
    output = sys.argv[1]
    if not os.path.exists('./tmp'):
        print('nothing to combine!')
    else:
        allFiles = os.popen('ls ./tmp/').readlines()
        print(allFiles)
        frame = pd.DataFrame()
        list_ = []
        colnames = ['a', 'b', 'c', 'd']
        for file_ in allFiles:
            df = pd.read_csv('./tmp/' + file_.replace('\n',''),index_col=None, header=0)
            # df = df.apply(lambda x: x.sort_values().values)
            list_.append(df)
        frame = pd.concat(list_, axis=0)
        frame.columns = colnames
        frame.to_csv("./cascade/" + output.replace('.csv','') + ".csv", index=None)
        print('success!')
        shutil.rmtree('./tmp/', ignore_errors=False, onerror=None)

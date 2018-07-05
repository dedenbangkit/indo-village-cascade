import pandas as pd
import csv
import sys
import os

argument = [sys.argv[1].lower(), sys.argv[2].lower()]
sources = './storage/'

# DEFINE LVL 1
# Indonesia: Provinsi / Province

lvl1 = pd.read_csv(sources + 'provinces.csv', names=['code', 'name'])
lvl1 = lvl1.loc[lvl1['name'] == argument[0].upper()]
lvl1_id = lvl1.iloc[0]['code']

# DEFINE LVL 2
# Indonesia: Kabupaten / Regency

lvl2 = pd.read_csv(sources + 'regencies.csv', names=['code', 'parent', 'name'])
lvl2 = lvl2.loc[lvl2['name'] == argument[1].upper()]
lvl2_id = lvl2.iloc[0]['code']

# GET LVL 3 & 4
# Indonesia: Kecamatan / Subdistricts
# Indonesia: Desa / Village

lvl3 = pd.read_csv(sources + 'subdistricts.csv', names=['code', 'parent', 'name'])
lvl4 = pd.read_csv(sources + 'villages.csv', names=['code', 'parent', 'name'])
lvl3 = lvl3.loc[lvl3['parent'] == lvl2_id]

# TOUCH FILE
if not os.path.exists('./tmp'):
   os.mkdir('./tmp/')

csvfile = './tmp/' + argument[0].replace(' ','_') + '-' + argument[1].replace(' ','_').replace('kota','kaa.') + '.csv'
open(csvfile, 'a').close()

def test():
    with open(csvfile, 'w', newline='') as csvs:
        fieldname = ['Province','Region','Subdistrict', 'Village']
        wr = csv.DictWriter(csvs, fieldnames = fieldname, delimiter = ',')
        wr.writeheader()
        for lv3, level3 in lvl3.iterrows():
            parent = level3['code']
            childs = lvl4.loc[lvl4['parent'] == parent]
            for lv4, child in childs.iterrows():
                lv3_name = level3['name'].lower().title()
                is_kota = argument[1].title().split(' ')
                if is_kota == 'Kota ':
                    administ = 'Kelurahan '
                else:
                    administ = 'Desa '
                lv4_name = child['name'].lower().title()
                wr.writerow({'Province':argument[0].title(),'Region': argument[1].title(),'Subdistrict':lv3_name, 'Village': administ + lv4_name})
                print("%s, %s, %s, %s\n"%(argument[0].title(), argument[1].title(), lv3_name, administ + lv4_name))

test()

#import ipdb; ipdb.set_trace()

# -*- coding: utf-8 -*-
'''
Created on 2018/02/25

@author: unyaunya
'''

import os
import urllib.request
import zipfile

class KabukaDataSouko(object):
    '''
    「株価データ倉庫」からのデータ取得処理
    '''
    def __init__(self, datafolder):
        self.name = '株価データ倉庫'
        self.root_url='http://www.geocities.co.jp/WallStreet-Stock/9256/'
        self.datafolder = datafolder
    
    def get_n225_data(self, year):
        '''
        日経平均先物の日足データを取得する。
        '''
        base_name = "n225-%d" % year
        zip_name = base_name + ".zip"
        csv_name = base_name + ".csv"
        target_url = "%s/%s" % (self.root_url, zip_name)
        download_folder = os.path.join(self.datafolder, 'download', 'n225')
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        download_file = os.path.join(download_folder, zip_name)
        csv_file = os.path.join(download_folder, csv_name)
        if os.path.exists(csv_file):
            print("%s already exists." % csv_name)
        else:
            if os.path.exists(download_file):
                print("%s already exists." % zip_name)
            else:
                urllib.request.urlretrieve(target_url, download_file)
            with zipfile.ZipFile(download_file,'r') as inputFile:
                inputFile.extractall(path=download_folder)
                
                

#import pdb; pdb.set_trace();

if __name__ == '__main__':
    folder = os.path.join(os.path.dirname(__file__), "..", "..", "data")
    site = KabukaDataSouko(folder)
    for year in range(1996, 2018):
        print("Downloading %s's data" % year)
        site.get_n225_data(year)
        
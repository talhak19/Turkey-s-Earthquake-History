import pandas as pd


def pre_process(data):
        data.df = data.df.drop(['No', 'Deprem Kodu', 'Tip',"Mw"], axis=1)


        data.df['Olus zamani'] = data.df['Olus zamani'].str.split('.').str[0]

        # Saniye is greater than 60 for some data points. I located and dropped them
        for i in range(0, len(data.df)):
            if float(data.df['Olus zamani'][i][6:]) >= 60:
                data.df = data.df.drop(i)
        data.df = data.df.reset_index(drop=True)


        #Tarihi tek bir sütuna indirgemek
        tarih_tek_sutun = pd.to_datetime(data.df['Olus tarihi'] + ' ' + data.df['Olus zamani'])
        data.df['Olus zamani'] = tarih_tek_sutun
        data.df.drop(['Olus tarihi'], axis=1, inplace=True)

        Yer = []
        for y in range(len(data.df)):
            Yer.append("")

        # Yer dizimize 'Yer' sütunundaki değerleri ekliyoruz.
        for i in range(0, len(data.df)):
            Yer[i] = data.df['Yer'][i]

            # Eğer ( var ise tekrardan soldan ve sağdan "("  - ")" ile böleriz.
            if Yer[i].find("(") != -1:
                Yer[i] = Yer[i].split('(')[1]
                Yer[i] = Yer[i].split(')')[0]
        Yer = pd.DataFrame(Yer)
        #[ ile başlatmak için
        Yer = Yer[0].str.split('[').str[0].to_frame()
        Yer.columns = ['Yer']
        data.df['Yer'] = Yer
        #Türkçe karakterlerden dolayı daha düzgün veri seti işlemek için, ing karakterlerle tekrar adlandırılan Yer sütunu
        Yer_update = {"?ORUM": "CORUM", "K?TAHYA": "KUTAHYA", "EGE DENiZi": "EGE DENIZI",
              "DiYARBAKIR": "DIYARBAKIR", "T?RKiYE-iRAN SINIR B?LGESi": "TURKIYE-IRAN SINIR BOLGESI",
              "BALIKESiR ": "BALIKESIR", "SiVAS": "SIVAS", "iZMiR": "IZMIR", "TUNCELi": "TUNCELI",
              "SURiYE": "SURIYE", "ESKiSEHiR": "ESKISEHIR", "DENiZLi": "DENIZLI", "BiTLiS": "BITLIS",
              "KiLiS": "KILIS", "VAN G?L?": "VAN GOLU", "?ANKIRI": "CANKIRI",
              "T?RKIYE-IRAN SINIR B?LGESI": "TURKIYE-IRAN SINIR BOLGESI", "MANiSA": "MANISA",
              "AKDENiZ": "AKDENIZ", "G?RCiSTAN": "GURCISTAN", "BiNGOL": "BINGOL", "OSMANiYE": "OSMANIYE",
              "KIRSEHiR": "KIRSEHIR", "MARMARA DENiZi": "MARMARA DENIZI", "ERZiNCAN": "ERZINCAN",
              "BALIKESiR": "BALIKESIR", "GAZiANTEP": "GAZIANTEP", "G?RCISTAN": "GURCISTAN",
              "?ANAKKALE'": "CANAKKALE", "HAKKARi": "HAKKARI", "AFYONKARAHiSAR": "AFYONKARAHISAR",
              "BiLECiK": "BILECIK", "KAYSERi": "KAYSERI", "T?RKiYE-IRAK SINIR B?LGESi": "TURKIYE-IRAK SINIR BOLGESI",
              "KARADENiZ": "KARADENIZ", "T?RKIYE-IRAK SINIR B?LGESI": "TURKIYE-IRAK SINIR BOLGESI",
              "KARAB?K": "KARABUK", "KIBRIS-SADRAZAMK?Y?K": "KIBRIS-SADRAZAMKOY",
              "T?RKIYE-SURIYE SINIR B?LGESI?K": "TURKIYE-SURIYE SINIR BOLGESI", "?ANAKKALE": "CANAKKALE",
              "KIBRIS-SADRAZAMK?Y": "KIBRIS-SADRAZAMKOY", "ERZURUM ": "ERZURUM",
              "T?RKIYE-SURIYE SINIR B?LGESI": "TURKIYE-SURIYE SINIR BOLGESI", "ADANA ": "ADANA", "KUS G?L?": "KUS GOLU",
              "BURDUR ": "BURDUR", "KIBRIS-G?ZELYURT": "KIBRIS-GUZELYURT", "KONYA ": "KONYA",
              "KOCAELI ": "KOCAELI", "AMASYA ": "AMASYA", "KIRSEHIR ": "KIRSEHIR",
              "KIBRIS-KILI?ASLAN": "KIBRIS-KILICASLAN", "KIBRIS-Z?MR?TK?Y": "KIBRIS-ZUMRUTKOY",
              "DENIZLI ": "DENIZLI", "MANISA ": "MANISA", "ULUBAT G?L?": "ULUBAT GOLU",
              "T?RKIYE-ERMENISTAN SINIR B?LGESI": "TURKIYE-ERMENISTAN SINIR BOLGESI",
              "ERZINCAN ": "ERZINCAN", "TOKAT ": "TOKAT", "ARDAHAN ": "ARDAHAN"}
        data.df['Yer'] = data.df['Yer'].replace(Yer_update)
        return data.df


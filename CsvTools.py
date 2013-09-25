"""
ＣＳＶファイルツール
書き込んだり読み込んだり
"""
import csv
import codecs
class CsvTools(csv.excel):
    """
    読み込みパラメータとか
    quoting
    csv.QUOTE_MINIMAL csv.QUOTE_ALL csv.QUOTE_NONNUMERIC
    """
#   quoting   = csv.QUOTE_ALL
#   delimiter = "\t"
    """
    書き込み
    rows 書き込む内容二次配列[(ver,ver),(ver,ver)]
    file 書き込むファイル名:string
    """
    @classmethod
    def writer(cls,rows,file):
        with open(file ,"w", newline='') as csvfile:
            writer = csv.writer(csvfile,CsvTools())
            writer.writerows(rows)
    #-----------------------------------------------
    """
    CSVを読み込んでCSVオブジェクトで返す
    file 読み込むファイル名:string
    return 読み込まれたデータのリスト
    """
    @classmethod
    def Reader(cls,file):
        with open(file,newline='') as csvfile:
            RtRows = list(csv.reader(csvfile,CsvTools()))[:]
        return RtRows
#-------------------------------------------------------

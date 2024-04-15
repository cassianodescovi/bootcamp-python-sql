import pandas as pd


class CsvProcessor(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
    
    def load_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filter_by(self, column, attribute):
        return self.df.query(f"{column} == '{attribute}'")
        

if __name__ == '__main__':
    file_csv = "data/data.csv"
    filter = 'state'
    limit = 'SP'

    file_CSV = CsvProcessor(file_csv)
    file_CSV.load_csv()
    print(file_CSV.filter_by(filter, limit))
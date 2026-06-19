class CSVExporter:

    def export(self, df):
        return df.to_csv(
            index=False
        ).encode("utf-8")
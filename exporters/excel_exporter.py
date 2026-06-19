from io import BytesIO


class ExcelExporter:

    def export(self, df):
        buffer = BytesIO()

        df.to_excel(
            buffer,
            index=False,
            engine="openpyxl"
        )

        return buffer.getvalue()
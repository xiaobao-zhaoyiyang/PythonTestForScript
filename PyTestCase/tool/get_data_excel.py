import xlrd
import data.title_in_json

class excel():

    def read_excel(table, title):

        #获取合并的单元格


        #表格行列数
        ncols = table.ncols
        nrown = table.nrows

        #创建一个空列表，存储Excel的数据
        tables = []

        for rown in range(nrown - 1):
            rown+=1
            # print('...............')
            array = {}
            for clon in range(ncols):
                value_title = (title[clon])
                value_excel = table.cell_value(rown, clon)
                ctype = table.cell(rown, clon).ctype
                #读取到number类型的数据，且含有小数，将小数去掉。秒杀价和原始价格除外
                if value_title != 'price' and value_title != 'original_price':
                    if ctype == 2 and value_excel % 1 == 0.0:
                        value_excel = str(int(value_excel))
                array[value_title] = value_excel
                #print(array)

            tables.append(array)
        # print(tables)
        # print(len(tables))
        return tables
        # return array

    def open_excel(filePath, sheetId):
        # 打开文件
        workbook = xlrd.open_workbook(filePath)
        # 获取所有sheet
        print(workbook.sheet_names())
        # 获取获取数据的sheet
        sheet_name = workbook.sheet_names()[sheetId]
        # print(sheet_name)
        # 根据sheet索引或是名称获取sheet内容
        table = workbook.sheet_by_name(sheet_name)
        # sheet的名称，行数，列数
        # name = table.name
        # rowNum = table.nrows
        # cloNum = table.ncols
        # 获取单元格内容的三种方法
        # print(table.cell(0, 3).value)
        # print(table.cell_value(1, 4))
        # print(table.row(1)[4].value)
        # 获取单元格的数据类型 0 empty 1 string 2 number 3 date 4 boolean 5 error
        # print(table.cell(1, 4).ctype)
        return table

    def read_title_from_excel(table):
        title = []
        # 将Excel表格内容导入到tables列表中
        for clon in range(table.ncols):
            value = data.title_in_json.search[table.cell_value(0, clon)]
            title.insert(clon, value)
        # print(title)
        return title

    def merge_cell(sheet_info):
        merge = {}
        merge_cells = sheet_info.merged_cells
        for (rlow, rhigh, clow, chigh) in merge_cells:
            value_mg_cell = sheet_info.cell_value(rlow, clow)
            if rhigh - rlow == 1:
                # Merge transverse cells
                for n in range(chigh - clow - 1):
                    merge[(rlow, clow + n + 1)] = value_mg_cell
            elif chigh - clow == 1:
                # Merge Vertical Cells
                for n in range(rhigh - rlow - 1):
                    merge[(rlow + n + 1, clow)] = value_mg_cell
        return merge

# if __name__ == '__main__':
#     read_excel('/Users/zhaoqiang/Documents/MyFiles/上架课程.xlsx', 0)
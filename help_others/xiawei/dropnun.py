import pandas as pd
import numpy as np
from tqdm import tqdm


def add_rows(original_excel, standard_excel):
    output_excel = pd.Series()
    for i in tqdm(range(len(standard_excel))):
        for j in range(len(original_excel)):
            if standard_excel.iloc[i][0] == original_excel.iloc[j][0]:
                rows = original_excel.iloc[j][:]
                output_excel = pd.concat([output_excel, rows])
                # print(output_excel)
            else:
                new_rows = pd.DataFrame(
                    [[standard_excel.iloc[i][0], 0, 0, 0, 0, 0]])
                output_excel = pd.concat([output_excel, new_rows])
                # while (original_excel.iloc[j][0] != standard_excel.iloc[i][0]):
                #     j = j + 1
                #     if original_excel.iloc[j][0] == standard_excel.iloc[i][0]:
                #         new_row = pd.DataFrame(
                #             [original_excel.iloc[j][0], original_excel.iloc[j][1:]])
                #         output_excel.append(new_row, ignore_index=True)
                #         break
    return output_excel


def main():
    data = pd.read_excel(r'D:\\piles\\20220617.xlsx')
    data1 = pd.read_excel(r'D:\\piles\\timetamp.xlsx')
    print(data1.shape)
    data_add_row = add_rows(data, data1)
    print(data_add_row.shape)


if __name__ == '__main__':
    main()

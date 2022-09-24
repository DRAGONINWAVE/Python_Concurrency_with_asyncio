import pandas as pd
import numpy as np
from tqdm import tqdm


def add_rows(original_excel, standard_excel):
    output_excel = pd.DataFrame()
    for i in tqdm(range(len(standard_excel))):
        for j in range(len(original_excel)):
            # print(standard_excel.iloc[[i]])
            if standard_excel.iloc[[i]]['time2'].values == original_excel.iloc[[j]]['time'].values:
                rows = original_excel.iloc[[j]]
                # print(rows)
                output_excel = pd.concat(
                    [output_excel, rows], ignore_index=True)
                # print(output_excel)
                break
            else:
                k = j
                while (k < len(original_excel)):
                    k = k + 1
                    if standard_excel.iloc[[i]]['time2'].values == original_excel.iloc[[k-1]]['time'].values:
                        rows = original_excel.iloc[[k-1]]
                        output_excel = pd.concat(
                            [output_excel, rows], ignore_index=True)
                        break
                    if k == len(original_excel):
                        new_rows = pd.DataFrame(
                            [[standard_excel.iloc[[i]]['time2'].values.astype(str)[0], 0, 0, 0, 0, 0]], columns=['time', 'a', 'b', 'c', 'd', 'e'])
                        output_excel = pd.concat(
                            [output_excel, new_rows], ignore_index=True)
                        break
                break
    return output_excel


def main():
    data = pd.read_excel(r'D:\\piles\\20220617.xlsx')
    data1 = pd.read_excel(r'D:\\piles\\timetamp.xlsx')
    print(data1.iloc[[0]]['time2'].values.astype(str)[0])
    print(list(data.iloc[[0]]['time']))
    print(data.iloc[[0]])
    print((data.iloc[[0]]['time'] == data1.iloc[[0]]['time2']))
    data_add_row = add_rows(data, data1)
    print(data_add_row.shape)
    data_add_row.to_excel('a.xlsx', index=False, header=False)


if __name__ == '__main__':
    main()

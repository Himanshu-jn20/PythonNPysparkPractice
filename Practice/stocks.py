with open("C:\\Users\\lenovo\\Desktop\\Files\\stocks.csv",'r') as f_i:
    f_i=f_i.readlines()[1:]
    with open('C:\\Users\\lenovo\\Desktop\\Files\\stocks_2.csv', 'w') as f_o:
        f_o.write('Company Name\tPE Ratio\tPB Ratio\n')
    for line in f_i:
        line_lst=line.split('\t')
        pe=round(int(line_lst[1])/int(line_lst[2]),2)
        pb=round(int(line_lst[1])/int(line_lst[3]),2)
        with open("C:\\Users\\lenovo\\Desktop\\Files\\stocks_2.csv",'a') as f_o:
            f_o.write(line_lst[0]+'\t'+str(pe)+'\t'+str(pb)+'\n')
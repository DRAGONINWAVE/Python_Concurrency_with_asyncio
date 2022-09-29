clear
clc
[a,R]=geotiffread('D:\piles\SPEI-1\SPEI-1\SPEI1.tif');%先导入投影信息，某个影像的路径就行（最好是你分析的数据中的一个）
info=geotiffinfo('D:\piles\SPEI-1\SPEI-1\SPEI1.tif');%同上
[m,n]=size(a);
SPEIsum=zeros(m*n,360);
for year=1:360
    filename=strcat('G:\data_paper\new_anusplin\SPEI\SPEI-1\','SPEI',int2str(year),'.tif');%此处要修改，我这里是八年的每年年均植被覆盖度的数据，注意你的文件名字。
    data=importdata(filename);
    data=reshape(data,m*n,1);
    SPEIsum(:,year-0)=data;
end

SEDIsum=zeros(m*n,360);
for year=1:360
    filename=strcat('G:\data_paper\new_anusplin\SEDI\SEDI-1\','SEDI',int2str(year),'.tif');%此处要修改，我这里是八年的每年年均地表温度的数据，注意你的文件名字。
    data=importdata(filename);
    data=reshape(data,m*n,1);
    SEDIsum(:,year-0)=data;
end
%SPI_SPEI_xgx=zeros(m,n);
%SPI_SPEI_p=zeros(m,n);
%SPEIsum1=num2cell(SPEIsum);
%SEDIsum1=num2cell(SEDIsum);
t21=zeros(m,n);
t12=zeros(m,n);

     

for i=1:length(SPEIsum)
  % SPI=SPIsum(i,:);   
 % SPEI=SPEIsum(i,:);
    x1=SPEIsum(i,:);
    x2=SEDIsum(i,:);
    %R [r2,p2]=corrcoef(SPI,SPEI);%corrcoef(x,y)表示序列x和序列y的相关系数，得到的是2*2的矩阵
     x1=x1(1:360);
     x2=x2(1:360);
     [T21, err90_21, err95_21, err99_21] = causality_est(x1, x2, 1);
     [T12, err90_12, err95_12, err99_12] = causality_est(x2, x1, 1);
     t21(i)=T21;
     t12(i)=T12;
  %  SPI_SPEI_xgx(i)=r2(2);
  %  SPI_SPEI_p(i)=p2(2);
end


%geotiffwrite('G:\liang\cor\cor.tif',SPI_SPEI_xgx,R,'GeoKeyDirectoryTag',info.GeoTIFFTags.GeoKeyDirectoryTag);
%geotiffwrite('G:\liang\cor\p.tif',SPI_SPEI_p,R,'GeoKeyDirectoryTag',info.GeoTIFFTags.GeoKeyDirectoryTag);
geotiffwrite('G:\liang\cor\SPEI_SEDI.tif',abs(t12),R,'GeoKeyDirectoryTag',info.GeoTIFFTags.GeoKeyDirectoryTag);
geotiffwrite('G:\liang\cor\SEDI_SPEI.tif',abs(t21),R,'GeoKeyDirectoryTag',info.GeoTIFFTags.GeoKeyDirectoryTag);




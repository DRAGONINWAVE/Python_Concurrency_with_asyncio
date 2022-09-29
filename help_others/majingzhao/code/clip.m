clear
clc
%% clip
% [a,R]=geotiffread('D:\data\LAIresult\clip\result\2005\test_clip0501.tif');%先导入投影信息
% info=geotiffinfo('D:\data\LAIresult\clip\result\2005\test_clip0501.tif');
% nan1=a(1);
% a(a==nan1)=0;
% a=lai{1};
% % a(a<0|a>1000)=0;
% b=cumsum(a);
% [m,n]=size(a);
% data1=b(m,:);
% cnum=find(data1~=0);
% c=cumsum(a,2);
% data2=c(:,n);
% rnum=find(data2~=0);
% a1=lai{49};
% a1(a1==a1(1))=0;
% b=cumsum(a1);
% [m,n]=size(a1);
% data1=b(m,:);
% cnum1=find(data1~=0);
% c=cumsum(a1,2);
% data2=c(:,n);
% rnum1=find(data2~=0);
% % data=a(rnum(1):(rnum(1)+769),:);
% % data=data(:,cnum(1):(cnum(1)+920));
% % [a1,R1]=geotiffread('D:\pre\2005\pre\pre_01.tif');
% % a1(a1<0)=0;

%% import SPI  
% for i=49:72
year=1990:2019;
% e=dir('D:\学习\LAIresult\2005\*.tif'); 
path1='G:\drought\Anusplin\SPI\SPI-3TIF\';
for i=1:length(year)
    filepath{i}=strcat(path1,num2str(year(i)),'.tif');
end
for k=1:length(year)
    e=dir([filepath{k},'*.tif']);
    for i=1:size(e,1)
      spi{12*(k-1)+i}=importdata([filepath{k},e(i).name]);
    end
end
     % geotiffwrite(e(i)
%     d=lai{i};
%     d(isnan(d))=0;
%     lai{i}=d;
% end
% a=lai{49};
% b=cumsum(a);
% data1=b(1057,:);
% cnum1=find(data1~=0);
% c=cumsum(a,2);
% data2=c(:,1790);
% rnum1=find(data2~=0);
% for i=1:size(lai,2)
%     d=lai{i};
%     d=d((1560-950):1560,:);
%     d=d(:,cnum(1):(cnum(1)+964));
%     lai{i}=d;
% end
%% import SSI
path2='G:\liang\SPI\';
for i=1:length(year)
    filepath{i}=strcat(path2,num2str(year(i)),'\');
end
for k=1:length(year)
    e=dir([filepath{k},'*.tif']);
    for i=1:size(e,1)
      ssi{12*(k-1)+i}=importdata([filepath{k},e(i).name]);
      %d1=pre{12*(k-1)+i}; 
      %d1(d1<0)=0;
      %pre{12*(k-1)+i}=d1;
     % geotiffwrite(e(i).name,data,R,'GeoKeyDirectoryTag',info.GeoTIFFTags.GeoKeyDirectoryTag);
    end
end
%% get the time series and calculate the information transfer
 nan1=spi{1}(1);
 for i=1:358
     aa=spi{i};
     aa(isinf(aa))=0;
     aa(isnan(aa))=0;
     aa(aa==nan1)=0;
     spi{i}=aa;
 end
 for i=1:358
     aa=ssi{i};
     aa(isinf(aa))=0;
     aa(isnan(aa))=0;
     ssi{i}=aa;
 end
 for i=1:358
     d=spi{i};
     d(isinf(d))=0;
     d(isnan(d))=0;
     if size(d,1)==762
         d=[zeros(1,783);d];
     end
%      if size(d,1)==756
%           d=[zeros(7,780);d];
%      end
%      d=d(13:626,:);
%      d=d(:,25:681);
%      d(d==nan1)=0;
     d=d(1:763,1:775);
     spi{i}=d;
 end
 
 [m,n]=size(ai{1});
 t21=zeros(m,n);
 t12=zeros(m,n);
 coeff=zeros(m,n);
    for j=1:m
        for k=1:n
           for i=1:120
               x1(i)=ai{i}(j,k);
               x2(i)=esi{i}(j,k);
           end
           if sum(x1)~=0&&sum(x2)~=0
%                x1=x1/sum(x1);
%                x2=x2/sum(x2);
               x1=x1(1:119);
               x2=x2(2:120);
%                coeff(j,k)=myPearson(x1,x2);
               [T21, err90_21, err95_21, err99_21] = causality_est(x1', x2', 1);
               [T12, err90_12, err95_12, err99_12] = causality_est(x2', x1', 1);
               t21(j,k)=T21;
               t12(j,k)=T12;
%                [tau21, dH1_star, dH1_noist] = tau_est(x1', x2', 1);
%                [tau12, dH2_star, dH2_noist] = tau_est(x2', x1', 1);
           end
%            rt21(j,k)=tau21;
%            rt12(j,k)=tau12;;/
        end
    end
  [a,R]=geotiffread('D:\data\ESI\2005\01.tif');
   info=geotiffinfo('D:\data\ESI\2005\01.tif');
%
%    imwrite( uint8(t21),'D:\data\t21.tif','tif' ) 
b=zeros(3,758);
t21=[t21;zeros(77,548)];
t21=[t21,zeros(763,227)];
t12=[t12;zeros(77,548)];
t12=[t12,zeros(763,227)];
% geotiffwrite('D:\data\AI_proj\AI_ESI1mon.tif',abs(t12),R,'GeoKeyDirectoryTag',info.GeoTIFFTags.GeoKeyDirectoryTag);
% geotiffwrite('D:\data\AI_proj\ESI_AI1mon.tif',abs(t21),R,'GeoKeyDirectoryTag',info.GeoTIFFTags.GeoKeyDirectoryTag);
geotiffwrite('D:\data\ESI\result\ESI_AI1mon.tif',abs(t21),R,'GeoKeyDirectoryTag',info.GeoTIFFTags.GeoKeyDirectoryTag);
geotiffwrite('D:\data\ESI\result\AI_ESI1mon.tif',abs(t12),R,'GeoKeyDirectoryTag',info.GeoTIFFTags.GeoKeyDirectoryTag);
%coeff=[coeff;zeros(79,547)];
%coeff=[coeff,zeros(763,228)];
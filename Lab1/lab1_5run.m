np = [1e3,1e5,1e7];
nd = 10;
for i = 1:3
   t(i,1) = lab1_5(np(i),nd); 
end
graphMe5([0,2,4],t);
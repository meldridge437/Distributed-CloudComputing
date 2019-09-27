np = [1e3,1e5,1e7];
for nd = 1:10
    for i = 1:3
        [~,t(i,nd)] = lab1_1(np(i),nd);
    end
end
graphMe([0,2,4],t);
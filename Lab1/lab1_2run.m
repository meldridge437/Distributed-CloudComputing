np = [1e3,1e5,1e7];
nd = 10; 
mnct = 8;
for nw = 1:mnct
    for i = 1:3
        [~,t(i,nw)] = lab1_2(np(i),nd,nw);
    end
end
graphMe2([1:mnct],t);
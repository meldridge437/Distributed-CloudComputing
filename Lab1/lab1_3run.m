% requires lab1_1, lab1_2, graphMe, graphMe_loni.m
np = [1e3,1e5,1e7];

% run through sequential tests
for nd = 1:10
    for i = 1:3
        [~,t(i,nd)] = lab1_1(np(i),nd);
    end
end
% store results in a graph (for.png)
graphMe([0,2,4],t);

% for testing purposes, lock num dimentions at 10
nd = 10;
% for LONI testing 
mnct = 20;
for nw = 1:mnct
    for i = 1:3
        [~,t2(i,nw)] = lab1_2(np(i),nd,nw);
    end
end
% store results in a graph (parfor.png)
graphMe2_loni([1:mnct],t2);
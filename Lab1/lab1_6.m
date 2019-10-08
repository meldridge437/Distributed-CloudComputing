np=1e7; nd=10;
hp = gcp('nocreate');
if isempty(hp) , hp=parpool(4); end
tic;
spmd
    if (labindex==1)
        A = randn(np,nd); B=randn(np,nd);
        C = A-B;
        labSend(C,2);
    elseif (labindex==2)
        C = labReceive(1);
        D = C.^2;
        labSend(D,3);
    elseif (labindex==3)
        D = labReceive(2);
        E = sum(D,2);
        labSend(E,4);
    elseif (labindex==4)
        E = labReceive(3);
        F = sqrt(E);
        %G = labSend(F,1);
    end
end
%d1 = G{4};
t = toc
delete(hp);

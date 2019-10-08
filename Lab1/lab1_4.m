function t = lab1_4(np,nd)
if(nargin < 1), np=1e7; nd=10; end
nl = 8;
tic;
spmd
    A=randn(np/nl,nd); 
    B=randn(np/nl,nd);
    c=zeros(np/nl,1);
    for i = 1:np/nl
        for j = 1:nd
            c(i) = c(i) + (B(i,j)-A(i,j)).^2;
        end
        c(i)=sqrt(c(i));
    end
    da = gcat(c,1,1);
end
t = toc;


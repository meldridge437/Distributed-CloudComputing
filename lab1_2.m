function [c,t] = lab1_2(np,nd,nw)
if(nargin < 1), np=1e7; nd=10; nw=4; end
hp = gcp('nocreate');
if isempty(hp) , hp=parpool(nw); end
A=randn(np,nd);
B=randn(np,nd);
c=zeros(np,1);
tic;
parfor i = 1:np
    for j = 1:nd
        c(i) = c(i) + (B(i,j)-A(i,j)).^2;
    end
    c(i)=sqrt(c(i));
end
t = toc;
delete(hp);
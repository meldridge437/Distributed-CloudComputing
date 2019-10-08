function t = lab1_5(np,nd)
if(nargin < 1), np=1e7; nd=10; end
hp = gcp('nocreate');
if isempty(hp), hp = parpool(8); end
aA=randn(np,nd); aB=randn(np,nd);
dA=distributed(aA); dB=distributed(aB);
d=zeros(np,1);
tic;
dc = sqrt(sum((dA-dB).^2,2));
d = gather(dc);
t = toc;
delete(hp);
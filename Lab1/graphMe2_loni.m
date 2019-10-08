function graphMe2_loni(X1, YMatrix1)
%CREATEFIGURE(X1, YMatrix1)
%  X1:  vector of x data
%  YMATRIX1:  matrix of y data

%  Auto-generated by MATLAB on 26-Sep-2019 10:12:11

% Create figure
figure1 = figure('NumberTitle','off','Name','Time vs Workers');

% Create axes
axes1 = axes('Parent',figure1);
hold(axes1,'on');

% Create multiple lines using matrix input to plot
plot1 = plot(X1,YMatrix1,'Parent',axes1);
set(plot1(1),'DisplayName','1e3');
set(plot1(2),'DisplayName','1e5');
set(plot1(3),'DisplayName','1e7');

% Create ylabel
ylabel({'Time(s)'});

% Create xlabel
xlabel({'Number of Workers'});

% Create title
title('Time vs Workers (LONI)');

box(axes1,'on');
% Create legend
legend1 = legend(axes1,'show');
set(legend1,'Location','east');
title(legend1,'Number of Points');
saveas(gcf,'parfor.png');

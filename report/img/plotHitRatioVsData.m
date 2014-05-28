clear all;
binary = importdata('hitrate-vs-data-dt1.csv');
count = importdata('hitrate-vs-data-dt2.csv');
L2 = importdata('hitrate-vs-data-dt3.csv');
zeroone = importdata('hitrate-vs-data-dt4.csv');

numArticles = 503;

x = ceil(numArticles*[0.01 0.02 0.03 0.04 0.08 0.16 0.32 0.64 1]);
titles = {'Bernoulli', 'Multinomial', 'Random Forest', 'SVM', 'Hybrid'};
j=0;
for i=9:13
    j=j+1;
    figure()
    plot(x,binary(:,i),'ks-',x,count(:,i),'ko-',x,L2(:,i),'kv-',x,zeroone(:,i),'k^-');
    title(titles(j));
    xlabel('Number of articles in training data')
    ylabel('Hit ratio')
    xlim([0 numArticles]);
    ylim([0.5 0.8]);
    if i==13
        legend('Binary','Count','L2-normalized','0-1 mapped','Location','NorthEastOutside')
    end
    filename = strcat('hitratio-vs-data-',titles{j},'.tikz');
    matlab2tikz(filename, 'height', '\figureheight', 'width', '\figurewidth');
end
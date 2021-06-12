dane = csvread('wig20.csv');
d = dane(2:end,5);
plot(d, 'r-;wig20;')
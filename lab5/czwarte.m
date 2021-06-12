dane = csvread('wig20.csv');
y = dane(2:end,5);
size(y)
x = [0:1:246];
xrot = rot90(x);
flip(xrot);
p = polyfit(xrot, y, 5);
ydane = polyval(p, x);
ydane = fliplr(ydane);
plot(y, 'r-;dane;',ydane,'b.;aprox;')
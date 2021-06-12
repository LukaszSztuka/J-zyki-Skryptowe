x=0;
function y = drugi(x)
  y(1) = x(1)^2 + 2*x(1)*x(2)^2 - 40;
  y(2) = 2*x(1)^2 - 3*x(2)^2 + 19;
endfunction;
[x] = fsolve ("drugi", [1,2])
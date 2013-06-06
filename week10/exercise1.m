clear all;
close all;
%% % Enter the measured data points by hand
x = [-10 -9 -8 -7 -6 -5 -4 -3 0];
y = [2.65 2.10 1.90 1.40 1.00 0.80 0.60 0.30 0.00];
ey = [0.1 0.1 0.1 0.1 0.05 0.05 0.05 0.05 0.2];
% Plot the data with error bars
figure(1)
errorbar(x,y,ey,'b.')
% Don't forget the labels
xlabel('x (mm)')
ylabel('y (mm)')
axis equal

%%
hold on
% Do something else now that the first part works.
[m, b, merror, berror] = WeightedLSQFit(x,y,ey.^-2);
fitted = m*x + b;
plot(x, fitted);

hold off

%%
% Do something in a second figure window.
func = @(a,b,c,x) - sqrt(a^2-(x-b).^2)+c;
% fit the data
fittedmodel = fit(x',y',func,'StartPoint',[15 0 15]);
% plot the result
figure(2)
plot(fittedmodel,'r-');

% fit the data using the uncertainties as weights
w = ey.^-2
weightedfitted = fit(x',y',func,'StartPoint',[15 0 15],'Weights',w')
% plot the result
figure(3)
plot(weightedfitted,'r-');
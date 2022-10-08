% Example of using causality_est.m.
% Shown here is the 1st case in Table 1 in Liang (2014) [1].
% The accurate result should be T21=0.11, T12=0.
%
% It is found that the pseudorandom number generator has problems in
% producing sample paths from a stochastic differential equation (see the
% footnote of Liang 2015[2]). We provide in this directory a pair of
% the series generated in [1].
%
% There is a typo in the caption of the Fig. 5 of [1]. The unit should be
% nats/year, not nats/month.
%
% References
% [1] X.S. Liang, 2014: Unraveling the cause-effect relation between time
%     series. Phys. Rev. E 90, 052150.
% [2] X.S. Liang, 2015: Normalizing the causality between time series.
%     Phys. Rev. E 92, 022126.
% [3] X.S. Liang, 2016: Information flow and causality as rigorous notions
%     ab initio. Phys. Rev. E 94, 052201.
%
%

x = load('G:\liang\sedissi.dat'); % remove the remarks in the file first.

range = 1:360;
t = x(range, 1);
x1 = x(range, 2);
x2 = x(range, 3);

dt = t(2) - t(1);

[T21, err90_21, err95_21, err99_21] = causality_est(x1, x2, 1);
[T12, err90_12, err95_12, err99_12] = causality_est(x2, x1, 1);

T21 = T21 / dt;
T12 = T12 / dt;

%%%%%% The following is a test of tau_est...  %%%%%%%%
%%%%%% tau21 = 5.47%,  tau12 = -0.096%

[tau21, dH1_star, dH1_noist] = tau_est(x1, x2, 1);
[tau12, dH2_star, dH2_noist] = tau_est(x2, x1, 1);
% tau21 & tau12 are in [-1 1]

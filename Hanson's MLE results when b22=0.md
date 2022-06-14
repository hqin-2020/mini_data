







# Hanson's MLE Estimation Results for $b_{21} = 0$



- The maximum log likelihood is **2178.2278**

$$
\begin{aligned}
Z_{t+1} &=\begin{bmatrix}0\\0.0004\end{bmatrix}+\begin{bmatrix}
1&1\\
0&0.9048
\end{bmatrix}
\begin{bmatrix}Z_t^1\\Z_t^2\end{bmatrix}
+ \begin{bmatrix}
0.0034\\
-0.0012
\end{bmatrix}W_{t+1}^z\\
S_{t+1}&=\begin{bmatrix}
0.0530\\0.2483\\0.4542
\end{bmatrix}+
\underbrace{\begin{bmatrix}
0.5229&0.0343& 0.0018\\-2.5682&1.166& 0.0044\\-4.1665&0.3062&1.0088
\end{bmatrix}}_{\mbox{eigenvalues = (0.3844 , 0.9816, 0.9890)}}
S_t + \begin{bmatrix}
 0.0010&0&0\\0.0327&0.0040&0\\0.0060&-0.0382&0.0019
\end{bmatrix}
W_{t+1}^s
\end{aligned}
$$

- Stationary distribution for $S_t$

$$
\begin{aligned}
\mu_s &= \begin{bmatrix}
0.0096\\-1.2807\\-2.4823
\end{bmatrix}\\
\Sigma_s&=\underbrace{\begin{bmatrix}
0.0002&0.0025&0.0001\\
0.0025&0.0356&-0.0040\\
0.0001&-0.0040&0.0823
\end{bmatrix}}_\mbox{eigenvalues = (0.000004,0.0354, 0.0826)}
\end{aligned}
$$

- Initial Distribution used in Kalman Filter

$$
\begin{aligned}
Z_0|D_0& = \begin{bmatrix}
-4.5066\\
0.0042
\end{bmatrix}\\
S_0|D_0&=\begin{bmatrix}
0.0453\\-0.7481\\-2.9939
\end{bmatrix}\\
\Sigma_0^{z2}|D_0 &= 7.94\times10^{-6}\\
\Sigma_0^{s}|D_0 &= (4.71\times10^{-6})\mathbf{1}_n\mathbf{1}_n'

\end{aligned}
$$


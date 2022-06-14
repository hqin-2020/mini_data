







# Haomin's MLE Estimation Results when $b_{22} = 0$



- The maximum log likelihood is **2172.7521**
  $$
  \begin{aligned}
  Z_{t+1} &=\begin{bmatrix}0\\0.0007\end{bmatrix}+\begin{bmatrix}
  1&1\\
  0&0.8468
  \end{bmatrix}
  \begin{bmatrix}Z_t^1\\Z_t^2\end{bmatrix}
  + \begin{bmatrix}
  0.0048\\
  0.0009
  \end{bmatrix}W_{t+1}^z\\
  S_{t+1}&=\begin{bmatrix}
  -0.9765\\-1.0891\\-0.2226
  \end{bmatrix}+
  \underbrace{\begin{bmatrix}
  0.3490&0.0299&0.0163\\-0.6668&1.0084&0.0118\\-0.1509&0.0175&0.9975
  \end{bmatrix}}_{\mbox{eigenvalues = (0.3844 , 0.9816, 0.9890)}}
  S_t + \begin{bmatrix}
  -0.0008&0&0\\-0.0331&-0.0059&0\\-0.0105&0.0379&-0.0097
  \end{bmatrix}
  W_{t+1}^s
  \end{aligned}
  $$

  - Stationary distribution for $S_t$

  $$
  \begin{aligned}
  \mu_s &= \begin{bmatrix}
  -1.7502\\-3.0044\\-4.4744
  \end{bmatrix}\\
  \Sigma_s&=\underbrace{\begin{bmatrix}
  0.0001&0.0011&0.0027\\
  0.0011&0.0278&-0.0064\\
  0.0027&-0.0064&0.1205
  \end{bmatrix}}_\mbox{eigenvalues = (0.1210 , 0.000002, 0.0274)}
  \end{aligned}
  $$

  - Initial Distribution used in Kalman Filter

  $$
  \begin{aligned}
  Z_0|D_0& = \begin{bmatrix}
  -2.7251\\
  0.0047
  \end{bmatrix}\\
  S_0|D_0&=\begin{bmatrix}
  -1.7362\\-2.5296\\-4.7754
  \end{bmatrix}\\
  \Sigma_0^{z2}|D_0 &= 2.87\times10^{-6}\\
  \Sigma_0^{s}|D_0 &= (2.01\times10^{-6})\mathbf{1}_n\mathbf{1}_n'
  
  \end{aligned}
  $$

  
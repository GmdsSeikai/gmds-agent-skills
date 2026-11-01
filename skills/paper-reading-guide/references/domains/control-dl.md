# Domain Reference: Control and Deep Learning

Covers reinforcement-learning control, learning-based control, system identification, imitation learning, trajectory optimization with learning, and sim-to-real transfer.

## Problem Setting

Learn a policy or controller mapping states or observations to actions to optimize a long-term objective such as return, cost, or tracking error. Stability, constraints, safety, and sample efficiency often also matter.

Distinguish measurable states from partial observability (POMDP), continuous from discrete actions, and online interaction from offline data.

## Core Concepts

- **MDP, return, and discounting:** States, actions, and rewards; the objective is to maximize discounted cumulative return.
- **Model-free and model-based:** Learn a policy or value directly, or learn environment dynamics and then plan.
- **On-policy and off-policy:** Use data from the current policy or reuse historical data, with substantial sample-efficiency implications.
- **Actor-critic:** Combine a policy (actor) and value estimator (critic); common examples include PPO, SAC, TD3, and DDPG.
- **Offline RL:** Learn solely from a fixed dataset without further interaction; distribution shift and extrapolation error are key difficulties.
- **Imitation learning:** Learn from expert demonstrations; examples include behavioral cloning (BC), DAgger, and adversarial GAIL.
- **MPC with learning:** Use neural networks for dynamics, costs, or terminal values in model predictive control, or learn an approximate MPC policy.
- **System identification and neural dynamics:** Fit system dynamics using neural networks, including Neural ODEs.
- **Koopman:** Lift nonlinear dynamics into a higher-dimensional approximately linear representation for linear control tools.
- **Stability and safety:** Lyapunov functions, control barrier functions (CBFs), constrained RL, and reachability.
- **Sim-to-real:** The gap between simulation training and real deployment; domain randomization, system identification, and domain adaptation are ways to address it.

## Datasets and Benchmarks

MuJoCo, DeepMind Control Suite, OpenAI Gym/Gymnasium, Atari, Meta-World, robosuite, and Isaac Gym/Lab; D4RL for offline RL. For physical robots, inspect the authors' own platform.

## Common Metrics

- Episode return or cumulative reward, success rate, tracking or control error.
- Sample efficiency (interaction steps needed to reach a performance level), asymptotic performance, training stability or variance.
- Generalization across tasks, initial conditions, and dynamics disturbances; performance loss from sim-to-real transfer.
- For safety: constraint-violation counts or boundary-violation rates.

## Domain-Specific Questions

- Are states measurable or partially observed? Are actions continuous or discrete? Is data online or offline?
- Which method family applies: model-free, model-based, imitation, MPC with learning, offline RL, or another family above?
- How is reward or cost designed? Are reward shaping or sparse rewards relevant?
- Is the main claim sample efficiency or asymptotic performance? Which baselines are used: PPO/SAC or classical control, for example?
- Are stability, safety, or constraint guarantees given? Are they empirical or theoretical?
- Is validation in simulation or on hardware? How large is the sim-to-real drop, and what transfer techniques are used?
- How many random seeds are used, and how large is the variance? RL results are sensitive to seeds.

## Optional Summary Fields

- Task setting: measurable or partially observed states, continuous or discrete actions, online or offline data.
- Method family: model-free / model-based / imitation / MPC with learning / offline RL.
- Main emphasis: sample efficiency or asymptotic performance.
- Stability, safety, and constraint guarantees: present or absent, empirical or theoretical.
- Validation: simulation or hardware, sim-to-real loss, seed count, and variance.

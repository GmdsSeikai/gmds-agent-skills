# Domain Reference: Network and Graph Optimization

Use for graph-based decisions about network placement, routing, connectivity, flow, or link selection, including dynamic networks. Add an offloading or learning sheet only when that mechanism is actually involved.

## Identify the Graph and Objective

- Locate vertices, directed or undirected edges, weights, capacities, terminals, and decision variables. Separate the physical topology from workload graphs and auxiliary graphs constructed by the solver. Explain the meaning and units of each relevant edge type.
- Identify what is minimized or maximized and what makes a solution feasible. Minimum cut, maximum flow, and minimum spanning tree solve different objectives; choose from the paper's formulation, not from a title or diagram's appearance. A spanning tree's total edge weight is not automatically end-to-end latency or throughput.
- Separate **solution quality** (such as cut value, flow value, or total tree weight) from **solver runtime** and update latency. Faster computation alone does not mean a better objective value.

## Follow Transformations and Guarantees

- For a reduction, map each original feasible choice to the transformed representation, account for its objective value, and inspect the reverse mapping. State feasibility or equivalence only under the conditions actually established. A numerical example is intuition, not proof.
- For min-cut/max-flow, locate directionality, capacities, source/sink construction, and the conditions used for optimality. For MST, locate the graph and connectivity conditions and how ties or disconnected cases are handled when relevant. Do not assume a named algorithm solves the paper's entire constrained problem.
- Read theorem assumptions and proof scope before generalizing: restricted topologies, fixed parameters, available information, or cost properties may be essential. Distinguish author claims, results whose relevant argument has been checked, and assistant inference.
- Read complexity in terms of the paper's variables and operations. Separate worst-case, amortized, and empirical runtime, preprocessing from updates, and one update from a complete time horizon.

## Dynamic and Prediction-Assisted Methods

- Identify what changes: edge existence, capacity, weight, demand, or a time-indexed topology. Trace which old state is reused (tree, residual network, flow, or other state), how feasibility is restored, and when recomputation is needed. A previously optimal solution need not remain feasible or optimal after an update.
- If predictions help, locate what is predicted, where predictions come from, and how the algorithm consumes them. "Learning-augmented" or "prediction enhancement" does not establish a neural predictor, training procedure, or learned loss. Check error handling or fallback only when assessing such a claim; leave it unresolved if the relevant source is unavailable.
- DNNs in a network paper may be inference workloads whose execution is optimized. Do not turn that into a study of model training without source evidence.

## Explain and Evaluate Selectively

Teach scene → model → algorithm → guarantee conditions → experiments flexibly around the current question. Use a small graph when helpful, labeling invented weights and teaching simplifications. Locate the corresponding construction or algorithm before drawing causal links.

For a runtime or quality comparison, inspect the change sequence, graph sizes, baselines, implementation settings, and whether prediction/preprocessing costs are included. Distinguish synthetic or trace-driven simulation from real deployment. Empirical speedups on selected networks do not prove general complexity or deployment robustness.

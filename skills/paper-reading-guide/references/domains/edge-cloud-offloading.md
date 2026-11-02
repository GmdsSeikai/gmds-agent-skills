# Domain Reference: Edge-Cloud Offloading

Use for deciding where application tasks or DNN inference stages execute across devices, edge nodes, and cloud resources. Combine with network optimization when a graph algorithm solves the placement problem. Select cues relevant to the user's current question.

## Establish the Model

- Separate the **task graph** from the **physical network**. Task vertices represent computations; task edges represent dependencies and transferred data. Physical vertices represent execution locations; physical edges represent communication links. Confirm each meaning in the paper. A task DAG does not imply that the physical network is a DAG.
- Identify the placement variables and their domains: binary edge/cloud choices, multiple locations, replication, or scheduling decisions only as defined. Locate fixed source/sink tasks and allowed locations. A DNN in the workload may be a fixed inference chain rather than a model being trained.
- Read computation costs with their units and location dependence. For communication costs, identify data volume, direction, link rate or delay, and any startup cost. Include asymmetric directions and communication within the same side only when the paper models them; never assume all same-side costs vanish.
- Separate precedence constraints from capacity, resource, location, and scheduling constraints. Determine whether transfers and computations overlap or contend and whether those effects are modeled. Do not import a scheduler into a placement-only model.

## Explain the Decision

Start from the scenario and the difficult trade-off, then connect model, algorithm, guarantee conditions, and experiments as needed; this is a flexible explanation path, not a required sequence.

- Define the objective precisely: application completion time, a sum of task/transfer costs, energy, monetary cost, throughput, or a weighted combination. A cost sum is not automatically wall-clock completion time for parallel branches. Preserve the paper's definition.
- For a graph reduction, map placement choices to the constructed graph and explain what its edge weights count. Distinguish this auxiliary graph from both the task DAG and physical network. Consult the network-optimization sheet for equivalence and feasibility conditions.
- Keep "optimal" tied to the stated objective, feasible set, topology, and assumptions. An exact result for a restricted model does not establish optimality under arbitrary contention, mobility, or resource limits.
- Separate optimizing inference deployment from training the DNN. Discuss losses or training only when they participate in the paper's mechanism.

## Teach and Check Selectively

When helpful, use two tasks and two locations to expose one trade-off. Label invented values and simplifying assumptions, compute the relevant terms, and return to the source equation. A toy calculation illustrates the objective; it does not prove the reduction or theorem. In a diagram, label task dependencies, physical links, and auxiliary edges separately.

For an experimental claim, locate the workload, topology, cost model, baselines, and metric. Ask only the questions needed to assess it: are resources and transfer assumptions comparable, what changes with task size or network conditions, and is evidence simulation or measured deployment? Do not infer unmodeled robustness from a favorable average.

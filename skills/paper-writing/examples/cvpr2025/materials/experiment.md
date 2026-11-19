# Synthetic preprocessing latency

This fixture was created from scratch for public workflow testing. The rows are
handwritten synthetic latencies, in milliseconds per image. No preprocessing
implementation ran to produce them.

Each of the sequential, batched, and reference groups contains five fixture rows.
The reference group lets a reviewer distinguish equal aggregates
that belong to different observations. Report the arithmetic mean and display
all rows. Compare the sequential and batched means by subtracting the latter
from the former. The fixture supports descriptive arithmetic within the sample.

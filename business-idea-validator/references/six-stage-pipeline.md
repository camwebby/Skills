# Six-Stage Validation Pipeline

Run these stages sequentially. Treat each stage as a dedicated agent with a decision gate. A later stage should not erase failures in an earlier stage; it can only explain or mitigate them.

## Stage 1: Problem and Market Validation

Core question: is this a real problem worth solving?

Check:
- painful, frequent, expensive, or strategically important problem
- current workarounds and spending
- evidence from customer conversations, communities, search demand, reviews, support tickets, or existing products
- urgency and cost of inaction

Decision gate:
- `pass`: repeated pain plus evidence of active workaround or spend
- `conditional`: pain exists but urgency or segment specificity is unclear
- `fail`: problem is nice-to-have, infrequent, or unsupported
- `unknown`: insufficient evidence

## Stage 2: Customer and ICP Validation

Core question: who exactly has the problem and who pays?

Check:
- specific ICP, buyer, user, influencer, and approver
- segment where pain is concentrated
- budget owner and procurement path
- adoption blockers, data/access needs, trust requirements

Decision gate:
- `pass`: clear ICP and buyer with reachable early adopters
- `conditional`: likely ICP but buyer path or segment priority is unclear
- `fail`: user and buyer are vague or misaligned
- `unknown`: not enough customer evidence

## Stage 3: Competitive and Positioning Validation

Core question: why will this win despite alternatives?

Check:
- direct competitors
- indirect competitors and workarounds
- incumbent bundling/copy risk
- differentiation that customers understand
- wedge and beachhead use case

Decision gate:
- `pass`: clear wedge against real alternatives
- `conditional`: differentiation exists but moat or switching reason is weak
- `fail`: no clear reason to switch or pay
- `unknown`: competitor landscape not researched

## Stage 4: Business Model and Unit Economics Validation

Core question: can this become a viable business?

Check:
- pricing basis and willingness-to-pay
- gross margins and service burden
- CAC/payback plausibility
- retention/expansion potential
- monetization fit with value delivered

Decision gate:
- `pass`: plausible price, buyer budget, and acquisition path
- `conditional`: monetization possible but unproven
- `fail`: value exists but cannot be captured economically
- `unknown`: no pricing or budget evidence

## Stage 5: Feasibility, Operations, and Trust Validation

Core question: can this be built, delivered, and trusted?

Check:
- technical complexity and dependencies
- data availability and integrations
- security, privacy, regulatory, and compliance constraints
- onboarding, support, implementation, and quality-control burden
- operational bottlenecks

Decision gate:
- `pass`: build and delivery risks are bounded
- `conditional`: feasible but one major dependency requires proof
- `fail`: core value depends on unavailable data, trust, regulation, or impossible operations
- `unknown`: feasibility not assessed

## Stage 6: GTM and Execution Roadmap Validation

Core question: can the team reach and convert early customers?

Check:
- first channel and first 100-customer path
- outbound, inbound, partner, product-led, or community motion
- sales cycle, buyer education, onboarding friction
- founder access to the segment
- first experiments and milestones

Decision gate:
- `pass`: credible first channel and testable route to early customers
- `conditional`: channel hypotheses exist but need testing
- `fail`: no believable acquisition path
- `unknown`: GTM not specified

## Stage Output Format

| Stage | Agent | Core question | Confidence | Gate | Supporting evidence | Opposing evidence | Next action |
|---|---|---|---:|---|---|---|---|
